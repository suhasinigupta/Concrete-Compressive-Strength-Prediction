import logging
import os
from ConcreteStrength.constant import *


LOG_DIR="concrete_logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_NAME=f"logs_{CURRENT_TIME_STAMP}.log"
FILENAME=os.path.join(ROOT_DIR,LOG_DIR,LOG_NAME)


logging.basicConfig(filename=FILENAME,
                     filemode="wb"
                     level=logging.INFO
                     format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s")