import os

class Config():
    SECRET_KEY = 'blaugrana'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://denis1816:kibet@localhost/forza'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}