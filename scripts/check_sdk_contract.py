#!/usr/bin/env python3
"""Offline Pandadata consumer contract check; never imports project code or logs credentials."""

import argparse
import ast
import json
import pathlib
import re
import textwrap
import subprocess

PACKAGE = re.compile(r"\bpanda[_-]data\s*((?:(?:===|==|>=|<=|~=|!=|>|<)\s*\d[\w.*+-]*(?:\s*,\s*)?)+)", re.I)



VERSION = re.compile(r"(?:SDK_VERSION|PANDADATA_VERSION|PANDA_DATA_VERSION)\s*=\s*['\"]([0-9]+(?:\.[0-9]+)+)['\"]")



def inspect_versions(text, path):
    versions = []
    is_python = pathlib.PurePosixPath(path).suffix == ".py"
    expected_guard = is_python and re.search(r'version\(["\']panda[_-]data["\']\)', text)
    compatibility = path.endswith("compatibility.ts") and "PANDA_SDK_COMPATIBILITY" in text
    for line_no, line in enumerate(text.splitlines(), 1):
        for match in PACKAGE.finditer(line):
            versions.append({"line": line_no, "constraint": re.sub(r"\s+", "", match[1]).rstrip(","), "source": "package"})
        if is_python:
            for match in VERSION.finditer(line):
                versions.append({"line": line_no, "constraint": "==" + match[1], "source": "runtime_guard"})
            if expected_guard:
                for match in re.finditer(r'EXPECTED\s*=\s*["\']([0-9.]+)["\']', line):
                    versions.append({"line": line_no, "constraint": "==" + match[1], "source": "runtime_guard"})
        if compatibility:
            for match in re.finditer(r'version:\s*["\']([0-9.]+)["\']', line):
                versions.append({"line": line_no, "constraint": "==" + match[1], "source": "compatibility_matrix"})
    return versions



def inspect_python(code, contracts):
    result = {"imports": False, "calls": [], "issues": [], "parse_error": False, "dynamic_dispatch": []}
    try:
        tree = ast.parse(textwrap.dedent(code))
    except (SyntaxError, ValueError):
        result["parse_error"] = True
        return result
    modules, functions = {"panda_data"}, {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "panda_data":
                    modules.add(alias.asname or alias.name)
                    result["imports"] = True
        elif isinstance(node, ast.ImportFrom) and node.module == "panda_data":
            result["imports"] = True
            for alias in node.names:
                functions[alias.asname or alias.name] = alias.name
    for _ in range(2):
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            value = node.value
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            is_module = isinstance(value, ast.Name) and value.id in modules
            if isinstance(value, ast.Call):
                if isinstance(value.func, ast.Name) and value.func.id in {"init_pandadata", "ensure_pandadata", "get_pandadata"}:
                    is_module = True
                if value.args and isinstance(value.args[0], ast.Constant) and value.args[0].value == "panda_data":
                    if isinstance(value.func, ast.Attribute) and value.func.attr == "import_module" or isinstance(value.func, ast.Name) and value.func.id == "__import__":
                        is_module = True
                if isinstance(value.func, ast.Name) and value.func.id == "getattr" and value.args and isinstance(value.args[0], ast.Name) and value.args[0].id in modules:
                    literal = len(value.args) > 1 and isinstance(value.args[1], ast.Constant) and isinstance(value.args[1].value, str)
                    for target in targets:
                        if isinstance(target, ast.Name) and literal:
                            functions[target.id] = value.args[1].value
                    if not literal:
                        result["dynamic_dispatch"].append(value.lineno)
            if is_module:
                modules.update(t.id for t in targets if isinstance(t, ast.Name))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = None
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id in modules:
            name = node.func.attr
        elif isinstance(node.func, ast.Name):
            name = functions.get(node.func.id)
        if not name or not (name.startswith("get_") or name == "init_token"):
            continue
        keywords = {kw.arg: kw.value for kw in node.keywords if kw.arg}
        dynamic = any(kw.arg is None for kw in node.keywords) or any(isinstance(a, ast.Starred) for a in node.args)
        call = {"method": name, "line": node.lineno, "keywords": sorted(keywords), "dynamic": dynamic}
        result["calls"].append(call)
        contract = contracts.get(name)
        if contract is None:
            result["issues"].append({"rule": "unexported_method", "line": node.lineno, "detail": name})
            continue
        declared = contract["parameters"]
        unknown = sorted(set(keywords) - set(declared))
        if unknown:
            result["issues"].append({"rule": "unknown_keyword", "line": node.lineno, "detail": name + ": " + ", ".join(unknown)})
        provided = set(keywords) | set(declared[:len(node.args)])
        if not dynamic:
            missing = sorted((set(contract.get("required", [])) | set(contract.get("runtime_required", []))) - provided)
            if missing:
                result["issues"].append({"rule": "missing_runtime_parameter", "line": node.lineno, "detail": name + ": " + ", ".join(missing)})
        empty = sorted(key for key, value in keywords.items() if key in contract.get("runtime_required", []) and isinstance(value, ast.Constant) and value.value in (None, ""))
        if empty:
            result["issues"].append({"rule": "empty_required_parameter", "line": node.lineno, "detail": name + ": " + ", ".join(empty)})
    result["dynamic_dispatch"] = sorted(set(result["dynamic_dispatch"]))
    return result



def scope(path):
    parts = pathlib.PurePosixPath(path.lower()).parts
    if any(x in parts for x in ("vendor", "vendored", "node_modules", ".agents", ".claude", ".codex", ".cursor", "skills_demo", "shared-skills", "library-v2")) or "public/skills/" in path.lower():
        return "embedded"
    if any(x in parts for x in ("tests", "test", "fixtures")) or pathlib.PurePosixPath(path).name.startswith("test_"):
        return "test"
    if any(x in parts for x in ("examples", "example", "demo")):
        return "example"
    if pathlib.PurePosixPath(path).suffix.lower() in {".md", ".rst", ".mdc", ".html"}:
        return "documentation"
    return "runtime"




def check(root, manifest, include_docs=False):
    contracts = manifest["methods"]
    expected = manifest["sdk_version"]
    try:
        paths = subprocess.check_output(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=root).decode("utf-8").split("\0")
    except subprocess.CalledProcessError:
        paths = [str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()]
    issues, scanned, dynamic = [], 0, []
    versions = []
    for relative in paths:
        if not relative or scope(relative) == "embedded" or any(p in pathlib.PurePosixPath(relative).parts for p in (".git",".venv","node_modules","__pycache__")):
            continue
        path = root / relative
        if not path.is_file() or path.suffix not in {".py",".md",".mdc",".toml",".txt",".yml",".yaml",".ts"}:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (UnicodeError, OSError):
            continue
        if scope(relative) == "runtime":
            versions.extend({**v,"path":relative} for v in inspect_versions(text,relative))
        blocks = [(text,0)] if path.suffix == ".py" and scope(relative) in {"runtime","example"} else []
        if include_docs and path.suffix in {".md",".mdc"}:
            blocks = [(m[1],text[:m.start(1)].count("\n")) for m in re.finditer(r"```(?:python|py)\s*\n(.*?)```",text,re.S)]
        for code, offset in blocks:
            if not re.search(r"panda_data|init_pandadata",code):
                continue
            scanned += 1
            result = inspect_python(code,contracts)
            if result["parse_error"] and path.suffix == ".py":
                issues.append({"path":relative,"line":offset+1,"rule":"syntax_error","detail":"Python source cannot be parsed"})
            for issue in result["issues"]:
                issues.append({**issue,"path":relative,"line":issue["line"]+offset})
            dynamic.extend({"path":relative,"line":line+offset} for line in result["dynamic_dispatch"])
    pins = [v for v in versions if v["constraint"].startswith("==")]
    matrix = [v for v in pins if v["source"] == "compatibility_matrix"]
    for v in pins:
        if v["source"] != "compatibility_matrix" and v["constraint"] != "=="+expected:
            issues.append({"path":v["path"],"line":v["line"],"rule":"sdk_version_mismatch","detail":v["constraint"]+"; expected =="+expected})
    if matrix and not any(v["constraint"] == "=="+expected for v in matrix):
        issues.append({"path":matrix[0]["path"],"line":matrix[0]["line"],"rule":"sdk_matrix_missing","detail":expected})
    return {"sdk_version":expected,"scanned_python_blocks":scanned,"issues":issues,"dynamic_dispatch_requires_project_tests":dynamic,
            "live_service":"not_tested"}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=pathlib.Path,default=pathlib.Path.cwd())
    parser.add_argument("--contract",type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]/"references/sdk-contract.json")
    parser.add_argument("--include-docs",action="store_true")
    parser.add_argument("--output",type=pathlib.Path)
    args=parser.parse_args()
    result=check(args.root.resolve(),json.loads(args.contract.read_text(encoding="utf-8")),args.include_docs)
    output=json.dumps(result,ensure_ascii=False,indent=2)
    if args.output:
        args.output.write_text(output+"\n",encoding="utf-8")
    print(output)
    return int(bool(result["issues"]))


if __name__ == "__main__":
    raise SystemExit(main())
