import email
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length, EqualTo




class LoginForm(FlaskForm):
    '''
    Class that handles user log in
    '''
    email = StringField('email', validators=[DataRequired(), Length(1,20)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('LogIn')


class SignUpForm(FlaskForm):
    '''
    Class that handles user sign in
    '''
    username = StringField('Username', validators=[
                           DataRequired(), Length(2, 15)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('SignUp')