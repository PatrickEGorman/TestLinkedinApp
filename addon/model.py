from addon import db
from exceptions import InvalidUserAddException, DuplicateUserException


users = db.users


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.access_token = None

    def add_to_db(self):
        if not self.username or not self.password:
            raise InvalidUserAddException
        elif users.find_one({"username":self.username}):
            raise DuplicateUserException
        else:
            users.insert({
                "username": self.username,
                "password": self.password
            })

    def set_access_token(self, access_token):
        self.access_token = access_token

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        user = users.find_one({"username": self.username})
        return user["_id"].__str__()
