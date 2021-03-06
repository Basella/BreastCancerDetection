import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # SQLALCHEMY_DATABASE_URI = "sqlite:///resultdb.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SQLALCHEMY_ECHO = False

    # set the SECRET_KEY for CSRF
    # SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youwillneverguess'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
