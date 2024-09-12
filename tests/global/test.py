from toolbox51.string_formatters import timestamp_formatter
from toolbox51.logger import touch_logger, INFO, DEBUG
logger = touch_logger("GLOBAL", level=DEBUG)

ts_msg = timestamp_formatter(12345.0)

logger.info(ts_msg("111111111111111"))