#!/usr/bin/env python3
"""Credential-aware Pandadata SDK initialization helpers."""

from __future__ import annotations

import os
import platform
import shlex
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE_URL = "http://pandadata.pandaaiquant.com"
DEFAULT_ENV_FILE = Path.home() / ".pandadata" / "pandadata.env"


class PandadataRuntimeError(RuntimeError):
    """Raised when the Pandadata runtime cannot be initialized."""


def _parse_env_assignment(line: str) -> tuple[str, str] | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None

    try:
        parts = shlex.split(stripped, posix=True)
    except ValueError:
        return None

    if not parts:
        return None
    if parts[0] == "export":
        parts = parts[1:]
    if not parts or "=" not in parts[0]:
        return None

    key, value = parts[0].split("=", 1)
    key = key.strip()
    if not key:
        return None
    return key, value


def load_env_file(path: Path = DEFAULT_ENV_FILE, override: bool = False) -> bool:
    """Load shell-style KEY=value or export KEY=value lines into os.environ."""

    if not path.exists():
        return False

    for line in path.read_text(encoding="utf-8").splitlines():
        parsed = _parse_env_assignment(line)
        if not parsed:
            continue
        key, value = parsed
        if override or key not in os.environ:
            os.environ[key] = value
    return True


def credentials_from_env() -> tuple[str, str, str]:
    username = os.getenv("DEFAULT_USERNAME", "")
    password = os.getenv("DEFAULT_PASSWORD", "")
    base_url = os.getenv("JAVA_SERVICE_BASE_URL", DEFAULT_BASE_URL)
    return username, password, base_url


def has_credentials() -> bool:
    username, password, base_url = credentials_from_env()
    return bool(username and password and base_url)


def setup_command(
    env_file: Path = DEFAULT_ENV_FILE,
    install: bool = False,
    probe_api: bool = False,
) -> list[str]:
    cmd = [sys.executable, str(ROOT / "scripts" / "setup_runtime.py"), "--env-file", str(env_file)]
    if not install:
        cmd.append("--no-install")
    if probe_api:
        cmd.append("--probe-api")
    return cmd


def run_setup(
    env_file: Path = DEFAULT_ENV_FILE,
    install: bool = False,
    probe_api: bool = False,
) -> None:
    """Run the interactive setup script."""

    subprocess.run(setup_command(env_file=env_file, install=install, probe_api=probe_api), check=True)


def open_setup_terminal(
    env_file: Path = DEFAULT_ENV_FILE,
    install: bool = False,
    probe_api: bool = False,
    dry_run: bool = False,
) -> str:
    """Open a user-facing terminal window for interactive credential setup."""

    cmd = setup_command(env_file=env_file, install=install, probe_api=probe_api)
    shell_cmd = " ".join(shlex.quote(part) for part in cmd)
    shell_cmd = (
        f"cd {shlex.quote(str(ROOT))} && {shell_cmd}; "
        "printf '\\nPandadata setup finished. You can close this terminal.\\n'; "
        "read -r -p 'Press Enter to close...'"
    )

    if dry_run:
        return shell_cmd

    if platform.system() == "Darwin":
        escaped = shell_cmd.replace("\\", "\\\\").replace('"', '\\"')
        apple_script = (
            'tell application "Terminal"\n'
            "  activate\n"
            f'  do script "{escaped}"\n'
            "end tell"
        )
        subprocess.run(["osascript", "-e", apple_script], check=True)
        return shell_cmd

    raise PandadataRuntimeError(
        "Opening a setup terminal is currently implemented for macOS Terminal only. "
        f"Run this command manually instead: {shell_cmd}"
    )


def setup_terminal_message(command: str) -> str:
    return (
        "Pandadata credentials are missing or invalid. Opened an interactive setup "
        "terminal for the user. After setup finishes, rerun the API call. "
        f"Setup command: {command}"
    )


def init_pandadata(
    *,
    env_file: Path = DEFAULT_ENV_FILE,
    setup_if_missing: bool = True,
    retry_setup_on_login_error: bool = True,
    install: bool = False,
):
    """Return the initialized panda_data module.

    The panda_data SDK keeps login state in the current Python process, so this
    function must be called inside the same process that will call get_* APIs.
    """

    try:
        import panda_data  # noqa: PLC0415
    except ModuleNotFoundError as exc:
        if not install:
            raise PandadataRuntimeError(
                "panda_data is not installed. Run `python scripts/setup_runtime.py` first."
            ) from exc
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")],
            check=True,
        )
        import panda_data  # noqa: PLC0415

    load_env_file(env_file)

    if not has_credentials():
        if not setup_if_missing:
            raise PandadataRuntimeError(
                "Missing DEFAULT_USERNAME / DEFAULT_PASSWORD / JAVA_SERVICE_BASE_URL. "
                "Run `python scripts/setup_runtime.py` or source ~/.pandadata/pandadata.env."
            )
        try:
            run_setup(env_file=env_file, install=install)
        except subprocess.CalledProcessError as exc:
            raise PandadataRuntimeError(
                "Pandadata setup did not complete. Check username/password/base_url, "
                "then rerun `python scripts/setup_runtime.py`."
            ) from exc
        load_env_file(env_file, override=True)

    username, password, base_url = credentials_from_env()
    if not username or not password or not base_url:
        raise PandadataRuntimeError("Pandadata credentials are still missing after setup.")

    try:
        panda_data.init_token(username=username, password=password, base_url=base_url)
    except Exception:
        if not (setup_if_missing and retry_setup_on_login_error):
            raise
        print(
            "[runtime] Existing Pandadata credentials failed; running setup_runtime.py again.",
            file=sys.stderr,
        )
        try:
            run_setup(env_file=env_file, install=False)
        except subprocess.CalledProcessError as exc:
            raise PandadataRuntimeError(
                "Pandadata setup did not complete after credential refresh."
            ) from exc
        load_env_file(env_file, override=True)
        username, password, base_url = credentials_from_env()
        panda_data.init_token(username=username, password=password, base_url=base_url)

    return panda_data


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Check and initialize Pandadata credentials.")
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--no-setup", action="store_true", help="Fail instead of prompting when credentials are missing.")
    parser.add_argument("--install", action="store_true", help="Install requirements if panda_data is missing.")
    args = parser.parse_args()

    try:
        init_pandadata(
            env_file=args.env_file,
            setup_if_missing=not args.no_setup,
            install=args.install,
        )
    except Exception as exc:
        print(f"[runtime] ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    print("[runtime] Pandadata SDK initialized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
