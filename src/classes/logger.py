import logging
from datetime import datetime

class Logger:
    def __init__(self):
        """Inicializa y configura el logger."""
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        log_filename = f"log_{timestamp}.log"
        
        logging.basicConfig(filename=log_filename, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    
    def log_info(self, message):
        logging.info(message)

    def log_error(self, message):
        logging.error(message)
