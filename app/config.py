import os

class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    MYSQL_HOST = 'database-mysql.ceqq93gikl7l.eu-west-1.rds.amazonaws.com'
    #MYSQL_HOST =  os.environ.get("MYSQL_HOST")
    MYSQL_USER = 'admin'
    #MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_PASSWORD = 'admin1234'
    #MYSQL_PASSWORD =  os.environ.get("MYSQL_PASSWORD")
    MYSQL_DB = 'test'
   # MYSQL_DB =  os.environ.get("MYSQL_DB")
