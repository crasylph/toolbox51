import unittest

# import logging
# LOG_FORMAT = "%(levelname) -5s %(asctime)s" "-1d: %(message)s"
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# logging.basicConfig(format=LOG_FORMAT)



from toolbox51 import ContextTimer
# from toolbox51 import touch_logger, DEBUG
# logger = touch_logger("GLOBAL", level=DEBUG)

class LoggerTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_context_timer(self):
        with ContextTimer("test_timer", log_mode="print", time_mode="seconds"):
            a = 0
            for i in range(1000000):
                a += 1