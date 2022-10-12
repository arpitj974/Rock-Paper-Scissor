import logging
import config
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("game_logger")
handler = RotatingFileHandler(filename=config.log_file_name,
                              maxBytes=config.log_file_max_bytes,
                              backupCount=config.log_file_backup_count)

formatter = logging.Formatter(config.log_file_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

# setting log level
if config.log_level.lower() == "debug":
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
