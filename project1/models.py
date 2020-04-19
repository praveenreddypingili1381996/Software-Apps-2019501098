from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.String, nullable=False)