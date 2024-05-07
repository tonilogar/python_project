import logging
import os
import sys
from datetime import datetime

class Logger:
    def __init__(self):
        """Inicializa y configura el logger."""
        # Configura el directorio correcto para el archivo de log
        if getattr(sys, 'frozen', False):
            # El programa se está ejecutando como un ejecutable independiente
            application_path = os.path.dirname(sys.executable)
        else:
            # El programa se está ejecutando en un entorno de desarrollo
            application_path = os.path.dirname(__file__)

        # Nombre de archivo de log que incluye un timestamp
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        log_filename = f"log_{timestamp}.log"
        log_path = os.path.join(application_path, log_filename)

        # Configura logging para escribir en un archivo
        logging.basicConfig(filename=log_path, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    
    def log_info(self, message):
        """Registra un mensaje de nivel INFO."""
        logging.info(message)

    def log_error(self, message):
        """Registra un mensaje de nivel ERROR."""
        logging.error(message)
