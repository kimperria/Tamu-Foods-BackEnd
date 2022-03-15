import email
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length




class LoginForm(FlaskForm):
    '''
    Class that handles user log in
    '''
    email = StringField('email', validators=[DataRequired(), Length(1,20)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('LogIn')