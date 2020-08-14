#coding:utf8
from flask import redirect,url_for,render_template,request,flash,abort,current_app
from flask_login import login_required,login_user,logout_user,current_user
from myapp import User,Post,PostLike,Comment
from  flask import Blueprint
from myapp.myForm import  LoginForm,ResgiterForm
from myapp.extensions import  db
from myapp.utils import redirect_back

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/register',methods=["POST","GET"])
def register():
    form=ResgiterForm()

    if form.validate_on_submit():
        userObj = User.query.filter_by(name=form.name.data).first()


        if userObj:
            flash('username exists!')
            return redirect(url_for('.register'))
        else:
            if User.query.filter_by(email=form.email.data).first():
                flash('Email exists!')
                return redirect(url_for('.register'))
            db.session.add(User(form.name.data, form.email.data, form.passwd.data))
            db.session.commit()
            flash('register successfully,please log in!')
            return redirect(url_for('.login'))

    return render_template('register.html',form=form)

@auth_bp.route('/login',methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form=LoginForm()
    if form.validate_on_submit():

        userObj=User.query.filter_by(name=form.name.data).first()
        if userObj and userObj.checkPassword(form.passwd.data):
            login_user(userObj)
            flash('You are logged in successfully')
            # return redirect(url_for('blog.index'))
            return redirect_back('blog.index')
        else:

            flash("username or password is  wrong!")
    return render_template('login.html', form=form)




@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    # return redirect(url_for('blog.index'))
    return redirect_back('blog.index')