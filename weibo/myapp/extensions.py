from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_bootstrap import Bootstrap


db=SQLAlchemy()
moment=Moment()
bootstrap=Bootstrap()

login_manager=LoginManager()
login_manager.login_view='auth.login'
login_manager.login_message='you need to log in to access'


@login_manager.user_loader
def loader_user(id):
    from model import  User
    return User.query.get(id)
