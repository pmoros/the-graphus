"""
Set up database logger.
"""

import logging

formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logger.addHandler(stream_handler)
