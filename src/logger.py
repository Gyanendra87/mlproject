import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)
LOG_FILE = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    filemode='w'
)
if __name__ == "__main__":
    logging.info("Logging setup complete.")
    print(f"Logs will be saved to {LOG_FILE}")  