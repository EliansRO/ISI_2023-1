from .entities.Pensions import Pension
import os
import re

class ModelPensions():

    @classmethod
    def create_pension(self, db, pension):
        try:
            cursor = db.connection.cursor()

            # Guardar la foto en el directorio "static/photos"
            photo_filename = secure_filename(pension.photo.filename)
            photo_path = os.path.join("static/photos", photo_filename)
            pension.photo.save(photo_path)

            sql = "INSERT INTO pensions (photo, name, description, price, availability, owner_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (photo_path, pension.name, pension.description, pension.price, pension.availability, pension.owner_id)
            cursor.execute(sql, values)
            self.db.commit()
            return cursor.lastrowid
        except Exception as e:
            print("Error in create_pension:", e)
            self.db.rollback()
            raise
    
    @classmethod
    def get_pensionsByUserid(self, db, user_id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT photo, name, description, price, availability, owner_id FROM pensions WHERE owner_id=%s"
            values = (user_id,)
            cursor.execute(sql, values)
            results = cursor.fetchall()

            pensions = []

            for result in results:
                pension = Pension(*result)
                pensions.append(pension)
            
            return pensions
        except Exception as e:
            print("Error in get_pensionsByUserid:", e)
            raise

    @classmethod
    def get_pension_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT pensions.photo, pensions.name, pensions.description, pensions.price, pensions.availability, user.name AS owner_name 
                    FROM pensions 
                    INNER JOIN user ON pensions.owner_id = user.id"""

            cursor.execute(sql)
            results = cursor.fetchall()
            
            pensions = []

            for result in results:
                pension = Pension(*result)
                pensions.append(pension)
            
            return pensions
        except Exception as e:
            print("Error in get_pension_all:", e)
            raise


def secure_filename(filename):
    # Eliminar caracteres no permitidos (excepto letras, números, guiones y guiones bajos)
    cleaned_filename = re.sub(r'[^\w.-]', '', filename)
    return cleaned_filename