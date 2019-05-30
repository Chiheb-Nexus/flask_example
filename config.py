#
# Flask config
#


class Config(object):
    pass


class ProdConf(Config):
    DEBUG = False


class DevConf(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CELERY_RESULT_BACKEND = 'rpc://'
    CELERY_BROKER_URL = 'pyamqp://USER:PASSWORD@localhost/YOUR_VHOST'
