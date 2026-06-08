#!/usr/bin/env python3
"""Call a panda_data.get_* API with automatic credential setup."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from pandadata_runtime import (
    DEFAULT_ENV_FILE,
    PandadataRuntimeError,
    has_credentials,
    init_pandadata,
    load_env_file,
    open_setup_terminal,
    setup_terminal_message,
)


def parse_params(raw: str) -> dict[str, Any]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise argparse.ArgumentTypeError(f"Invalid JSON params: {exc}") from exc
    if not isinstance(value, dict):
        raise argparse.ArgumentTypeError("--params must be a JSON object")
    return value


def dataframe_to_records(result: Any) -> dict[str, Any]:
    if hasattr(result, "to_json") and hasattr(result, "columns"):
        records = json.loads(result.to_json(orient="records", force_ascii=False))
        return {
            "type": "dataframe",
            "rows": int(len(result)),
            "columns": [str(column) for column in result.columns],
            "data": records,
        }

    if hasattr(result, "to_dict"):
        return {"type": type(result).__name__, "data": result.to_dict()}

    return {"type": type(result).__name__, "data": result}


def emit_result(method: str, params: dict[str, Any], result: Any, output: str) -> None:
    if output == "csv":
        if not hasattr(result, "to_csv"):
            raise TypeError(f"Result of {method} does not support CSV output")
        print(result.to_csv(index=False), end="")
        return

    if output == "repr":
        print(result)
        return

    payload = {
        "ok": True,
        "method": method,
        "params": params,
        "result": dataframe_to_records(result),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--method", required=True, help="panda_data method name, e.g. get_stock_daily")
    parser.add_argument("--params", type=parse_params, default={}, help="JSON object of keyword arguments")
    parser.add_argument("--output", choices=["json", "csv", "repr"], default="json")
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--no-setup", action="store_true", help="Fail instead of prompting when credentials are missing.")
    parser.add_argument(
        "--open-setup-terminal",
        action="store_true",
        help="Open macOS Terminal for interactive setup when credentials are missing or invalid.",
    )
    parser.add_argument("--install", action="store_true", help="Install requirements if panda_data is missing.")
    parser.add_argument("--dry-run", action="store_true", help="Validate method/params shape without logging in or calling the API.")
    args = parser.parse_args()

    if not args.method.startswith("get_"):
        print("--method must be a panda_data get_* API method.", file=sys.stderr)
        return 2

    if args.dry_run:
        try:
            import panda_data  # noqa: PLC0415
        except ModuleNotFoundError as exc:
            print(f"panda_data import failed: {exc}", file=sys.stderr)
            return 2
        method_obj = getattr(panda_data, args.method, None)
        if method_obj is None:
            print(f"Method not found: panda_data.{args.method}", file=sys.stderr)
            return 2
        print(
            json.dumps(
                {"ok": True, "dry_run": True, "method": args.method, "params": args.params},
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    setup_if_missing = not args.no_setup and not args.open_setup_terminal

    try:
        if args.open_setup_terminal:
            load_env_file(args.env_file)
            if not has_credentials():
                command = open_setup_terminal(env_file=args.env_file, install=args.install)
                print(f"[call_api] {setup_terminal_message(command)}", file=sys.stderr)
                return 3

        panda_data = init_pandadata(
            env_file=args.env_file,
            setup_if_missing=setup_if_missing,
            retry_setup_on_login_error=setup_if_missing,
            install=args.install,
        )
    except PandadataRuntimeError as exc:
        if args.open_setup_terminal:
            command = open_setup_terminal(env_file=args.env_file, install=args.install)
            print(f"[call_api] {setup_terminal_message(command)}", file=sys.stderr)
            return 3
        print(f"[call_api] Runtime setup failed: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        if args.open_setup_terminal:
            command = open_setup_terminal(env_file=args.env_file, install=args.install)
            print(f"[call_api] {setup_terminal_message(command)}", file=sys.stderr)
            return 3
        print(f"[call_api] Login failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    method_obj = getattr(panda_data, args.method, None)
    if method_obj is None:
        print(f"Method not found: panda_data.{args.method}", file=sys.stderr)
        return 2

    try:
        result = method_obj(**args.params)
        emit_result(args.method, args.params, result, args.output)
    except Exception as exc:
        print(f"[call_api] API call failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
