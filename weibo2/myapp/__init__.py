from flask import  Flask

from  .config import myconfig
from .model import User,Post,PostLike,Comment
from .extensions import db,login_manager,moment,cache,celery,mail
from myapp.blueprints  import blog_bp,auth_bp



import  os

def create_app(config_name=None):
    if config_name is None:
        config_name=os.getenv('FLASK_CONFIG','development')
    app = Flask(__name__)
    app.config.from_object(myconfig[config_name])

    register_blueprint(app)
    register_manager(app)
    register_model(app)
    register_other(app)
    register_cache(app)
    register_celery(app)

    return  app

def register_blueprint(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(auth_bp)#url_prefix='/myblog'

def register_manager(app):
    login_manager.init_app(app=app)

def register_model(app):
    db.app=app
    db.init_app(app)

def register_cache(app):
    cache.init_app(app)


def register_celery(app):
   celery.init_app(app)

def register_other(app):
    moment.init_app(app)
    mail.init_app(app)

    # bootstrap.init_app(app)




def register_template_context(app):
    '''
    register global variable in all tempalte
    :param app:
    :return: a dict
    '''
    pass


