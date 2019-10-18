import os
import random
import string
import sys

from flask import *
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)

from user_login import LoginForm, User

app = Flask(__name__)


# Index Page
@app.route('/')
def index():
    return render_template('index.html')


# region Error handler for 404,500
@app.errorhandler(500)
def page_error(error):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
# endregion


# region User Login
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = request.form.get('username', None)
        password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        next = request.args.get('next')
        user = User(user_name)
        if user.verify_password(password):
            login_user(user, remember=remember_me)
            return redirect(next or "/")
        else:
            flash('Invalid user name or password')
    return render_template('login.html', form=form)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/registerhandler', methods=['GET', 'POST'])
def registerhandle():
    form = LoginForm()
    data = request.form
    user_name = data['username']
    password = data['password']
    email = data['email']
    reg_ip = request.remote_addr
    user = User()
    reg = user.register(user_name, password, email, reg_ip)
    if(reg):
        return render_template('login.html', data='0', form=form)
    else:
        username_suffix = ''.join(random.sample(
            string.ascii_letters + string.digits, 4))
        flash(
            f'user name exists, suggest user name {user_name}{username_suffix}')
        return render_template('register.html', data='0')
# endregion

@app.route('/bstabledemo')
def bstabledemo():
    return render_template('bs_table_demo.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)
