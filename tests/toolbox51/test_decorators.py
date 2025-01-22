import unittest

# import logging
# LOG_FORMAT = "%(levelname) -5s %(asctime)s" "-1d: %(message)s"
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# logging.basicConfig(format=LOG_FORMAT)



from toolbox51 import logger, func_logger
# from toolbox51 import touch_logger, DEBUG
# logger = touch_logger("GLOBAL", level=DEBUG)

class LoggerTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_func_logger(self):
        
        @func_logger
        def this_func(x, y):
            """test"""
            print(x+y)
            # raise ValueError("test")
            
        print(this_func)
        this_func(1,2)