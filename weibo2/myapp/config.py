
import  os

baseDir=os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY='xin' or os.urandom(24)
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:passwd@localhost:3306/flaskdb2?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    AVATAR_SAVE_PATH=os.path.join(baseDir,'static/avatar')
    PER_PAGE_NUM=5
    PER_PAGE_COMMENT_NUM=5
    DETAIL_COMMNET_NUM=10
    THUMB_ICON='/static/icon/'
    USER_AVATAR='/static/avatar/'
    COMMENT_ICON='/static/icon/commet.jpg'

    #if COMMENT_COUNT_VIEW equals to hide ,html page will show at most PER_PAGE_COMMENT_NUM comments
    #else will show all comments
    COMMENT_COUNT_VIEW='hide'

    #flask-caching redis
    CACHE_TYPE='redis'
    CACHE_REDIS_HOST='localhost'  # redis ip
    CACHE_REDIS_PORT=6379 # port
    CACHE_REDIS_DB=2  #  db
    CACHE_REDIS_PASSWORD=''

    #celery
    CELERY_BROKER_URL='redis://localhost:6379/3'
    CELERY_RESULT_BACKEND='redis://localhost:6379/3'

    # Flask-Mail configuration
    MAIL_SERVER='smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL=True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_USERNAME')
    MAIL_DEBUG=False

class DevelopmentConfig(BaseConfig):

    pass




myconfig ={
    'development':DevelopmentConfig
}
