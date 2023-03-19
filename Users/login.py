from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin



app = Flask(__name__)
app.secret_key = "clave_secreta_para_flask"

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Clase de usuario que implementa UserMixin de Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Función que retorna un usuario por ID
def get_user(id):
    return User(id)

# Función que simula la autenticación de usuario
def authenticate(username, password):
    if username == "admin" and password == "admin":
        return User(username)
    else:
        return None

# Vista para la página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate(username, password)
        if user is not None:
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Usuario o contraseña inválidos')
    else:
        return render_template('login.html')

# Vista para la página de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Vista para la página de inicio (requiere login)
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Función que carga un usuario por ID (necesaria para Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)



if __name__ == '__main__':
    app.run(debug=True)

