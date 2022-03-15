from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap



bootstrap=Bootstrap()



def createapp(config_class=Config):
    '''
    Factory function
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)


    '''
    Registering auth blueprint
    '''
    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)
    '''
    Registering errores blueprint
    '''
    from app.errors import errors as errors_bp
    app.register_blueprint(errors_bp)

    return app