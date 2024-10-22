import unittest

class LoggerTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_default_logger(self):
        """默认logger测试"""
        from toolbox51 import touch_logger, DEBUG
        logger = touch_logger("GLOBAL", level=DEBUG)
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")
        
    def test_logger_release(self):
        """release模式下logger测试"""
        from toolbox51 import touch_logger, DEBUG
        logger = touch_logger("GLOBAL", level=DEBUG, debug=False)
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")