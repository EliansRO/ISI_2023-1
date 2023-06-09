from flask import Flask, render_template, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from config import config

# Models
from Models.ModelUser import ModelUser
from Models.ModelPensions import ModelPensions

# Entities
from Models.entities.User import User


app = Flask(__name__)

app.config.from_object(config['development'])
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index')) 


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['FirstName']
        last_name = request.form['LastName']
        username = request.form['username']
        password = request.form['password']
        id_card = request.form['id_card']
        phone = request.form['phone']

        try:
            useradd = ModelUser.add_user(db, id_card, name, last_name, username, phone, password)
            flash('Usuario registrado exitosamente', 'success')
            return redirect(url_for('login'))
        except Exception as ex:
            flash('Error al registrar el usuario', 'error')
            return redirect(url_for('auth/register.html'))
    return render_template('auth/register.html')


@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_user(user_id):
    if request.method == 'GET':
        print("GET")
        return render_template('update_user.html')
    if request.method == 'POST':
        print("POST")
        name = request.form['FirstName']
        last_name = request.form['LastName']
        username = request.form['username']
        phone = request.form['phone']

        try:
            user = User(user_id,0,name,last_name,username,phone,0)
            update_user_validate = ModelUser.update(db,user)

            if update_user_validate == True:
                print("GOOD")
                flash("Update complete...")
                return redirect(url_for('index'))
            else:
                print("ERROR")
                flash("Update fail...", 'error')
                return redirect(url_for('index'))
        except Exception as ex:
            print("ERROR")
            flash("Update fail...", 'error')
            return redirect(url_for('index'))
    else:
        return render_template('update_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0,0,0,0,request.form['username'],0,request.form['password'])
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('index'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')   

# Ruta de inicio
@app.route('/')
def index():
    if current_user.is_authenticated:
        cards = ModelPensions.get_pension_all(db)
        return render_template('index.html', cards=cards)
    else:
        cards = ModelPensions.get_pension_all(db)
        return render_template('index.html', cards=cards)

def status_401(error):
    return redirect(url_for('/'))

def status_404(error):
    return redirect(url_for('/'))

if __name__ == '__main__':                                  
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True)