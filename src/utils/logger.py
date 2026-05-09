import logging
import os

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "running_logs.log"),
    level=logging.INFO,
    format="[ %(asctime)s ] %(message)s"
)

logger = logging.getLogger()