import unittest

from toolbox51.logger import logger

class EnumTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_result_enum(self):
        from toolbox51.const.result import ResultEnum
        self.assertEqual(ResultEnum.SUCCESS.value, "SUCCESS")
        self.assertEqual(ResultEnum.FAILURE.value, "FAILURE")