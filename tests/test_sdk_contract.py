"""Offline contract checks against the installed, pinned Pandadata wheel.

Run: python -m unittest discover -s tests -v
No login or data requests are made.
"""

import ast
import inspect
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

import panda_data

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_method_index import parse_methods, render_markdown
from sdk_compat import DOCUMENTED_ONLY_METHODS, require_sdk_version
from search_api_docs import method_spans


class SDKContractTests(unittest.TestCase):
    def run_cli(self, script, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script), *args],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
        )

    def test_supported_release(self):
        self.assertEqual(require_sdk_version(), "1.0.4")

    def test_all_data_exports_have_searchable_sections(self):
        documented = {item["method"] for item in parse_methods(ROOT / "references/api-docs.md")}
        exported = {
            name for name in dir(panda_data)
            if name.startswith("get_") and callable(getattr(panda_data, name))
        } - {"get_client", "get_factory", "get_token_ttl"}
        self.assertEqual(documented, exported)
        self.assertFalse(DOCUMENTED_ONLY_METHODS)

    def test_parameter_tables_match_sdk(self):
        lines = (ROOT / "references/api-docs.md").read_text(encoding="utf-8").splitlines()
        for name, _, start, end in method_spans(lines):
            with self.subTest(method=name):
                section = "\n".join(lines[start:end])
                table = re.search(r"\*\*\d+\.2\. 入参\*\*\s*\n(.*?)(?=\*\*\d+\.3\.)", section, re.S)
                self.assertIsNotNone(table)
                fields = [line.split("|")[1].strip().strip("`")
                          for line in table[1].splitlines() if line.startswith("|")][2:]
                declared = {key for key, param in inspect.signature(getattr(panda_data, name)).parameters.items()
                            if param.kind not in (param.VAR_POSITIONAL, param.VAR_KEYWORD)}
                self.assertEqual(set(fields), declared)

    def test_examples_use_declared_keywords(self):
        doc = (ROOT / "references/api-docs.md").read_text(encoding="utf-8")
        for code in re.findall(r"```python\s*\n(.*?)```", doc, re.S):
            for node in ast.walk(ast.parse(code)):
                if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                        and isinstance(node.func.value, ast.Name) and node.func.value.id == "panda_data"):
                    continue
                with self.subTest(method=node.func.attr):
                    sig = inspect.signature(getattr(panda_data, node.func.attr))
                    keywords = {kw.arg for kw in node.keywords if kw.arg}
                    self.assertLessEqual(keywords, set(sig.parameters))
                    sig.bind(*[None for _ in node.args], **{key: None for key in keywords})

    def test_newly_exported_methods_and_aliases_dry_run(self):
        for name in ("get_stock_preferred_detail", "get_stock_equity_nature",
                     "get_stock_competitor", "get_stock_intermediary",
                     "get_stock_related_party", "get_stock_over_allotment",
                     "get_factor_exposure_style"):
            with self.subTest(method=name):
                result = self.run_cli("call_api.py", "--method", name, "--params", "{}", "--dry-run")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(json.loads(result.stdout)["dry_run"])

    def test_dry_run_rejects_obsolete_future_symbol(self):
        result = self.run_cli("call_api.py", "--method", "get_future_daily_post",
                              "--params", '{"symbol":["A"]}', "--dry-run")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Unknown parameter(s): symbol", result.stderr)

    def test_new_method_search(self):
        result = self.run_cli("search_api_docs.py", "--method", "get_us_min")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("frequency", result.stdout)

    def test_index_is_reproducible(self):
        methods = parse_methods(ROOT / "references/api-docs.md")
        self.assertEqual((ROOT / "references/method-index.md").read_text(encoding="utf-8"),
                         render_markdown(methods, "api-docs.md"))


if __name__ == "__main__":
    unittest.main()
