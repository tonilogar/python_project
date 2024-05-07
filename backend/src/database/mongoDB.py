from pymongo import MongoClient, errors
import os
from dotenv import load_dotenv

class DatabaseClient:
    def __init__(self):
        load_dotenv()  # Carga las variables de entorno
        self.database_url = os.getenv('DATABASE_URL')
        try:
            self.client = MongoClient(self.database_url, serverSelectionTimeoutMS=5000)  # Tiempo de espera corto para la prueba de conexión
            self.client.admin.command('ping')  # Intenta ping a la base de datos para probar la conexión
            print("The connection to the database is correct.")
        except errors.ServerSelectionTimeoutError as err:
            print("Failed to connect to the database:", err)
            self.client = None  # Establece el cliente a None si la conexión falla

    def get_collection(self, collection_name):
        """Devuelve una colección para realizar operaciones, si la conexión fue exitosa."""
        if self.client:
            return self.client['apps'][collection_name]
        else:
            print("Database connection not established.")
            return None

    def close_connection(self):
        """Cierra la conexión con la base de datos si está abierta."""
        if self.client:
            self.client.close()
            print("Database connection closed.")
        else:
            print("No database connection to close.")
