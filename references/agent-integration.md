# Pandadata Skill Agent Integration

Use this file when installing, loading, or smoke-testing `pandadata-api` across agent runtimes. Keep the whole skill folder together; do not copy only `SKILL.md`, because the skill depends on `references/` and `scripts/`.

Set the source path once:

```bash
export PANDADATA_SKILL_ROOT="/Volumes/aicom/pandaai/dataapi/pandadata-api"
```

If the target machine cannot access that path, copy the entire `pandadata-api/` directory first.

## Universal Smoke Test

Run from inside the skill folder:

```bash
cd "$PANDADATA_SKILL_ROOT"
PYTHON_BIN="${PANDADATA_PYTHON:-./.venv/bin/python}"
[ -x "$PYTHON_BIN" ] || PYTHON_BIN=python3
"$PYTHON_BIN" scripts/setup_runtime.py
"$PYTHON_BIN" scripts/search_api_docs.py --method get_stock_daily | sed -n '1,60p'
"$PYTHON_BIN" scripts/search_api_docs.py --list-methods | wc -l
```

Expected result: `get_stock_daily` prints its parameter table and the method count is `185`.

Runtime API calls require SDK login:

```bash
cd "$PANDADATA_SKILL_ROOT"
PYTHON_BIN="${PANDADATA_PYTHON:-./.venv/bin/python}"
[ -x "$PYTHON_BIN" ] || PYTHON_BIN=python3
"$PYTHON_BIN" scripts/setup_runtime.py
```

The setup script installs `panda_data`, asks for username/password with hidden password input, calls `panda_data.init_token()`, and optionally writes a private env file:

```bash
source ~/.pandadata/pandadata.env
```

Manual equivalent:

```bash
export DEFAULT_USERNAME="..."
export DEFAULT_PASSWORD="..."
export JAVA_SERVICE_BASE_URL="http://pandadata.pandaaiquant.com"
```

```python
import panda_data
panda_data.init_token()  # reads DEFAULT_USERNAME / DEFAULT_PASSWORD / JAVA_SERVICE_BASE_URL
```

Or pass credentials explicitly:

```python
panda_data.init_token(
    username="...",
    password="...",
    base_url="http://pandadata.pandaaiquant.com",
)
```

Agent prompt smoke test:

```text
Use $pandadata-api to find the Pandadata method for A-share daily bars of 000001.SZ from 20250101 to 20250131. Return a minimal Python example, but do not call the API.
```

Expected agent behavior: load `SKILL.md`, consult `references/method-index.md` or `scripts/search_api_docs.py`, choose `panda_data.get_stock_daily`, and preserve the documented date/symbol/fields conventions.

Credential-aware API runner:

```bash
cd "$PANDADATA_SKILL_ROOT"
PYTHON_BIN="${PANDADATA_PYTHON:-./.venv/bin/python}"
[ -x "$PYTHON_BIN" ] || PYTHON_BIN=python3
"$PYTHON_BIN" scripts/call_api.py \
  --method get_stock_daily \
  --params '{"symbol":["000001.SZ"],"start_date":"20250101","end_date":"20250131","fields":[]}'
```

`call_api.py` first checks the current environment and `~/.pandadata/pandadata.env`. If credentials are missing, it runs `scripts/setup_runtime.py` and asks for username/password. If credentials exist, it calls `panda_data.init_token()` and then the requested data API.

## Claude Code

Claude Code skills are folders containing `SKILL.md`; personal skills live under `~/.claude/skills/`, and project skills under `.claude/skills/`.

Install:

```bash
mkdir -p ~/.claude/skills
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ ~/.claude/skills/pandadata-api/

# or project-local
mkdir -p .claude/skills
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ .claude/skills/pandadata-api/
```

Load:

```text
Restart Claude Code, then ask: "List all available Skills."
```

Use:

```text
Use $pandadata-api to write a panda_data call for Hong Kong daily data.
```

## Codex

Codex-compatible installs use the same `SKILL.md` package shape. Prefer `$CODEX_HOME/skills`; if `CODEX_HOME` is unset, use `~/.codex/skills`.

Install:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ "${CODEX_HOME:-$HOME/.codex}/skills/pandadata-api/"
```

For workspaces or runners that also scan `.agents/skills`, install a project copy:

```bash
mkdir -p .agents/skills
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ .agents/skills/pandadata-api/
```

Load:

```text
Restart the Codex session or refresh the skill registry, then ask it to list available skills.
```

Use:

```text
Use $pandadata-api to select the right panda_data API for macro economic calendar data and show the documented parameters.
```

## Hermes

Hermes discovers local skills from `~/.hermes/skills/<category>/<skill-name>/`.
The `hermes skills install` command is registry/URL oriented; for this local
workspace skill, install by copying the full folder into Hermes' local skills
tree.

Install:

```bash
mkdir -p ~/.hermes/skills/finance/pandadata-api
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ ~/.hermes/skills/finance/pandadata-api/
hermes skills list
```

Load/use:

```bash
hermes chat --toolsets skills,terminal -q \
  "Use the pandadata-api skill to find the API for A-share dividend data. Return the method name and a minimal Python example."
```

If terminal tools are disabled, import `SKILL.md`, `references/method-index.md`, and `references/api-docs.md` into Hermes as trusted local context, then use the same prompt.

## OpenClaw

OpenClaw uses `SKILL.md` directories and scans common roots such as workspace skill folders and user-level OpenClaw skill folders. Prefer a real directory copy instead of a symlink: OpenClaw may skip symlinks that resolve outside the configured scan root.

Install:

```bash
mkdir -p ~/.openclaw/skills
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ ~/.openclaw/skills/pandadata-api/

# workspace-local alternatives
mkdir -p skills .agents/skills
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ skills/pandadata-api/
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ .agents/skills/pandadata-api/
```

If migrating from Codex:

```bash
openclaw migrate plan codex
openclaw migrate codex
```

Load/use:

```bash
openclaw skills list
openclaw -p "Use $pandadata-api to find the Pandadata API for futures dominant contract data."
```

## Cursor

Cursor project rules live in `.cursor/rules` as `.mdc` files. Cursor rules are the adapter layer; the full skill remains in `pandadata-api/`.

Install into a project:

```bash
mkdir -p .cursor/skills .cursor/rules
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ .cursor/skills/pandadata-api/
cp "$PANDADATA_SKILL_ROOT/agents/cursor-rule.mdc" .cursor/rules/pandadata-api.mdc
```

Load:

```text
Reload the Cursor window. The rule is agent-requested and should attach when the user asks about Pandadata, panda_data, or Pandadata API docs.
```

Use:

```text
Use the Pandadata API skill to write a panda_data.get_hk_daily example for Hong Kong daily data. Verify the symbol format from the docs first.
```

## WorkBuddy

WorkBuddy is commonly deployed on top of Claude Code and a persistent knowledge/workflow store. Prefer installing through Claude Code first, then register the universal loader prompt as a reusable workflow/note.

Install:

```bash
mkdir -p ~/.claude/skills
rsync -a --exclude '__pycache__' "$PANDADATA_SKILL_ROOT"/ ~/.claude/skills/pandadata-api/
```

Optional knowledge/workflow adapter:

```bash
cp "$PANDADATA_SKILL_ROOT/agents/portable-loader.md" ./PANDADATA_API_SKILL_LOADER.md
```

Load/use:

```text
In WorkBuddy, attach PANDADATA_API_SKILL_LOADER.md or paste its contents into the workflow. Ask: "Use pandadata-api to choose the correct API for option implied volatility."
```

## Maintenance

When `接口文档.md` changes:

```bash
cp /Volumes/aicom/pandaai/dataapi/接口文档.md "$PANDADATA_SKILL_ROOT/references/api-docs.md"
cd "$PANDADATA_SKILL_ROOT"
python scripts/build_method_index.py > references/method-index.md
python scripts/search_api_docs.py --list-methods | wc -l
```

Re-run the universal smoke test after every document refresh.
