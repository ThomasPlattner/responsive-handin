from app.extensions.database import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    icon = db.Column(db.String)
    text = db.Column(db.Text)
    date = db.Column(db.Date)
    image_url = db.Column(db.String)
    image_name = db.Column(db.String)
    image_alt = db.Column(db.String)

# class Article_link(db.Model):
#     id = id.Column(db.Integer, primary_key=True)
#     image_url = db.Column(db.String)
#     image_name = db.Column(db.String)
#     image_alt = db.Column(db.String)