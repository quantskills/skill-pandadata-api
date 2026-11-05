# 1.0.4 离线验收记录

- 验证日期：2026-11-05。
- 输入：PyPI 发布的 `panda_data-1.0.4-py3-none-any.whl`，SHA-256 见 [版本契约](sdk-1.0.4.md)。
- 环境：Windows、Python 3.11，技能目录 `.venv`，依赖按 `requirements.txt` 安装。
- 结果：8 项回归测试通过；运行时安装检查通过，无需凭证。未进行登录、生产数据请求或 WebSocket 订阅。

## 复跑

在技能根目录运行（其他平台选择对应 Python 3.10+ 解释器）：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe scripts/setup_runtime.py --no-install --skip-login-check --non-interactive --no-save-env
```

测试覆盖：

| 检查 | 断言 |
|---|---|
| SDK 版本 | 运行时接受 1.0.4 |
| 导出覆盖 | 261 个数据名称全部有独立可搜索章节；原有 218 个接口均已导出 |
| 入参契约 | 每个章节的参数表与实际 SDK 声明的参数集合一致 |
| Python 示例 | 示例语法、导出方法、关键字和调用绑定有效；不执行示例 |
| CLI 正向检查 | 原先未导出的接口、4 个股票别名及风格因子入口均通过 dry-run |
| CLI 反向检查 | `get_future_daily_post(symbol=...)` 被拒绝，提示未知参数 |
| 文档检索 | 新收录的 `get_us_min` 可检索并返回频率参数 |
| 索引生成 | `build_method_index.py` 的输出与已提交索引一致 |

## 运行时包兼容性

Cursor 使用 `agents/cursor-rule.mdc`；Codex 使用 `SKILL.md` 与 `agents/openai.yaml`；Claude Code、Hermes、OpenClaw 使用完整 `SKILL.md` 技能目录与共享引用，必要时使用 `agents/portable-loader.md`。安装路径见 [集成说明](agent-integration.md)。

五种运行时所需入口、共享文档、脚本和支持文件均保留。验证范围为包结构、文件一致性和 Python 命令，不代表已在五种客户端分别启动会话或验证线上数据权限。
