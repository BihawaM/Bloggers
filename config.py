import os

class Config:
    SECRET_KEY ='SECRET_KEY'
    UPLOADED_PHOTOS_DEST ='app/static/images'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'bihawam271@gmail.com'
    
    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        debug = os.environ.get("DEBUG")
        
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/bloggers_test'
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/bloggers'
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}