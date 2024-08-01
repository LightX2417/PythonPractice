# Create a logger that logs messages of different levels (INFO, ERROR, WARNING) to different files. Use info.log for INFO level and error.log for ERROR and WARNING levels.

import logging

# Create handlers
info_handler = logging.FileHandler("info.log")
error_handler = logging.FileHandler("error.log")

# Set level for handlers
info_handler.setLevel(logging.INFO)
error_handler.setLevel(logging.WARNING)

# Create formatters and add to handlers
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Create a logger and add handlers
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(info_handler)
logger.addHandler(error_handler)

# Log some messages
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
