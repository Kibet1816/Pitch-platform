import os

class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://denis1816:kibet@localhost/forza'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}