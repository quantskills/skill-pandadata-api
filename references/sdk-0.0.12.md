# panda_data 0.0.12 Compatibility

Use this reference when installing the SDK, validating runtime behavior, or handling a method whose bundled interface documentation does not match the installed Python package.

## Runtime Contract

- Supported SDK: `panda_data==0.0.12`.
- Supported Python declared by PyPI: `>=3.10`.
- Runtime dependencies: `pandas>=2.0.0`, `numpy>=1.22,<2.0`, `python-snappy>=0.7.3`, `python-dotenv>=1.0.0`, `PyYAML>=6.0`, `zstandard>=0.22.0`, `duckdb`, `pyarrow`, `websockets>=13.0`, and `requests`.
- Keep using `init_token(username=..., password=..., base_url=...)`; SDK 0.0.12 adds optional `user_endpoint`, `login_path`, and `tick_user` parameters without breaking the three-argument pattern.
- Do not assume the SDK's built-in default service URL. Supply `JAVA_SERVICE_BASE_URL` or pass `base_url` explicitly.

## Authentication Changes

SDK 0.0.12 keeps the token in memory, persists encrypted credentials and expiry metadata in `user.json`, and can automatically log in again when the token expires. Calling `init_token()` performs this SDK persistence even when `scripts/setup_runtime.py --no-save-env` is used; that flag only controls the skill's separate plaintext shell env file.

The 0.0.12 wheel lists `is_authenticated`, `auth_remaining_seconds`, `auth_expires_at`, `auth_info`, and `clear_auth` in `panda_data.__all__`, but does not bind them on the top-level module. Do not generate calls such as `panda_data.is_authenticated()` until the upstream package exports them.

## Interface Reconciliation

The bundled document contains 218 gateway interfaces. After reconciling six legacy headings with the names exported by SDK 0.0.12, 201 are directly callable as top-level `panda_data.get_*` methods.

The supplied interface document uses these legacy headings. `search_api_docs.py --method <legacy-name>` resolves them to the canonical section; `call_api.py` requires the canonical SDK name:

| Legacy document name | SDK 0.0.12 name |
|---|---|
| `get_option_exercise_data` | `get_option_exercise` |
| `get_option_spot_market_data` | `get_option_spot_market` |
| `get_stock_competitor` | `get_stock_competitor_information` |
| `get_stock_intermediary` | `get_stock_intermediary_information` |
| `get_stock_over_allotment` | `get_stock_status_over_allotment` |
| `get_stock_related_party` | `get_stock_rela_party_trans` |

Other contract decisions checked against the 0.0.12 wheel:

- `get_lhb_list` and `get_repurchase` keep optional date arguments. `get_restricted_list` requires both dates because its 0.0.12 implementation rejects empty values even though its Python defaults are `None`.
- `get_fina_ex` and `get_fina_statement` retain the 0.0.12 `interim_type` argument, which is absent from the supplied document.
- Eighteen exported methods have optional 0.0.12 parameters absent from the supplied document. Their input tables in `api-docs.md` now include the SDK signature additions: concept date bounds; `market="cn"` on six A-share corporate-action methods; `fields` on eleven futures/macro methods; and `underlying_symbol_cn` on `get_broker_flow_daily`.
- `get_fina_reports` requires `start_quarter` and `end_quarter` in the 0.0.12 implementation; `get_future_contract_rank.rank_type`, `get_future_dominant_corr.symbol`, and `get_macro_cal_config.event_code` are optional.
- Macro date parameters retain the gateway document's conservative required markers even where the Python signature defaults to `None`; provide date bounds to avoid unbounded requests and service-side ambiguity.
- `get_index_detail.status` accepts integer codes, despite the supplied document labeling the input as a string.
- `get_stock_litigation_arbitration.lawsuit_type` is documented as a string code (`CI`, `AD`, `CR`, or `AR`), not an integer. This gateway interface remains one of the documented-only methods below.
- The erroneous option-exercise example that called `get_option_underlying_volatility` was corrected to `get_option_exercise`.

These 17 documented gateway interfaces are not exported by SDK 0.0.12. `search_api_docs.py` marks them as `not exported`; do not generate Python SDK calls for them:

- `get_cumu_guarantee`
- `get_investor_brief_detail`
- `get_investor_brief_qa`
- `get_stock_csrc_approval`
- `get_stock_disclosure_date`
- `get_stock_equity_illegal`
- `get_stock_equity_nature`
- `get_stock_equity_placard`
- `get_stock_issuer_credit_rating`
- `get_stock_litigation_arbitration`
- `get_stock_material_contract`
- `get_stock_preferred_detail`
- `get_stock_preferred_dividend`
- `get_stock_preferred_placement`
- `get_stock_preferred_rating`
- `get_stock_preferred_shares`
- `get_stock_preferred_trading`

SDK 0.0.12 exposes these additional data methods that are not described as standalone sections in the bundled document. Use the signatures below, but do not invent field semantics or response schemas:

```text
get_adj_factor_hk(symbol=None, start_date=None, end_date=None, fields=None, **kwargs)
get_factor_hk(symbol="", start_date="", end_date="", factors=None, **kwargs)
get_future_market_post(symbol=None, start_date=None, end_date=None, fields=None, **kwargs)
get_hk_daily_post(symbol=None, start_date=None, end_date=None, fields=None, **kwargs)
get_hk_daily_pre(symbol=None, start_date=None, end_date=None, fields=None, **kwargs)
get_index_component(stock_symbol=None, index_symbol=None, **kwargs)
get_index_constituent(stock_symbol=None, index_symbol=None, **kwargs)
get_macro_or(symbol=None, start_date=None, end_date=None, fields=None, **kwargs)
```

`get_market_data` and `get_market_min_data` are legacy aliases. `get_client` and `get_factory` are SDK plumbing rather than documented data interfaces.

## Validation Commands

Run without credentials:

```bash
PYTHON_BIN="${PANDADATA_PYTHON:-python3}"
"$PYTHON_BIN" scripts/setup_runtime.py \
  --no-install \
  --skip-login-check \
  --non-interactive \
  --no-save-env
"$PYTHON_BIN" scripts/call_api.py \
  --method get_stock_competitor_information \
  --params '{}' \
  --dry-run
```

Run a live probe only with configured credentials and the intended service URL:

```bash
"${PANDADATA_PYTHON:-python3}" scripts/setup_runtime.py --no-install --probe-api --no-save-env
```

Source: [panda-data 0.0.12 on PyPI](https://pypi.org/project/panda-data/0.0.12/). The compatibility facts above were checked against the published 0.0.12 wheel.
