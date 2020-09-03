#coding:utf8
from  myapp import create_app
from myapp import User,Post,PostLike,Comment
from myapp import celery

app=create_app()

if __name__=='__main__':

    app.run(debug=True)
