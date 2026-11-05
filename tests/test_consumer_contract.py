import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_sdk_contract import inspect_python, inspect_versions, scope

CONTRACT = {
    "get_stock_daily": {"parameters": ["symbol", "start_date", "end_date", "fields"], "required": [], "runtime_required": ["start_date", "end_date"]},
    "get_future_daily_post": {"parameters": ["underlying_symbol", "start_date", "end_date", "method", "fields"], "required": [], "runtime_required": ["start_date", "end_date"]},
    "init_token": {"parameters": ["username", "password", "base_url", "country"], "required": [], "runtime_required": []},
}


class AuditTests(unittest.TestCase):
    def test_module_alias(self):
        x = inspect_python('import panda_data as pd\npd.get_stock_daily(symbol=["000001.SZ"], start_date="20260101", end_date="20260102")', CONTRACT)
        self.assertEqual(x["calls"][0]["method"], "get_stock_daily")
        self.assertFalse(x["issues"])

    def test_pandas_is_not_sdk(self):
        x = inspect_python('import pandas as pd\npd.get_stock_daily()', CONTRACT)
        self.assertFalse(x["calls"])

    def test_from_import(self):
        x = inspect_python('from panda_data import get_future_daily_post as fetch\nfetch(symbol=["A"], start_date="20260101", end_date="20260102")', CONTRACT)
        self.assertEqual(x["issues"][0]["rule"], "unknown_keyword")

    def test_wrapper_alias(self):
        x = inspect_python('sdk = init_pandadata()\nsdk.get_missing()', CONTRACT)
        self.assertEqual(x["issues"][0]["rule"], "unexported_method")

    def test_dynamic_kwargs_are_not_missing(self):
        x = inspect_python('import panda_data\npanda_data.get_stock_daily(**params)', CONTRACT)
        self.assertFalse(x["issues"])
        self.assertTrue(x["calls"][0]["dynamic"])

    def test_old_login_options(self):
        x = inspect_python('import panda_data\npanda_data.init_token(username=u,password=p,base_url=b,tick_user=True)', CONTRACT)
        self.assertEqual(x["issues"][0]["detail"], "init_token: tick_user")

    def test_runtime_required_dates(self):
        x = inspect_python('import panda_data\npanda_data.get_stock_daily(symbol=["000001.SZ"])', CONTRACT)
        self.assertEqual(x["issues"][0]["rule"], "missing_runtime_parameter")

    def test_requirement_not_numpy(self):
        x = inspect_versions('pandas==2.2.0\npanda_data>=0.0.12\n', "requirements.txt")
        self.assertEqual([v["constraint"] for v in x], [">=0.0.12"])

    def test_helper_version_is_runtime_pin(self):
        x = inspect_versions('SDK_VERSION = "0.0.12"\n', "scripts/sdk_compat.py")
        self.assertEqual(x[0]["constraint"], "==0.0.12")

    def test_versioned_library_is_embedded(self):
        self.assertEqual(scope("assets/library-v2/quantskills/versions/skill-demo/abc/source/requirements.txt"), "embedded")

    def test_no_trailing_comma_in_version(self):
        self.assertEqual(inspect_versions('"panda_data>=0.0.9, pandas"', "skill.yml")[0]["constraint"], ">=0.0.9")

    def test_desktop_compatibility_matrix(self):
        text = "export const PANDA_SDK_COMPATIBILITY = [{version: '0.0.12'}, {version: '0.0.14'}]"
        self.assertEqual([v["constraint"] for v in inspect_versions(text, "src/compatibility.ts")], ["==0.0.12", "==0.0.14"])

    def test_python_expected_version_guard(self):
        text = 'EXPECTED = "0.1.0"\ninstalled = version("panda_data")'
        self.assertEqual(inspect_versions(text, "scripts/check_runtime.py")[0]["constraint"], "==0.1.0")


if __name__ == "__main__":
    unittest.main()
