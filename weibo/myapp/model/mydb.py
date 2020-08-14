#coding:utf8
from  datetime import  datetime
from myapp.extensions import db


class User(db.Model):
    #use UserMixin is ok too

    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(32),unique=True)
    email=db.Column(db.String(64),unique=True)
    password=db.Column(db.String(32))
    about_me=db.Column(db.String(64))
    register_time=db.Column(db.DateTime,default=datetime.now())
    avatar=db.Column(db.String(32))
    posts = db.relationship('Post', backref='user', lazy='dynamic')



    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        self.authentication=False

    def __repr__(self):
        return '<User:%s>'% self.name

    def get_user(self,name):
        return User.query.filter_by(name=name).first()

    def is_authenticated(self):
        return True if self.authentication else False
    def is_active(self):
        return True
    def is_anonymous(self):
        return (True if self.authentication else False)
    def get_id(self):
        return unicode(self.id)

    def checkPassword(self,InPassword):
        if InPassword == self.password:
            self.authentication=True
            return True
        else:
            return False
    def checkNameRepeat(self,inname):
        return True  if inname ==self.name else False
    def checkEmailRepeat(self,inemail):
        return  True if inemail == self.email else False
    def checkReapt(self,name,email):

        return self.checkEmailRepeat(email) and self.checkNameRepeat(name)




class Post(db.Model):
    __tablename__='post'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    send_time=db.Column(db.DateTime,default=datetime.now())
    body=db.Column(db.String(128))
    post_like_person_ids=db.relationship('PostLike',backref='post',lazy='dynamic',foreign_keys='PostLike.post_id')
    all_comments=db.relationship('Comment',backref='post',lazy='dynamic',foreign_keys='Comment.post_id')#class.filed to assignment


    def __init__(self,user_id,body):

        self.body=body
        self.user_id=user_id

    def __repr__(self):
        return '<Post:%s>'% self.body
class PostLike(db.Model):
    __tablename__='post_likes'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    post_id=db.Column(db.Integer,db.ForeignKey('post.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,post_id,user_id):
        self.post_id=post_id
        self.user_id=user_id

    def __repr__(self):
        return '<PostLike:post %s is liked by uesr %s>'%(self.post_id,self.user_id)

class Comment(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    send_time = db.Column(db.DateTime,default=datetime.now())
    comment_body=db.Column(db.Text)
    post_id=db.Column(db.Integer,db.ForeignKey('post.id'))
    parent_id=db.Column(db.Integer)#if it equals to comments.id that is relpy,otherwise comment
    comment_like_count=db.Column(db.Integer,default=0)

    def __init__(self,user_id,comment_body,post_id,parent_id):
        self.user_id=user_id
        self.comment_body=comment_body
        self.post_id=post_id
        self.parent_id=parent_id
    def __repr__(self):
        return '<Comment:user %s \'s comment in comment_id %s in post_id:%s>'%(self.user_id,self.parent_id,self.post_id)
