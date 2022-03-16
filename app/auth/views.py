import email
from app.auth import auth
from flask import flash, render_template,redirect, url_for
from app.auth.forms import LoginForm, SignUpForm
from app.model import User
from flask_login import current_user, login_user,logout_user
from app import db





@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function tha renders login page
    '''
    if current_user.is_authenticated:
        '''
        Function that approves user
        '''
        return redirect(url_for('main.index'))
    title='login'
    form = LoginForm()
    if form.validate_on_submit():
        '''
        Logic that creates a user after clicking submit
        '''
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            '''
            condition that handles user input
            '''
            flash('Invalid username or password')
            return render_template(url_for('auth.login'))
        login_user(user)
        flash('LogIn sucess')
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title=title, form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    Function that renders signup page
    '''
    if current_user.is_authenticated:
        '''
        Logic that handles user approval
        '''
        return redirect(url_for('main.index'))
    title = 'signup'
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        '''
        Condition that creates a new user variable and adds to database
        '''
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome to Tamu Foods community we look forward to serve you')
        return redirect('login')
    return render_template('auth/signup.html', title=title, form=form)



@auth.route('/logout')
def logout():
    '''
    Function that handles log out
    '''
    logout_user()
    return redirect(url_for('main.index'))