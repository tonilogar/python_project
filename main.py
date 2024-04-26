from datetime import datetime
import colorama
from colorama import Fore, Back, Style
from src.classes.questions import Questions, ExitCommand
from src.classes.validator import Validator
from src.classes.logger import Logger

# Inicializar colorama para que los códigos de colores funcionen correctamente en todas las plataformas
colorama.init()

def main():
    #print(Fore.RED + "Este es un texto en rojo")
    #print(Style.BRIGHT + Fore.GREEN + "Este es un texto en verde y negrita" + Style.RESET_ALL)
    #print(Style.BRIGHT + Back.RED + Fore.WHITE + 'Texto blanco en negrita con fondo rojo' + Style.RESET_ALL)
    validator = Validator()  # Crear una instancia de Validator
    questions = Questions(validator)  # Crear una instancia de Questions
    
    logger = Logger()
    logger.log_info("Init application")
    
    try:
        response = questions.ask('Hola, buenos días. Indica tu nombre por favor:')
        print(f"Nombre recibido: {response}")
        # Continuar con más interacciones aquí
    except ExitCommand:
        print("Has decidido salir de la aplicación. Hasta pronto!")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
