# 1.0.6 验证记录

- 日期：2026-11-05。
- 发布包：PyPI panda_data 1.0.6，SHA-256 见 sdk-contract.json。
- Python 3.11；24 项离线测试通过，覆盖全部 323 个数据名称、参数表、示例绑定、CLI、索引和消费者检查器。
- 使用标准保存的配置完成有界线上烟测：A 股日线 1 行；一个股票的因子、一个期货品种的后复权行情在 30 天窗口各返回 20 行。只记录状态/行数，没有发布账号信息或原始数据。
- 该烟测不证明所有接口、账号权限或项目业务流程可用；WebSocket 尚未验证。

复跑：`python -m unittest discover -s tests -v`，再运行 `python scripts/check_sdk_contract.py --root .`。

Cursor、Claude Code、Codex、Hermes、OpenClaw 的共享入口、适配器、引用和脚本已一起更新。
