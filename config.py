import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    POSTGRES_USER = '<db user name>'
    POSTGRES_PASSWORD = '<db user password>'
    POSTGRES_PORT = '<db port>'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'postgres+psycopg2://<db admin user>:<db admin password>@172.17.0.1:<available port>/clix_dashboard_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 20
    BCRYPT_LOG_ROUNDS = 13
    UPLOAD_FOLDER = basedir + '/SchoolImages'


class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # new


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # new


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')  # new


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # new
