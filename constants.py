from enum import Enum, auto

log_file_name = "game.log"
log_file_max_bytes = 2000
log_file_backup_count = 5
log_file_format = "%(asctime)s | %(name)s | %(levelname)s : %(message)s"
log_level="info"


class Action(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
