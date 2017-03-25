from inc.db import db

class HomeModel(db.Model):
	__tablename__ = 'dummy'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(255), nullable=False)