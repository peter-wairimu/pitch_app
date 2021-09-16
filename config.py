
import os


class Config:
    '''
    General configuration parent class

    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wairimu22@localhost/watchlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN =True



    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wairimu22@localhost/watchlist_test'

    
class ProdConfig(Config):
    '''
    production configuration child class

    Args:
        config:  The parent configuration class with General configuration settings

    '''



class DevConfig(Config):
    '''
    Development configuration child class

    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wairimu22@localhost/watchlist'
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
    