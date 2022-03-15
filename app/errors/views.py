from app.errors import errors
from flask import redirect, render_template



@errors.app_errorhandler(404)
def not_found(error):
    '''
    Function that renders page not found error
    '''
    return render_template('errors/404.html')