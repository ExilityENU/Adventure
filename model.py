from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
	__tablename__ = 'adventure.db'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), nullable=False)
	section = db.Column(db.String(50), nullable=False)