from flask import render_template,flash
from app.main import main
from app import db




@main.route('/')
def index():
    '''
    View function that set display on home page
    '''
    title='Home'
    return render_template('index.html', title=title)