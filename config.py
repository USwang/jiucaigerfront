#数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'jcgstockdata'
USERNAME = 'root'
PASSWORD = 'mtjb1..'
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOSTNAME, port=PORT,
                                                                                        db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
