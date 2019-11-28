import hashlib

from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField
from wtforms.validators import DataRequired

from db_connection.mysql_connection import MYSQL_CONN


class User(UserMixin):

    def __init__(self, username=None):
        self.conn = MYSQL_CONN()
        self.username = username
        self.id = self.get_id()

    def md5(self, password):
        m = hashlib.md5()
        m.update(password.encode("utf8"))
        password = m.hexdigest()
        return password

    def get_id(self):
        if self.username is not None:
            sql = "SELECT id FROM user_info WHERE user_name = '{}'".format(
                self.username)
            user_id = self.conn.execute_query(sql)
            if len(user_id) != 0:
                return user_id[0][0]

    def verify_password(self, password):
        password = self.md5(password)
        if self.id is not None:
            sql = "SELECT password FROM user_info WHERE id = '{}'".format(
                self.id)
            user_pwd = self.conn.execute_query(sql)
            if len(user_pwd) != 0:
                if user_pwd[0][0] == password:
                    return True
        return False

    def register(self, user_name, password, email, reg_ip):

        password = self.md5(password)
        sql_get_username = "SELECT user_name FROM user_info"
        usernamelist = self.conn.execute_query(sql_get_username)
        for user in usernamelist:
            if user_name == user[0]:
                return False

        sql = "INSERT INTO user_info (`user_name`,`password`,`email`,`reg_ip`) VALUES ('{}','{}','{}','{}')".format(
            user_name, password, email, reg_ip)
        self.conn.execute_non_query(sql)
        return True

    @staticmethod
    def get(user_id):
        sql = "SELECT * FROM user_info"
        conn = MYSQL_CONN()
        user_profiles = conn.execute_query(sql)
        for id in user_profiles:
            if id[0] == user_id:
                user_name = id[1]
                return User(user_name)


class LoginForm(FlaskForm):

    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)
