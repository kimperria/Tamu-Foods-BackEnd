from app import db



class User(db.Model):
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