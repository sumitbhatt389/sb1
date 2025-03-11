import logging
from logging.handlers import RotatingFileHandler

log_handler= RotatingFileHandler("app.log", maxBytes=5*1024*1024, backupCount=3)

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app;log"),
              log_handler,
              logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
