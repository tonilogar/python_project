from datetime import datetime
from pymongo import MongoClient

class User:
    def __init__(self, username, email, roles=None, extra_permissions=None):
        self.username = username
        self.email = email
        self.password = None  # La contraseña debe ser establecida a través de un método seguro
        self.roles = roles if roles is not None else ["user"]
        self.permissions = self.assign_permissions(roles, extra_permissions)
        self.session_count = 0
        self.status = "active"
        self.last_login = None
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def assign_permissions(self, roles, extra_permissions):
        """Asigna permisos basados en roles con opción a permisos adicionales."""
        role_permissions = {
            'user': {
                'edit_settings': False,
                'view_sensitive_data': False,
                'delete_user': False
            },
            'admin': {
                'edit_settings': True,
                'view_sensitive_data': True,
                'delete_user': True
            }
        }
        permissions = {}
        for role in roles:
            permissions.update(role_permissions.get(role, {}))
        
        if extra_permissions:
            permissions.update(extra_permissions)
        
        return permissions

    def set_password(self, password_hash):
        """Establece el hash de la contraseña del usuario."""
        self.password = password_hash

    def check_permission(self, permission):
        """Verifica si el usuario tiene un permiso específico."""
        return self.permissions.get(permission, False)

    def login(self):
        """Registra el inicio de sesión del usuario."""
        self.session_count += 1
        self.last_login = datetime.utcnow()
    
    def save(self, db):
        """Guarda el usuario en la base de datos."""
        user_data = {k: v for k, v in self.__dict__.items() if v is not None}
        db.users.insert_one(user_data)
