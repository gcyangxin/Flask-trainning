#coding:utf8
from flask_wtf import  FlaskForm
from wtforms import StringField,validators,PasswordField,SubmitField,TextAreaField,FileField,IntegerField

class SendMessageForm(FlaskForm):
    message = TextAreaField('message',
                            validators=[
                                        validators.length(min=1,max=128,message="Enter %(min)d-%(max)d characters"),
                                        validators.DataRequired('Enter valid messages')],
                                        # render_kw={'onkeyup':"count(this)"}
                            #  # add js funtion to check length of text always
                            # filters =(strip,)
                            )

    submit=SubmitField('Send')



class ProfileForm(FlaskForm):
    avatar = FileField('avatar')
    text=TextAreaField('sign',
                       validators=[validators.length(max=15,message='Length of characters less than %(max)d')],
                       )
    submit=SubmitField('Modify')
    cancel=SubmitField('Cancel')
    submit_avatar=SubmitField('Upload')

class LoginForm(FlaskForm):
    name = StringField("Name:",
                       validators=[validators.DataRequired("Enter your name"),
                                   validators.Regexp(r'^[a-zA-Z0-9\u4e00-\u9fa5]+$',message='invalid input.')],
                       render_kw={'placeholder':'name'}

    )
    passwd=PasswordField("Password:",validators=[validators.required("Enter your password")],render_kw={'placeholder':'Passwords'})
    submit=SubmitField('LogIn')

class ResgiterForm(FlaskForm):
    name=StringField('name',
                     validators=[
                                validators.DataRequired("Enter name"),
                                validators.length(min=2,max=12,message="Enter %(min)d-%(max)d characters"),
                                validators.Regexp(r'([a-zA-Z\u4e00-\u9fa5])([a-zA-Z0-9\u4e00-\u9fa5]+$)',message=\
                                                 'only contains chinese,english,and not starts with number')],
                     render_kw={'placeholder': 'name,not start with number'}
                     )
    email=StringField('email',
                      validators=[validators.email("Enter your email"),
                                  validators.DataRequired("Enter your email")],
                      render_kw={'placeholder': 'email'}
                      )
    passwd=PasswordField('passwd',
                         validators=[validators.DataRequired("Enter your passwords"),
                                     validators.length(min=6,max=12,message="Enter %(min)d-%(max)d characters")],
                         render_kw={'placeholder': '6-12 charaters'}

                         )
    passwd2=PasswordField('repeatpasswd', validators=[validators.equal_to('passwd',"password must match")],
                          render_kw={'placeholder': 'repeat passwords'}
                          )

    Captcha=IntegerField('Captcha',
                                validators=[validators.DataRequired("Enter Verfication")],
                                render_kw={'placeholder': 'please input 6 numbers in your email'}
                                )


    submit=SubmitField('Register')



class CommentForm(FlaskForm):
    comment = TextAreaField('comment',
                            validators=[
                                validators.length(min=1, max=128, message="Enter %(min)d-%(max)d characters"),
                                validators.DataRequired('Enter valid messages')],
                            render_kw={'class_':'newCommentTextarea'}
                            #  # add js funtion to check length of text always
                            # filters =(strip,)
                            )

    submit = SubmitField('Send')
