from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()

def create_app(config_name):
    """
    Function that handles all app configs and initializing flask extensions

    Args:
        ConfigName:Configuration key setting
    """
    app = Flask(__name__)

    # create app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app,photos)
    simple.init_app(app)

    # registering the blueprint
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    app.register_blueprint(main_blueprint)

    return app