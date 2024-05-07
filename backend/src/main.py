from datetime import datetime
import colorama
from colorama import Fore, Back, Style
from services.questions import Questions, ExitCommand
from services.validator import Validator
from services.logger import Logger
from dotenv import load_dotenv
import os
from database.mongoDB import DatabaseClient

def setup():
    """Configura el entorno inicial cargando variables y bibliotecas necesarias."""
    load_dotenv()  # Cargar variables de entorno desde .env
    colorama.init()  # Inicializar colorama para manejo correcto de colores en la terminal
    return {
        'database_url': os.getenv('DATABASE_URL'),  # Extraer y retornar configuraciones
        'secret_key': os.getenv('SECRET_KEY')
    }

def main():
    config = setup()  # Obtener configuraciones del setup
    print(f"URL de la base de datos: {config['database_url']}")
    print(f"Clave secreta: {config['secret_key']}")

    db_client = DatabaseClient()
    validator = Validator()
    questions = Questions(validator)
    logger = Logger()
    logger.log_info("Init application")

    collection = db_client.get_collection('test_users')
    if collection is not None:
        print("Conectado a la colección test_users correctamente.")
        for document in collection.find():
            print(document)
    else:
        print("No se pudo obtener la colección.")

    try:
        name = questions.ask("¿Cuál es tu nombre?")
        print(f"Hola, {name}! Bienvenido.")

        color = questions.select_option("Elige un color favorito", ["rojo", "verde", "azul"])
        print(f"Has seleccionado el color {color}.")

        file = questions.select_file("selecciona un fichero txt ", "txt")
        print(f"Has seleccionado el fichero {file}.")

        folder = questions.select_folder("seleciona un directorio ")
        print(f"Has seleccionado el directorio {folder}.")

        files = questions.select_files("seleciona un directorio con ficheros tif ", "tif")
        print(f"Has seleccionado el directorio {files}.")

    except ExitCommand:
        logger.log_info("Exit application")
        print("You have chosen to exit the application.")
    except Exception as e:
        logger.log_info(f"Se ha producido un error: {e}")
        print(f"An error has occurred: {e}")
    finally:
        db_client.close_connection()

if __name__ == "__main__":
    main()
