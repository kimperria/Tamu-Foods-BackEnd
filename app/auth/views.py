from app.auth import auth
from flask import render_template,redirect
from app.auth.forms import LoginForm, SignUpForm





@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function tha renders login page
    '''
    title='login'
    form = LoginForm()
    return render_template('auth/login.html', title=title, form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    Function that renders signup page
    '''
    title = 'signup'
    form = SignUpForm()
    return render_template('auth/signup.html', title=title, form=form)