from .entities.User import User
from werkzeug.security import generate_password_hash

class ModelUser():

    @classmethod
    def login(self, db, user):

        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password FORM user 
                      WHERE username= '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username FORM user 
                      WHERE id= '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_cards(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username FORM user 
                      WHERE id= '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_user(cls, db, username, password):
        try:
            hashed_password = generate_password_hash(password)
            cursor = db.connection.cursor()
            sql = "INSERT INTO user(username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, hashed_password))
            db.connection.commit()
            user_id = cursor.lastrowid
            return User(user_id, username, hashed_password)
        except Exception as ex:
            raise Exception(ex)