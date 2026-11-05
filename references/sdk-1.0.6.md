# panda_data 1.0.6 Compatibility

Read this before configuring authentication, selecting an API, or upgrading a runtime.

## Verified release

- SDK: `panda_data==1.0.6`; Python `>=3.10` according to wheel metadata.
- Source: [PyPI 1.0.6](https://pypi.org/project/panda-data/1.0.6/), uploaded 2026-11-04; wheel checked 2026-11-05.
- Wheel: `panda_data-1.0.6-py3-none-any.whl`.
- SHA-256: `5437a54546946ca5dd3a24ec074d05342518f22310f04403e01adb4d034ce15f`.
- Dependencies: `pandas>=2.0.0`, `numpy>=1.22,<2.0`, `python-snappy>=0.7.3`, `python-dotenv>=1.0.0`, `PyYAML>=6.0`, `zstandard>=0.22.0`, `duckdb`, `pyarrow`, `websockets>=13.0`, `requests`.

The PyPI description contains older version, Python, and API examples. Use the published wheel's metadata, exports, signatures, and validation code for this release's contract.

## Authentication

```python
import os
import panda_data

panda_data.init_token(
    username=os.environ["DEFAULT_USERNAME"],
    password=os.environ["DEFAULT_PASSWORD"],
    base_url=os.environ["JAVA_SERVICE_BASE_URL"],
    country="CN",
)
```

The signature is `init_token(username=..., password=..., base_url=..., country="CN")`. Previous `user_endpoint`, `login_path`, and `tick_user` options are no longer accepted. Supply the plaintext password; the SDK hashes it internally. The implementation passes the username through to the server; do not assume SDK phone-number normalization or additional country support.

The SDK strips a trailing `/pandaData/pandaDataTick`, `/pandaDataTick`, or `/pandaData` to find the service root, then logs in at `<root>/pandaData/dataUser/login`. Supply the configured service URL; do not hard-code the default host or assume a WebSocket-only port exposes HTTP login.

The token stays in memory. Successful login persists encrypted credentials and expiry metadata in `user.json`; the SDK can refresh expired authentication. `setup_runtime.py --no-save-env` disables only the skill's separate plaintext shell env file, not SDK persistence.

Unlike 0.0.12, this wheel actually binds top-level `init`, `is_authenticated`, `auth_remaining_seconds`, `auth_expires_at`, `get_token_ttl`, `auth_info`, and `clear_auth`. Do not expose tokens or credentials from authentication state in reports.

## Coverage and changed contracts

All **218** original gateway methods are now exported, including the **17** previously marked `not exported`. The supplement in `api-docs.md` adds **105** other exported data names, bringing the searchable total to **323**. Counts include compatibility names and aliases, and do not count distinct server datasets or newly introduced capabilities.

The other three callable `get_*` exports (`get_client`, `get_factory`, `get_token_ttl`) are SDK/authentication helpers. `api_catalog.json` retains its **218 MCP gateway dispatch paths**; it is not a catalog of every Python SDK export. Do not invent gateway paths for supplemental methods.

| Area | 1.0.6 contract |
|---|---|
| Futures adjusted daily bars | `get_future_daily_post(underlying_symbol=..., start_date=..., end_date=..., method="close_pcs", fields=...)`; `symbol` is not accepted. Methods: `close_pcs`, `close_os`, `close_pcr`, `close_or`. Response `symbol` is the actual contract (e.g. `CF509.CZC`); `dominant_id` is the continuous identifier (e.g. `A_dominant.DCE`). |
| Metadata snapshots | Stock, index, futures, HK, and US `get_*_detail` add optional `date`. HK/US `get_*_detail_all` are separate entrypoints without `date`. |
| Industry data | `get_industry_constituents`, `get_industry_detail`, `get_stock_industry` add `reference` and `date`. References: `sws_2021` (default), `citics_2019`, `gildata`; `sw`, `sws`, `sw2021` normalize to `sws_2021`. |
| HK bars | `get_hk_daily` adds `frequency="1D"`; choices `1D`, `1W`, `1M`. |
| Required dates | `get_lhb_list` and `get_repurchase` now require nonempty dates despite empty-string defaults. Other date/quarter defaults also changed to `""`; defaults do not establish optionality. Use keywords because some positional parameter orders changed. |
| Additional routes | Stock weekly/monthly, adjusted minutes, stock flow, ST/suspension status, CNE style exposure, ETF events/minutes, US adjusted bars/minutes, HK/US indices, daily index weights, and overseas stock lists are searchable in the supplement. |

`get_fina_ex` and `get_fina_statement` retain `interim_type`. `get_fina_reports` still validates nonempty `start_quarter` and `end_quarter`. Follow each method's table for exact dates, symbols, and frequencies.

Four former document names are now actual SDK aliases and work with `call_api.py`:

| Alias | Canonical name |
|---|---|
| `get_stock_competitor` | `get_stock_competitor_information` |
| `get_stock_intermediary` | `get_stock_intermediary_information` |
| `get_stock_over_allotment` | `get_stock_status_over_allotment` |
| `get_stock_related_party` | `get_stock_rela_party_trans` |

`get_option_exercise_data` and `get_option_spot_market_data` remain unexported document spellings. Search resolves them to `get_option_exercise` and `get_option_spot_market`; the runner requires canonical names.

## Upstream limitations

An export does not establish server availability. The wheel labels numerous corporate/preferred-stock, option, fund, and legacy index/market methods “deprecated or not yet online.” Their sections preserve the warning. Confirm account permissions and server support. Existing gateway response examples were not refreshed through live requests.

The supplement records wheel signatures and available docstrings without inventing complete response schemas. Runtime validation takes precedence over conflicting docstrings (e.g. stock-flow dates are required).

`get_oversea_stock_list` returns lists, not a DataFrame: specifying `market="US"` or `"HK"` returns that market's list; omission returns `[US_list, HK_list]`. Minute methods' `time_zone` expects a Python tuple. `call_api.py` does not convert JSON arrays to tuples; use Python directly for that parameter.

## Real-time clients

The wheel exports WebSocket clients separately from the synchronous `get_*` runner and 323-method data index:

| Client | Subscription methods |
|---|---|
| `TickStreamClient` | `subscribe_tick(symbols)`, `unsubscribe_tick(symbols)` |
| `QuoteStreamClient` | `subscribe(symbols)`, `unsubscribe(symbols)` |
| `MinuteBarStreamClient` | inherited `subscribe(symbols)`, `unsubscribe(symbols)` |
| `OrderBookStreamClient` | inherited `subscribe(symbols)`, `unsubscribe(symbols)` |
| `MarketBreadthStreamClient` | `subscribe_markets(markets)`, `unsubscribe_markets(markets)` |

Read the wheel's constructor, async method, and callback contracts before coding; configure the intended `url` and authentication. Do not invent channel URLs, subscription payloads, symbol formats, or message schemas. Live streaming was not tested for this documentation update.

## Reproducible offline validation

From the skill root, select Python 3.10+ (Windows virtual environments use `.venv\Scripts\python.exe`):

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/setup_runtime.py --no-install --skip-login-check --non-interactive --no-save-env
python scripts/call_api.py --method get_stock_preferred_detail --params '{}' --dry-run
python scripts/search_api_docs.py --method get_us_min
```

Tests check version selection, every data export's coverage, parameter tables, Python example binding, CLI acceptance/rejection, lookup, and reproducible index generation. They require no credentials and make no data requests. Dry-run validates names and Python binding only; it does not execute SDK value validation, authenticate, or verify server availability.

Maintainer: `abgyjaguo`. This skill is data-access/research tooling; outputs are not investment advice.

## Migration from 1.0.4

1.0.6 adds 62 exported data names (including compatibility aliases), with no removed exports. Twelve existing futures/broker signatures now default their formerly required arguments to empty strings; runtime nonempty validation still applies. The default service URL is now HTTPS. The machine-readable baseline is `references/sdk-contract.json`; `validation.live_service` explicitly remains `not_tested` until service checks are run in an authorized environment.

Consumer repositories can run `python scripts/check_sdk_contract.py --root <project> --contract references/sdk-contract.json`. The shared `pandadata-compat.yml` reusable workflow provides the same offline check. Dynamic dispatch and response semantics require project tests; static checks do not establish account or server availability.
