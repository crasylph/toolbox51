import unittest

# import logging
# LOG_FORMAT = "%(levelname) -5s %(asctime)s" "-1d: %(message)s"
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# logging.basicConfig(format=LOG_FORMAT)



from toolbox51.common.logger_manager import logger
logger.use_relative_path_off()
# from toolbox51 import touch_logger, DEBUG
# logger = touch_logger("GLOBAL", level=DEBUG)

class LoggerTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_logger_stacklevel(self):
        def test_func():
            logger.debug("debug message", stacklevel=2)
            logger.info("info message", stacklevel=2)
            logger.warning("warning message", stacklevel=2)
            logger.error("error message", stacklevel=2)
            logger.critical("critical message", stacklevel=2)
            
        test_func()
    
    def test_default_logger(self):
        """默认logger测试"""
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")
        
    def test_async_logger(self):
        """异步logger测试"""
        
        async def async_test():
            logger.debug("debug message")
            logger.info("info message")
            logger.warning("warning message")
            logger.error("error message")
            logger.critical("critical message")
            
        import asyncio
        asyncio.run(async_test())
        
    # def test_logger_release(self):
    #     """release模式下logger测试"""
    #     logger = touch_logger("GLOBAL", level=DEBUG, debug=False)
    #     logger.debug("debug message")
    #     logger.info("info message")
    #     logger.warning("warning message")
    #     logger.error("error message")
    #     logger.critical("critical message")