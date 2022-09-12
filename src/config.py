class Config: 
    SECRET_KEY = '!#CJAra@^DSddSD*Dd'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'user'
    MYSQL_PASSWORD = 'password'
    MYSQL_DB = 'database_name'

config={
    'development': DevelopmentConfig
}