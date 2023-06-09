from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, id_card, name, last_name, username, phone, password) -> None:
        self.id = id
        self.id_card = id_card
        self.name = name
        self.last_name = last_name
        self.username = username
        self.phone = phone
        self.password = password

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)