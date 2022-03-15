from app.auth import auth
from flask import render_template,redirect
from app.auth.forms import LoginForm





@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function tha renders login page
    '''
    title='login'
    form = LoginForm()
    return render_template('auth/login.html', title=title, form=form)