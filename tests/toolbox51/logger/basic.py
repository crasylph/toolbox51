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
        from toolbox51.logger import logger
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")
        
    def test_logger_relative(self):
        """logger_relative测试"""
        from toolbox51.logger import logger_relative as logger
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")