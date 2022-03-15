from flask import Flask
from config import Config







def createapp(config_class=Config):
    '''
    Factory function
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)


    '''
    Registering auth blueprint
    '''
    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    return app