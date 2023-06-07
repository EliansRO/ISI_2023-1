class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'pensiones-isi-2023'
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}