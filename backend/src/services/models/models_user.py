import datetime
from pymongo import MongoClient

class User:
    def __init__(self, username, email, roles=None, permissions=None):
        self.username = username
        self.email = email
        self.password = None  # La contraseña debe ser establecida a través de un método seguro
        self.roles = roles if roles is not None else ["user"]
        self.permissions = permissions if permissions is not None else {}
        self.session_count = 0
        self.status = "active"
        self.last_login = None
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def set_password(self, password_hash):
        """Establece el hash de la contraseña del usuario."""
        self.password = password_hash

    def check_permission(self, permission):
        """Verifica si el usuario tiene un permiso específico."""
        return self.permissions.get(permission, False)

    def login(self):
        """Registra el inicio de sesión del usuario."""
        self.session_count += 1
        self.last_login = datetime.datetime.utcnow()
    
    def save(self, db):
        """Guarda el usuario en la base de datos."""
        user_data = self.__dict__
        db.users.insert_one(user_data)