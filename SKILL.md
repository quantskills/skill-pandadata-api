---
name: pandadata-api
description: Pandadata/panda_data Python SDK API reference skill for selecting, calling,
  and troubleshooting Pandadata data interfaces from the bundled Chinese 接口文档. Use
  when the user asks to query Pandadata data, choose the right panda_data.get_* method,
  write or validate panda_data Python examples, inspect request/response fields, or
  install/load/use this skill in Claude Code, Codex, Hermes, OpenClaw, Cursor, or
  WorkBuddy agents.
license: GPL-3.0-only
metadata:
  organization: QuantSkills
  organization_url: https://github.com/quantskills
  repository: skill-pandadata-api
  repository_url: https://github.com/quantskills/skill-pandadata-api
  project_type: skill
  collection: pandadata-api
quantSkills:
  project_type: skill
  category: data-api
  tags:
  - pandadata
  - panda-data
  - market-data
  - python-sdk
  - api-reference
  platforms:
  - claude-code
  - codex
  - openclaw
  - cursor
  status: stable
  validation_level: runnable
  maintainer_type: official
  summary_zh: 把自然语言数据需求，精准路由到正确的 pandadata API，并生成可直接运行的 Python 调用。
  summary_en: Pandadata and panda_data Python SDK reference skill for selecting, calling,
    and troubleshooting quant data APIs.
  license: GPL-3.0
---

# Pandadata API

Use this skill to route natural-language data requests to the correct `panda_data` API method, load the exact parameter/field contract from the bundled Pandadata interface document, and write runnable Python calls.

## Workflow

1. Identify the data domain: trading calendar, A-share, futures, options, factors, Hong Kong/US equities, or macro.
2. Open `references/method-index.md` first, or run `./.venv/bin/python scripts/search_api_docs.py --list-methods` when `.venv` exists.
3. Load the exact method section before coding:

```bash
PYTHON_BIN="${PANDADATA_PYTHON:-./.venv/bin/python}"
[ -x "$PYTHON_BIN" ] || PYTHON_BIN=python3

"$PYTHON_BIN" scripts/search_api_docs.py --method get_stock_daily
"$PYTHON_BIN" scripts/search_api_docs.py 股票 分红 --context-lines 4
```

4. Use the documented method signature and examples from `references/api-docs.md`. Do not invent parameters, field names, symbols, or authentication steps.
5. For real API calls, prefer `scripts/call_api.py`; it loads saved credentials, runs setup when credentials are missing, initializes `panda_data` in the same process, then calls the API.

## Calling Pattern

Use `import panda_data`; Pandadata calls return DataFrame-like tabular results in the examples.

Install the runtime SDK when real API calls are required:

```bash
PYTHON_BIN="${PANDADATA_PYTHON:-./.venv/bin/python}"
[ -x "$PYTHON_BIN" ] || PYTHON_BIN=python3
"$PYTHON_BIN" -m pip install -r requirements.txt
```

For first-time setup, prefer the interactive setup script. It installs the SDK, prompts for credentials without echoing the password, validates login, and can optionally save a shell env file at `~/.pandadata/pandadata.env`.

```bash
PYTHON_BIN="${PANDADATA_PYTHON:-./.venv/bin/python}"
[ -x "$PYTHON_BIN" ] || PYTHON_BIN=python3
"$PYTHON_BIN" scripts/setup_runtime.py
```

Initialize the SDK before any `get_*` call. The installed SDK raises `ClientNotInitializedError` until `init_token()` succeeds.

```python
import panda_data

panda_data.init_token(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url="http://pandadata.pandaaiquant.com",
)
```

The SDK can also read `DEFAULT_USERNAME`, `DEFAULT_PASSWORD`, and `JAVA_SERVICE_BASE_URL` from environment variables. Pass the plain password; the SDK hashes it internally.

If credentials were saved by `scripts/setup_runtime.py`, load them before running data scripts:

```bash
source ~/.pandadata/pandadata.env
```

Preferred CLI runner for agents:

```bash
PYTHON_BIN="${PANDADATA_PYTHON:-./.venv/bin/python}"
[ -x "$PYTHON_BIN" ] || PYTHON_BIN=python3
"$PYTHON_BIN" scripts/call_api.py \
  --method get_stock_daily \
  --params '{"symbol":["000001.SZ"],"start_date":"20250101","end_date":"20250131","fields":[],"indicator":"000300","st":true}'
```

`call_api.py` behavior:

- Load credentials from current env or `~/.pandadata/pandadata.env`.
- If credentials are missing, run `scripts/setup_runtime.py` interactively.
- Call `panda_data.init_token()` in the same Python process.
- Invoke the requested `panda_data.get_*` method and emit JSON by default.

For custom Python scripts, import the runtime helper so the login check happens in the same process as the API call:

```python
from pathlib import Path
import sys

sys.path.append(str(Path("scripts").resolve()))
from pandadata_runtime import init_pandadata

panda_data = init_pandadata()
result = panda_data.get_stock_daily(
    symbol=["000001.SZ"],
    start_date="20250101",
    end_date="20250131",
    fields=[],
)
print(result)
```

```python
import panda_data

result = panda_data.get_stock_daily(
    symbol=["000001.SZ"],
    start_date="20250101",
    end_date="20250131",
    fields=[],
    indicator="000300",
    st=True,
)
print(result)
```

Before running real calls in a new environment:

```bash
python - <<'PY'
import panda_data
print("panda_data import ok", getattr(panda_data, "__version__", "unknown"))
PY
```

If `panda_data` is unavailable or credentials are missing, report that the SDK/runtime is not configured. The supplied interface document does not define installation, token, or login setup.

Known PyPI runtime dependencies from `panda_data==0.0.9`: `pandas>=2.0.0`, `numpy>=1.22,<2.0`, `python-snappy>=0.7.3`, `python-dotenv>=1.0.0`, `PyYAML>=6.0`, `zstandard>=0.22.0`, `duckdb`, and `pyarrow`.

## Core Conventions

- Dates in the document use `YYYYMMDD` strings, for example `20250131`.
- A-share symbols use suffix format such as `000001.SZ` or `600000.SH`.
- Exchange codes documented for calendars include `SH`, `HK`, and `US`.
- Many APIs accept `fields=[]` for all fields, but some tables describe `fields` as `string`; follow the exact method example when present.
- Some APIs accept list inputs such as `symbol=["000001.SZ"]`; others show scalar strings such as `symbol="000001.SZ"`. Match the target method's own example.
- For broad/unfiltered calls, warn the user when the API may return a large table.

## Reference Files

- `references/method-index.md`: compact method map grouped by domain, with line numbers into `api-docs.md`.
- `references/api_catalog.json`: method-to-service endpoint mapping for API routing checks.
- `references/api-docs.md`: full Pandadata interface document copied from `接口文档.md`.
- `references/agent-integration.md`: installation, loading, and smoke-test patterns for Claude Code, Codex, Hermes, OpenClaw, Cursor, and WorkBuddy.

## Agent Usage Rules

- Prefer the bundled reference over memory. Search before answering API-specific questions.
- Quote method names and parameters exactly as documented.
- Keep examples minimal and executable; use `head()`, `shape`, or explicit row counts when validating.
- Separate data retrieval from analysis: first obtain/verify the DataFrame, then transform or analyze it.
- If a method returns empty data, check date range, symbol format, and required filters before assuming service failure.
