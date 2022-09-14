from flask import Flask
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)

##########################################################
# SECRET_KEY:
# cmd  ---> python ---> import secrets ----> secrets.token_hex(16) will return key
##########################################################
app.config['SECRET_KEY'] = '9283f36dde6a58de39738c1637ab9ade'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes