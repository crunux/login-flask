class Config: 
    SECRET_KEY = '!#CJAra@^DSddSD*Dd'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Cross19950502'
    MYSQL_DB = 'login'

config={
    'development': DevelopmentConfig
}