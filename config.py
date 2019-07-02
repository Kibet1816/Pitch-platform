import os

class Config():
    SECRET_KEY = 'blaugrana'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://denis1816:kibet@localhost/forza'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass
    
class DevConfig(Config):
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}