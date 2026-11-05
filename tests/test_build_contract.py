import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build_sdk_contract import describe_method


class ContractGenerationTests(unittest.TestCase):
    def test_authentication_defaults_are_never_published(self):
        def login(username='private-user',password='private-password',base_url='https://private.invalid',country='CN'):
            return None
        result=describe_method('init_token',login)
        serialized=json.dumps(result)
        self.assertNotIn('private-user',serialized)
        self.assertNotIn('private-password',serialized)
        self.assertNotIn('private.invalid',serialized)
        self.assertEqual(result['parameters'],['username','password','base_url','country'])

    def test_signature_and_runtime_validation_are_distinct(self):
        def getter(start_date='',end_date='',fields=None,**kwargs):
            validate_not_empty(start_date,'start_date')
            validate_not_empty(end_date,'end_date')
        result=describe_method('get_example',getter)
        self.assertEqual(result['required'],[])
        self.assertEqual(result['runtime_required'],['end_date','start_date'])
        self.assertNotIn('kwargs',result['parameters'])

    def test_required_python_arguments_are_preserved(self):
        def getter(symbol,fields=None):
            return None
        self.assertEqual(describe_method('get_example',getter)['required'],['symbol'])


if __name__=='__main__':unittest.main()
