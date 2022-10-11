import logging
from logging.handlers import RotatingFileHandler
import constants

logger = logging.getLogger("game_logger")
handler = RotatingFileHandler(filename=constants.log_file_name,
                              maxBytes=constants.log_file_max_bytes,
                              backupCount=constants.log_file_backup_count)
formatter = logging.Formatter(constants.log_file_format)
handler.setFormatter(formatter)
logger.addHandler(handler)
if constants.log_level.lower() =="debug":
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)


