import os

class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    #MYSQL_HOST = 'localhost'
    MYSQL_HOST =  os.environ.get("MYSQL_HOST")
    #MYSQL_USER = 'root'
    MYSQL_USER = os.environ.get("MYSQL_USER")
    #MYSQL_PASSWORD = ''
    MYSQL_PASSWORD =  os.environ.get("MYSQL_PASSWORD")
    #MYSQL_DB = 'test_db'
    MYSQL_DB =  os.environ.get("MYSQL_DB")
