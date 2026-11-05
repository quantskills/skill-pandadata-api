#!/usr/bin/env python3
"""Compatibility facts for the supported panda_data SDK release."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version


SDK_DISTRIBUTION = "panda-data"
SDK_VERSION = "1.0.6"

# Legacy headings found in the supplied gateway document.
LEGACY_METHOD_ALIASES = {
    "get_option_exercise_data": "get_option_exercise",
    "get_option_spot_market_data": "get_option_spot_market",
    "get_stock_competitor": "get_stock_competitor_information",
    "get_stock_intermediary": "get_stock_intermediary_information",
    "get_stock_over_allotment": "get_stock_status_over_allotment",
    "get_stock_related_party": "get_stock_rela_party_trans",
}

# SDK 1.0.6 also exports four former document aliases; the two option aliases
# above remain documentation-only spellings.
SDK_EXPORTED_ALIASES = frozenset(
    {
        "get_stock_competitor",
        "get_stock_intermediary",
        "get_stock_over_allotment",
        "get_stock_related_party",
    }
)

# All 218 original gateway interfaces are now exported. Export availability
# does not establish that the configured server supports a method.
DOCUMENTED_ONLY_METHODS: frozenset[str] = frozenset()


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
