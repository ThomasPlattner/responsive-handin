from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin

class User(db.Model, CRUDMixin, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, index=True, unique=True)
    password = db.Column(db.String(1024))
    name = db.Column(db.String(20))