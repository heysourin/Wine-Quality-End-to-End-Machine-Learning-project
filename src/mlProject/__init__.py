import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)  # Create directory if not exists

logging.basicConfig(

    level=logging.INFO,
    format=logging_str,

    handlers=(
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    )
)

logger = logging.getLogger("mlProject") # It can be imported from other files to log

""""
#? logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

1. saves the current timestamp and current date
2. Then it will save the level name from what particular level you are running the logging file from
3. Then it will give you the module name.
4. Finally it shows the logging message.
"""
