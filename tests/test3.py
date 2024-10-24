import logging
import uuid

# 自定义日志格式，包括uuid字段
fmt = "%(asctime)s%(msecs)d | %(levelname)s | %(pathname)s | %(funcName)s | %(uuid)s - %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=fmt, datefmt=datefmt)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def log_with_uuid(logger, level, msg, uuid_value, *args, **kwargs):
    extra = {'uuid': uuid_value}  # 通过extra传递uuid
    logger.log(level, msg, *args, extra=extra, stacklevel=2, **kwargs)  # stacklevel=2 指向调用方

# 测试函数
def my_function():
    uuid_value = uuid.uuid4()  # 生成UUID
    log_with_uuid(logger, logging.INFO, "This is a log message", uuid_value)

my_function()
