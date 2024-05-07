from models.User import User
from database.mongoDB import DatabaseClient

class UserManager:
    def __init__(self, db):
        self.db = db

    def save_user(self, user):
        """Guarda o actualiza el usuario en la base de datos."""
        user_data = vars(user)
        if self.db.users.find_one({"username": user.username}):
            self.db.users.update_one({"username": user.username}, {"$set": user_data})
        else:
            self.db.users.insert_one(user_data)

    def deactivate_user(self, username):
        """Desactiva un usuario."""
        self.db.users.update_one({"username": username}, {"$set": {"status": "inactive"}})

    def find_user(self, username):
        """Encuentra un usuario por su nombre de usuario."""
        return self.db.users.find_one({"username": username})
