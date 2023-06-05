from .entities.User import User
from werkzeug.security import generate_password_hash

class ModelUser():

    @classmethod
    def login(self, db, user):

        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, id_card, name, last_name, username, phone, password FROM user 
                      WHERE username= '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],row[2],row[3],row[4],row[5],User.check_password(row[6],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, id_card, name, last_name, username, phone FROM user 
                      WHERE id= '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],row[2],row[3],row[4],row[5],None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_cards(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username FROM user 
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
    def add_user(cls, db, id_card, name, last_name, username, phone, password):
        try:
            hashed_password = generate_password_hash(password)
            cursor = db.connection.cursor()
            sql = "INSERT INTO user (id_card, name, last_name, username, phone, password) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (id_card, name, last_name, username, phone, hashed_password))
            db.connection.commit()
            user_id = cursor.lastrowid
            return User(user_id, id_card, name, last_name, username, phone, hashed_password)
        except Exception as ex:
            raise Exception(ex)