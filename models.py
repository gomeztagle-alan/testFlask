from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_address = db.Column(db.String(64), nullable=False)
    password = db.Column(db.Integer, nullable=False)

