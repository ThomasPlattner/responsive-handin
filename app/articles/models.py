from app.extensions.database import db
from datetime import datetime

# class ArticleCategory(db.Model):
    # article_id = db.Column(db.Integer, db.ForeignKey('article.id'), primary_key=True)
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    # articles = db.relationship('Article', backref='user', lazy=True)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    icon = db.Column(db.String)
    text = db.Column(db.Text)
    date = db.Column(db.Date, default=datetime.utcnow)
    image_url = db.Column(db.String)
    image_name = db.Column(db.String)
    image_alt = db.Column(db.String)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # article_categories = db.relationship('ArticleCategory', backref='article', lazy=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String)
    # article_categories = db.relationship('ArticleCategory', backref='category', lazy=True)

