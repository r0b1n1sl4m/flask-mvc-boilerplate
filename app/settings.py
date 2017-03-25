# configuration
class Config():
	DEBUG = True
	#db
	SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flask-boilerplate'
	SQLALCHEMY_TRACK_MODIFICATIONS = False