from datetime import datetime
import colorama
from colorama import Fore, Back, Style
from services.questions import Questions, ExitCommand
from services.validator import Validator
from services.logger import Logger
from dotenv import load_dotenv
import os
from database.mongoDB import DatabaseClient

# Inicializar colorama para que los códigos de colores funcionen correctamente en todas las plataformas
colorama.init()

def main():
    # Cargar las variables de entorno desde .env
    load_dotenv()
    
    # Usar las variables de entorno
    database_url = os.getenv('DATABASE_URL')
    secret_key = os.getenv('SECRET_KEY')
    
    print("URL de la base de datos:", database_url)
    print("Clave secreta:", secret_key)
    # Inicia el cliente de base de datos, que intentará conectarse automáticamente
    db_client = DatabaseClient()

    # Obtiene la colección, asegurándote de que la conexión fue exitosa antes de continuar
    collection = db_client.get_collection('test_users')
    if collection is not None:
        print("Conectado a la colección test_users correctamente.")
        # Iterar sobre todos los documentos en la colección y imprimir cada uno
        for document in collection.find():
            print(document)  # Imprime el documento. Ajusta esto si necesitas un formato específico.
    else:
        print("No se pudo obtener la colección.")
    #print(Fore.RED + "Este es un texto en rojo")
    #print(Style.BRIGHT + Fore.GREEN + "Este es un texto en verde y negrita" + Style.RESET_ALL)
    #print(Style.BRIGHT + Back.RED + Fore.WHITE + 'Texto blanco en negrita con fondo rojo' + Style.RESET_ALL)
    validator = Validator()  # Crear una instancia de Validator
    questions = Questions(validator)  # Crear una instancia de Questions
    
    logger = Logger()
    logger.log_info("Init application")
    
    try:
        # Probar el método ask para preguntar algo simple
        name = questions.ask("¿Cuál es tu nombre?")
        print(f"Hola, {name}! Bienvenido.")

        # Probar el método select_option para elegir entre varias opciones
        color = questions.select_option("Elige un color favorito", ["rojo: ", "verde: ", "azul: "])
        print(f"Has seleccionado el color {color}.")

        file = questions.select_file("seleciona un fichero txt ", "txt")
        print(f"Has seleccionado el fichero {file}.")
        
        folder = questions.select_folder("seleciona un directorio ")
        print(f"Has seleccionado el directorio {folder}.")
        
        files = questions.select_files("seleciona un directorio con ficheros tif ", "tif")
        print(f"Has seleccionado el directorio {files}.")
        

    except ExitCommand:
        logger.log_info("Exit application")
        print("You have chosen to exit the application.")
        # Cierra la conexión de manera segura al final
        db_client.close_connection()
    except Exception as e:
        logger.log_info(f"Se ha producido un error: {e}")
        print(f"An error has occurred: {e}")
        # Cierra la conexión de manera segura al final
        db_client.close_connection()


if __name__ == "__main__":
    main()
