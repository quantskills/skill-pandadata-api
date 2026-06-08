#!/usr/bin/env python3
"""Set up the Pandadata runtime SDK and optional credential env file."""

from __future__ import annotations

import argparse
import getpass
import os
import shlex
import stat
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE_URL = "http://pandadata.pandaaiquant.com"
DEFAULT_ENV_FILE = Path.home() / ".pandadata" / "pandadata.env"


def run_pip_install() -> None:
    requirements = ROOT / "requirements.txt"
    cmd = [sys.executable, "-m", "pip", "install", "-r", str(requirements)]
    print("[setup] Installing runtime requirements...")
    subprocess.run(cmd, check=True)


def prompt_text(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def prompt_secret(label: str, existing: str = "") -> str:
    suffix = " [press Enter to use existing env value]" if existing else ""
    value = getpass.getpass(f"{label}{suffix}: ")
    return value or existing


def resolve_credentials(args: argparse.Namespace) -> tuple[str, str, str]:
    env_username = os.getenv("DEFAULT_USERNAME", "")
    env_password = os.getenv("DEFAULT_PASSWORD", "")
    env_base_url = os.getenv("JAVA_SERVICE_BASE_URL", DEFAULT_BASE_URL)

    username = args.username or env_username
    password = args.password or env_password
    base_url = args.base_url or env_base_url

    if not args.non_interactive:
        username = prompt_text("Pandadata username", username)
        password = prompt_secret("Pandadata password", password)
        base_url = prompt_text("Pandadata base URL", base_url or DEFAULT_BASE_URL)

    return username, password, base_url


def shell_export_line(key: str, value: str) -> str:
    return f"export {key}={shlex.quote(value)}"


def write_env_file(path: Path, username: str, password: str, base_url: str) -> None:
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    content = "\n".join(
        [
            "# Pandadata runtime credentials. Keep this file private.",
            shell_export_line("DEFAULT_USERNAME", username),
            shell_export_line("DEFAULT_PASSWORD", password),
            shell_export_line("JAVA_SERVICE_BASE_URL", base_url),
            "",
        ]
    )
    path.write_text(content, encoding="utf-8")
    path.chmod(stat.S_IRUSR | stat.S_IWUSR)
    print(f"[setup] Wrote env file: {path}")
    print(f"[setup] Load it in a shell with: source {shlex.quote(str(path))}")


def ask_yes_no(prompt: str, default: bool = True) -> bool:
    suffix = " [Y/n]" if default else " [y/N]"
    raw = input(prompt + suffix + ": ").strip().lower()
    if not raw:
        return default
    return raw in {"y", "yes"}


def validate_import() -> None:
    import panda_data  # noqa: PLC0415

    print(f"[setup] panda_data import OK: {panda_data.__file__}")
    for name in ("init_token", "get_stock_daily", "get_trade_cal"):
        if not hasattr(panda_data, name):
            raise RuntimeError(f"panda_data is missing expected method: {name}")


def validate_login(username: str, password: str, base_url: str, probe_api: bool) -> None:
    import panda_data  # noqa: PLC0415

    print("[setup] Checking Pandadata login with panda_data.init_token()...")
    panda_data.init_token(username=username, password=password, base_url=base_url)
    print("[setup] Login OK.")

    if probe_api:
        print("[setup] Probing API with get_last_trade_date(exchange='SH')...")
        result = panda_data.get_last_trade_date(exchange="SH")
        print(f"[setup] API probe OK: {result}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", help="Pandadata username. Defaults to DEFAULT_USERNAME.")
    parser.add_argument("--password", help="Pandadata password. Defaults to DEFAULT_PASSWORD.")
    parser.add_argument(
        "--base-url",
        help=f"Pandadata base URL. Defaults to JAVA_SERVICE_BASE_URL or {DEFAULT_BASE_URL}.",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=DEFAULT_ENV_FILE,
        help=f"Credential env file to write when saving credentials. Default: {DEFAULT_ENV_FILE}",
    )
    parser.add_argument("--save-env", action="store_true", help="Save credentials to --env-file without prompting.")
    parser.add_argument("--no-save-env", action="store_true", help="Do not save credentials to --env-file.")
    parser.add_argument("--no-install", action="store_true", help="Skip pip install -r requirements.txt.")
    parser.add_argument("--skip-login-check", action="store_true", help="Skip panda_data.init_token() validation.")
    parser.add_argument("--probe-api", action="store_true", help="After login, call get_last_trade_date as a live API probe.")
    parser.add_argument("--non-interactive", action="store_true", help="Never prompt; require credentials via args or env.")
    args = parser.parse_args()

    if args.save_env and args.no_save_env:
        print("Choose only one of --save-env or --no-save-env.", file=sys.stderr)
        return 2

    if not args.no_install:
        run_pip_install()

    username, password, base_url = resolve_credentials(args)
    if not args.skip_login_check and (not username or not password or not base_url):
        print(
            "Missing username/password/base_url. Provide args, env vars, or run interactively.",
            file=sys.stderr,
        )
        return 2

    validate_import()

    if not args.skip_login_check:
        try:
            validate_login(username, password, base_url, args.probe_api)
        except Exception as exc:
            print(f"[setup] Login check failed: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 1
    else:
        print("[setup] Login check skipped.")

    should_save = args.save_env
    if not args.save_env and not args.no_save_env and not args.non_interactive:
        should_save = ask_yes_no(
            f"Save credentials to {args.env_file}? This stores the password in a local chmod 600 file",
            default=True,
        )

    if should_save:
        if not username or not password or not base_url:
            print("Cannot save env file without username/password/base_url.", file=sys.stderr)
            return 2
        write_env_file(args.env_file, username, password, base_url)
    else:
        print("[setup] Credentials were not saved.")

    print("[setup] Pandadata runtime setup complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
