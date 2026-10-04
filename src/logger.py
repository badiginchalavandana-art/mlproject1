import logging
import os
from datetime import datetime
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE_NAME)
os.makedirs(logs_path,exist_ok=True)
log_file_path=os.path.join(logs_path,LOG_FILE_NAME)
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
)