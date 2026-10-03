import logging
import os
from datetime import datetime
Log_File=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",Log_File)
os.makedirs(logs_path,exist_ok=True)
logging.basicConfig(filename=logs_path, level=logging.INFO)
Log_File_Path=os.path.join(logs_path,Log_File)
logging.basicConfig(filename=Log_File_Path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

