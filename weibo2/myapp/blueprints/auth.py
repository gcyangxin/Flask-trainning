#coding:utf8
from flask import redirect,url_for,render_template,request,flash,abort,current_app,Blueprint,session
from flask_login import login_required,login_user,logout_user,current_user
from myapp import User,Post,PostLike,Comment
from myapp.myForm import  LoginForm,ResgiterForm
from myapp.extensions import  db,cache
from myapp.utils import redirect_back,send_async_email,random_num,hello
import  time


auth_bp=Blueprint('auth',__name__)

def cache_unless():
    submit=request.method
    return submit=="post"

@auth_bp.route('/register',methods=["POST","GET"])
@cache.cached(timeout=10,unless=cache_unless)
def register():
    form=ResgiterForm()
    if request.method=="GET" and request.args.get('email'):
        # print(request.args.get('email'),'email')
        code = random_num()
        cache.set("code:{}".format(request.args.get('email')), code, timeout=5 * 60)

        send_async_email.delay("Mail Validation",
                         request.args.get('email'),
                         " blog Captcha : {} \n 5 minutes availability.".format(code))
    elif request.method=="POST":
        if form.validate():
            userObj = User.query.filter_by(name=form.name.data).first()

            if userObj:
                flash('username exists!')
                return redirect(url_for('.register'))
            else:
                if User.query.filter_by(email=form.email.data).first():
                    flash('Email exists!')
                    return redirect(url_for('.register'))
                Vcode=cache.get("code:{}".format(form.email.data))
                if Vcode and int(Vcode) == form.validationCode.data:
                    db.session.add(User(form.name.data, form.email.data, form.passwd.data))
                    db.session.commit()
                    flash('register successfully,please log in!')

                    return redirect(url_for('auth.login'))
                else:
                    flash("validationCode is wrong!")
    return render_template('register.html',form=form)




@auth_bp.route('/login',methods=["POST","GET"])
@cache.cached(timeout=10,unless=cache_unless)
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form=LoginForm()
    # print('auth',request.form,session),'\n'
    if form.validate_on_submit():

        userObj=User.query.filter_by(name=form.name.data).first()
        if userObj and userObj.checkPassword(form.passwd.data):
            login_user(userObj)
            flash('You are logged in successfully')
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