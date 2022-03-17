import logging
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



bootstrap=Bootstrap()
db=SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'



def createapp(config_class=Config):
    '''
    Factory function
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)



    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

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
    '''
    Registering main blueprint
    '''
    from app.main import main as main_bp
    app.register_blueprint(main_bp)


    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)

    return app



from app import model
'''
Help db initialization
'''