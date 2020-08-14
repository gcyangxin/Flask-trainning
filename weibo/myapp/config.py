
import  os

baseDir=os.path.abspath(os.path.dirname(__name__))
class BaseConfig(object):
    SECRET_KEY='' or os.urandom(24)

    #SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:<passwd>@localhost:3306/<your database>?charset=utf8'
    SQLALCHEMY_DATABASE_URI=''
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    AVATAR_SAVE_PATH=os.path.join(baseDir,'myapp/static/avatar')

    PER_PAGE_NUM=5
    PER_PAGE_COMMENT_NUM=5
    DETAIL_COMMNET_NUM=10
    THUMB_ICON='/static/icon/'
    USER_AVATAR='/static/avatar/'
    COMMENT_ICON='/static/icon/commet.jpg'

    #if COMMENT_COUNT_VIEW equals to hide ,html page will show at most PER_PAGE_COMMENT_NUM comments
    #else will show all comments
    COMMENT_COUNT_VIEW='hide'

class DevelopmentConfig(BaseConfig):

    pass




myconfig ={
    'development':DevelopmentConfig
}
