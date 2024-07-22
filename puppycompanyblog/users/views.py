
from flask import url_for,render_template,flash,redirect,request,Blueprint
from flask_login import login_required,login_user,logout_user,current_user
from puppycompanyblog import db
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)


#registration
@users.route("/registration",methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.data.email,username=form.data.username,password=form.data.password)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for Registration!')
        return redirect(url_for('users.login'))

    return render_template('register.html',form=form)

#login
@users.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Login Successfull!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.index')
            
            return redirect(next)
        
        return render_template('login.html',form=form)

#logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))

#account (update FlaskForm)

# user's list of blog posts
