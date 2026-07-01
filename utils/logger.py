import logging
import os

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, "automation.log"),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    force=True      # <-- Important
)

logger = logging.getLogger(__name__)