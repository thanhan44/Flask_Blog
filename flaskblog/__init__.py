from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

##########################################################
# SECRET_KEY:
# cmd  ---> python ---> import secrets ----> secrets.token_hex(16) will return key
##########################################################
app.config['SECRET_KEY'] = '9283f36dde6a58de39738c1637ab9ade'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
# if not login and accept to account, default go login page
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes