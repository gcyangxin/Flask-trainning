#coding:utf8
from flask import redirect,url_for,render_template,request,flash,abort,current_app
from flask_login import login_required,login_user,logout_user,current_user
from myapp.extensions import  db
from myapp import User,Post,PostLike,Comment
from myapp.myForm import SendMessageForm,CommentForm,ProfileForm
from myapp.utils import MyValidate,ImageVlidator
from  flask import Blueprint

blog_bp=Blueprint('blog',__name__)

@blog_bp.route('/',methods=["POST","GET"])
@blog_bp.route('/index',methods=["POST","GET"])
def index():
    page=request.args.get('page',1,type=int)
    loc='index'

    per_page=current_app.config['PER_PAGE_NUM']
    form = SendMessageForm()
    commentForm=CommentForm()

    pagination=Post.query.order_by(Post.id.desc()).paginate(page=page,per_page=per_page)
    posts=pagination.items
    return render_template('index.html',
                           form=form,pagination=pagination,
                           posts=posts,
                           commentForm=commentForm,
                           flags=current_app.config['COMMENT_COUNT_VIEW'],
                           loc=loc)




@blog_bp.route('/profile',methods=['POST','GET'])
@login_required
def profile():
    page = request.args.get('page', 1, type=int)
    loc='profile'
    per_page = current_app.config['PER_PAGE_NUM']
    form=ProfileForm()
    commentForm = CommentForm()
    query=User.query.get(current_user.id)
    pagination = Post.query.filter_by(
                                    user_id=current_user.id).order_by(Post.id.desc()).paginate(page=page,
                                                                                                 per_page=per_page)
    posts = pagination.items


    myvalidator = MyValidate(form.avatar.data,
                             validators=[
                                 ImageVlidator(filename=query.name, save_path=current_app.config['AVATAR_SAVE_PATH'])
                             ])


    if form.submit.data:
        if form.validate_on_submit():
            query.about_me=form.text.data
            db.session.commit()
            flash('modfiy successfully')
            return redirect(url_for('blog.profile'))
    elif form.cancel.data:
        form.text.data = query.about_me
    elif form.submit_avatar.data:
        if myvalidator.validate():
            query.avatar=myvalidator.filename
            db.session.commit()
            flash('upload successfully')
            return redirect(url_for('blog.profile'))

    return render_template('profile.html',
                           form=form,
                           pagination=pagination,
                           posts=posts,
                           query=query,
                           myvalidator=myvalidator,
                           commentForm=commentForm,
                           flags=current_app.config['COMMENT_COUNT_VIEW'],
                           loc=loc)





@blog_bp.route('/newsend',methods=['POST','GET'])
@login_required
def new_message():
    form = SendMessageForm()
    if form.validate_on_submit():
        db.session.add(Post(current_user.id, form.message.data))
        db.session.commit()
        form.message.data = ''
        flash("send sucessfully!")
    return  redirect(url_for('blog.index')+'#posts')



@blog_bp.route('/<loc>/newreply/<int:post_id>/<int:parent_id>',methods=['POST','GET'])
@blog_bp.route('/<loc>/newcomment/<int:post_id>/<int:parent_id>',methods=['POST','GET'])
@login_required
def new_comment(post_id,parent_id,loc):

    post=Post.query.get_or_404(post_id)
    if post_id != parent_id:
        # if it it a reply parent_id should be in table comments of id field
        comment = Comment.query.get_or_404(parent_id)
    commentForm=CommentForm()
    if commentForm.validate_on_submit():

        db.session.add(Comment(current_user.id, commentForm.comment.data, post_id=post_id, parent_id=parent_id))
        db.session.commit()
        flash('comment successfully!')
    return redirect(url_for('blog.{}'.format(loc),post_id=post_id,parent_id=parent_id,loc=loc)+'#post_{}'.format(post_id))



@blog_bp.route('/<loc>/showpost/<int:post_id>',methods=['POST','GET'])
@login_required
def show_post(post_id,loc):
    '''readmore'''
    post = Post.query.get_or_404(post_id)
    loc='show_post'
    page=request.args.get('page',1,type=int)

    form = SendMessageForm()
    commentForm = CommentForm()


    return  render_template('postdetail.html',
                            posts=[post],
                            form=form,
                            commentForm=commentForm,
                            loc=loc,
                            page=page
                            )
@blog_bp.route('/<loc>/posts/<int:post_id>/thumb',methods=['GET'])
@blog_bp.route('/posts/<int:post_id>/thumb',methods=['GET'])
@login_required
def thumbup(post_id,loc):
    '''
    this view will redirect 2 kinds of view,need give all args
    :param post_id:
    :param loc:index,show_post
    :return:
    '''
    page=request.args.get('page',1,type=int)
    Post.query.get_or_404(post_id)

    if not PostLike.query.filter_by(post_id=post_id,user_id=current_user.id).first():

        db.session.add(PostLike(post_id,current_user.id))
        db.session.commit()

    return redirect(url_for('blog.{}'.format(loc),page=page,post_id=post_id,loc=loc))
