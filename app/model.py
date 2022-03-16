from app import db, login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    '''
    Function that handles logged in user in each user session'
    '''
    return User.query.get(int(id))
class User(UserMixin, db.Model):
    '''
    Class that defines user instace with its attributes
    '''

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    phone_number = db.Column(db.Integer)


    def __repr__(self):
        return '<User {}>'.format(self.username)


    def set_password(self, password):
        '''
        Function that creates hash password on db
        '''
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''
        Function that confirms correct user password in db
        '''
        return check_password_hash(self.password_hash, password)
        