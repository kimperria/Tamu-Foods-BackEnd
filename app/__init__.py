from flask import Flask
import sqlalchemy
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



bootstrap=Bootstrap()
db=SQLAlchemy()
migrate = Migrate()



def createapp(config_class=Config):
    '''
    Factory function
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)



    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)

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

    return app