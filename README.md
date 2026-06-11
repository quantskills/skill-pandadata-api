# 🐼 Pandadata API Skill

**简体中文** | [English](README.en.md)

> 把自然语言数据需求，精准路由到正确的 `panda_data` API，并生成可直接运行的 Python 调用。

<p align="center">
  <img alt="methods" src="https://img.shields.io/badge/API_methods-185-brightgreen">
  <img alt="domains" src="https://img.shields.io/badge/data_domains-7-blue">
  <img alt="sdk" src="https://img.shields.io/badge/panda__data-0.0.9-orange">
  <img alt="python" src="https://img.shields.io/badge/python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="agents" src="https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%2B4-7c3aed">
  <img alt="license" src="https://img.shields.io/badge/license-GPLv3-blue">
</p>

---

## 📖 这是什么

`pandadata-api` 是一个 **Agent Skill**（技能包）——它把 Pandadata / `panda_data` Python SDK 的中文接口文档（185 个数据接口）打包成 AI Agent 可以查询、引用、校验的本地知识库。

当你向 Agent（Claude Code、Codex、Cursor 等）提出诸如 *"帮我查 000001.SZ 的 A 股日线"* 这类需求时，这个技能会：

1. 🧭 **路由** —— 在 7 大数据域中定位到正确的接口
2. 📑 **加载契约** —— 从接口文档中读取**精确的**参数名 / 字段名 / 示例，而不是凭记忆瞎编
3. ✍️ **生成代码** —— 写出符合文档约定的、可运行的 `panda_data` 调用
4. 🚀 **真实调用**（可选）—— 自动加载凭证、初始化 SDK、执行接口并返回结果

> 核心原则：**Prefer the bundled reference over memory.** 先查文档，再回答。

---

## 🗂️ 数据域总览

```mermaid
mindmap
  root((panda_data<br/>185 methods))
    交易工具
      交易日历
      交易日推算
      在售股票列表
    A股数据
      行情/分钟线
      概念/行业/指数
      龙虎榜/融资融券
      财务/分红/股东
    期货数据
      行情/主力合约
      DeepView 持仓
      基差/库存/套利
    期权数据
      基本信息
      日线行情
      隐含波动率
    量化因子
      回测因子
      复权因子
    港美股
      港股/美股行情
      公司事件
      一致预期/因子
    宏观数据
      中国/国际宏观
      行业/特色数据
      经济日历
```

| 数据域 | 代表接口 | 说明 |
|---|---|---|
| 🛠️ **交易工具** | `get_trade_cal` · `get_last_trade_date` | 交易日历、交易日推算、在售股票 |
| 📈 **A股数据** | `get_stock_daily` · `get_stock_dividend` · `get_fina_reports` | 行情、概念行业、资金、公司行为、财务 |
| 🔩 **期货数据** | `get_future_daily` · `get_future_dominant` · `get_broker_netmarg` | 行情、主力合约、DeepView 持仓席位 |
| ⚖️ **期权数据** | `get_option_daily` · `get_option_implied_volatility` | 期权信息、日线、波动率 |
| 🧮 **量化因子** | `get_factor` · `get_adj_factor` | 回测因子、复权因子 |
| 🌏 **港美股** | `get_hk_daily` · `get_us_daily` | 行情、公司事件、一致预期、财务因子 |
| 🏛️ **宏观数据** | `get_macro_na` · `get_macro_cal` | 中国/国际宏观、行业、特色数据、经济日历 |

完整 185 个接口映射见 [`references/method-index.md`](references/method-index.md)。

---

## ⚡ Agent 工作流

```mermaid
flowchart TD
    A[用户自然语言需求] --> B{识别数据域}
    B --> C[查 method-index.md<br/>或 search_api_docs.py --list-methods]
    C --> D[加载精确接口契约<br/>search_api_docs.py --method get_xxx]
    D --> E[按文档示例生成 Python 调用]
    E --> F{需要真实数据?}
    F -- 否 --> G[输出可运行代码示例]
    F -- 是 --> H[call_api.py 自动登录并调用]
    H --> I[返回 JSON / DataFrame]

    style A fill:#e3f2fd,stroke:#1976d2
    style G fill:#e8f5e9,stroke:#388e3c
    style I fill:#e8f5e9,stroke:#388e3c
    style H fill:#fff3e0,stroke:#f57c00
```

---

## 📦 目录结构

```
pandadata-api/
├── SKILL.md                          # 技能入口：工作流、调用约定、规则
├── requirements.txt                  # panda_data==0.0.9, requests
├── references/
│   ├── method-index.md               # 📇 185 接口速查表（按域分组 + 文档行号）
│   ├── api_catalog.json              # 🧭 方法到后端服务 endpoint 的映射
│   ├── api-docs.md                   # 📚 完整中文接口文档
│   └── agent-integration.md          # 🔌 各 Agent 安装/加载/冒烟测试
├── scripts/
│   ├── search_api_docs.py            # 🔍 检索/抽取接口文档
│   ├── call_api.py                   # 📞 凭证感知的接口运行器
│   ├── setup_runtime.py              # 🔐 交互式安装 + 登录 + 保存凭证
│   ├── pandadata_runtime.py          # 同进程初始化 SDK 的运行时助手
│   └── build_method_index.py         # 从 api-docs.md 重建 method-index
└── agents/
    ├── cursor-rule.mdc               # Cursor 规则适配
    ├── openai.yaml                   # OpenAI/Codex 适配
    └── portable-loader.md            # 通用加载器
```

---

## 🚀 快速开始

### 1️⃣ 检索接口（无需凭证，纯文档查询）

```bash
# 列出全部方法（应为 185）
python scripts/search_api_docs.py --list-methods

# 查看某个方法的完整参数 / 字段 / 示例
python scripts/search_api_docs.py --method get_stock_daily

# 关键词检索（多个词需命中同一行）
python scripts/search_api_docs.py 股票 分红 --context-lines 4
```

### 2️⃣ 首次配置运行时（安装 SDK + 登录）

```bash
python scripts/setup_runtime.py
```

该脚本会：安装 `panda_data` → 隐藏输入用户名/密码 → 校验登录 → 可选保存凭证到 `~/.pandadata/pandadata.env`。

### 3️⃣ 真实调用接口

```bash
python scripts/call_api.py \
  --method get_stock_daily \
  --params '{"symbol":["000001.SZ"],"start_date":"20250101","end_date":"20250131","fields":[]}'
```

`call_api.py` 会自动：读取当前环境或 `~/.pandadata/pandadata.env` 的凭证 → 缺失则触发交互式 `setup_runtime.py` → 同进程 `init_token()` → 执行接口 → 默认输出 JSON。

### 4️⃣ 在自定义 Python 中使用

```python
from pathlib import Path
import sys

sys.path.append(str(Path("scripts").resolve()))
from pandadata_runtime import init_pandadata

panda_data = init_pandadata()                       # 同进程完成登录校验
result = panda_data.get_stock_daily(
    symbol=["000001.SZ"],
    start_date="20250101",
    end_date="20250131",
    fields=[],
)
print(result)
```

---

## 🔌 多 Agent 安装

技能为 `SKILL.md` 包结构，**必须保留整个目录**（依赖 `references/` 与 `scripts/`），不要只拷贝 `SKILL.md`。

```bash
# 先固定源路径
export PANDADATA_SKILL_ROOT="/path/to/pandadata-api"
```

| Agent | 安装位置 | 用法示例 |
|---|---|---|
| **Claude Code** | `~/.claude/skills/` 或项目 `.claude/skills/` | `Use $pandadata-api to ...` |
| **Codex** | `$CODEX_HOME/skills`（默认 `~/.codex/skills`） | `Use $pandadata-api to ...` |
| **Hermes** | `~/.hermes/skills/finance/pandadata-api/` | `hermes chat --toolsets skills,terminal` |
| **OpenClaw** | `~/.openclaw/skills/`（用真实目录，避免符号链接） | `openclaw -p "Use $pandadata-api ..."` |
| **Cursor** | `.cursor/skills/` + 规则 `.cursor/rules/pandadata-api.mdc` | 重载窗口后自动按需附加 |
| **WorkBuddy** | 经 Claude Code 安装 + `portable-loader.md` | 附加加载器后调用 |

各 Agent 的完整安装命令与冒烟测试见 [`references/agent-integration.md`](references/agent-integration.md)。

### ✅ 通用冒烟测试

```bash
cd "$PANDADATA_SKILL_ROOT"
python scripts/search_api_docs.py --method get_stock_daily | head -60
python scripts/search_api_docs.py --list-methods | wc -l
```

**预期结果**：`get_stock_daily` 打印其参数表，且方法计数为 **185**。

---

## 📐 核心约定

| 约定 | 示例 | 说明 |
|---|---|---|
| 📅 日期格式 | `20250131` | 统一 `YYYYMMDD` 字符串 |
| 🏷️ A 股代码 | `000001.SZ` · `600000.SH` | 带交易所后缀 |
| 🌐 交易所代码 | `SH` · `HK` · `US` | 用于日历类接口 |
| 📋 全字段 | `fields=[]` | 多数接口返回全字段；部分接口 `fields` 为 `string`，**以方法示例为准** |
| 🔢 入参类型 | `symbol=["000001.SZ"]` vs `symbol="000001.SZ"` | 列表 / 标量因接口而异，**严格匹配目标方法示例** |

> ⚠️ 对于宽口径 / 无过滤的调用，需提醒用户接口可能返回大表。

---

## 🤖 Agent 使用规则

- **先查再答**：API 相关问题先检索文档，不要凭记忆。
- **精确引用**：方法名、参数名严格按文档书写，不发明参数 / 字段 / 代码 / 鉴权步骤。
- **示例最小可执行**：用 `head()`、`shape` 或显式行数做校验。
- **取数与分析分离**：先获取并验证 DataFrame，再做转换 / 分析。
- **空数据先自查**：返回空时先核对日期范围、代码格式、必填过滤，再判定服务异常。

---

## 🔄 文档维护

当上游 `接口文档.md` 更新时：

```bash
cp /path/to/接口文档.md references/api-docs.md
python scripts/build_method_index.py > references/method-index.md
python scripts/search_api_docs.py --list-methods | wc -l   # 复核方法计数
```

并重新执行通用冒烟测试。

---

## 🔐 凭证与依赖

- SDK 在 `init_token()` 成功前会抛出 `ClientNotInitializedError`。
- 可通过环境变量提供凭证：`DEFAULT_USERNAME` / `DEFAULT_PASSWORD` / `JAVA_SERVICE_BASE_URL`。传入**明文密码**，SDK 内部自行哈希。
- `panda_data==0.0.9` 运行时依赖：`pandas>=2.0.0`、`numpy>=1.22,<2.0`、`python-snappy>=0.7.3`、`python-dotenv>=1.0.0`、`PyYAML>=6.0`、`zstandard>=0.22.0`、`duckdb`、`pyarrow`。

> 凭证文件（`*.env`、`user.json`、`.pandadata/`）已在 `.gitignore` 中忽略，不会提交。

---

## 📜 License

This project is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE).
