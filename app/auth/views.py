from app.auth import auth
from flask import render_template,redirect




@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function tha renders login page
    '''
    title='login'
    return render_template('auth/login.html')