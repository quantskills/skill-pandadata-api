# 1.0.6 验证记录

- 日期：2026-11-05。
- 发布包：PyPI panda_data 1.0.6，SHA-256 见 sdk-contract.json。
- Python 3.11；21 项离线测试通过，覆盖全部 323 个数据名称、参数表、示例绑定、CLI、索引和消费者检查器。
- 未登录服务，未验证生产数据或 WebSocket 权限；发布清单明确标记 live_service: not_tested。

复跑：`python -m unittest discover -s tests -v`，再运行 `python scripts/check_sdk_contract.py --root .`。

Cursor、Claude Code、Codex、Hermes、OpenClaw 的共享入口、适配器、引用和脚本已一起更新。
