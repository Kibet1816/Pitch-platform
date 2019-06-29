from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask import Blueprint
from


bootstrap = Bootstrap()

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

    return app