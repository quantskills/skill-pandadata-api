#!/usr/bin/env python3
"""Compatibility facts for the supported panda_data SDK release."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version


SDK_DISTRIBUTION = "panda-data"
SDK_VERSION = "0.0.12"

# Legacy headings found in the supplied gateway document. SDK 0.0.12 exports
# only the canonical names on the right-hand side.
LEGACY_METHOD_ALIASES = {
    "get_option_exercise_data": "get_option_exercise",
    "get_option_spot_market_data": "get_option_spot_market",
    "get_stock_competitor": "get_stock_competitor_information",
    "get_stock_intermediary": "get_stock_intermediary_information",
    "get_stock_over_allotment": "get_stock_status_over_allotment",
    "get_stock_related_party": "get_stock_rela_party_trans",
}

# These interfaces exist in the bundled gateway documentation but are not
# exported as top-level panda_data methods by SDK 0.0.12.
DOCUMENTED_ONLY_METHODS = frozenset(
    {
        "get_cumu_guarantee",
        "get_investor_brief_detail",
        "get_investor_brief_qa",
        "get_stock_csrc_approval",
        "get_stock_disclosure_date",
        "get_stock_equity_illegal",
        "get_stock_equity_nature",
        "get_stock_equity_placard",
        "get_stock_issuer_credit_rating",
        "get_stock_litigation_arbitration",
        "get_stock_material_contract",
        "get_stock_preferred_detail",
        "get_stock_preferred_dividend",
        "get_stock_preferred_placement",
        "get_stock_preferred_rating",
        "get_stock_preferred_shares",
        "get_stock_preferred_trading",
    }
)


def installed_sdk_version() -> str:
    try:
        return version(SDK_DISTRIBUTION)
    except PackageNotFoundError as exc:
        raise RuntimeError(
            "panda_data is not installed. Run `python scripts/setup_runtime.py` first."
        ) from exc


def require_sdk_version() -> str:
    installed = installed_sdk_version()
    if installed != SDK_VERSION:
        raise RuntimeError(
            f"Unsupported panda_data version {installed}; this skill requires {SDK_VERSION}. "
            "Run `python scripts/setup_runtime.py` to install the pinned SDK."
        )
    return installed
