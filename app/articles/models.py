from app.extensions.database import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String, unique=True)
    icon = db.Column(db.String)
    text = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    image_url = db.Column(db.String)
    image_name = db.Column(db.String)
    image_alt = db.Column(db.String)

# class User(db.Model): #is this the right place for this model?
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String)
#     password = db.Column(db.String)
#     name = db.Column(db.String)

# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     categories = db.Column(db.String)

# class Topic(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))