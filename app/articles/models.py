from app.extensions.database import db, CRUDMixin
from datetime import datetime

class ArticleCategory(db.Model, CRUDMixin):
    __tablename__ = 'article_category'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id', name='fk_article_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', name='fk_category_id'))

class Article(db.Model, CRUDMixin):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    icon = db.Column(db.String(30))
    text = db.Column(db.String(20000))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_name = db.Column(db.String(30))  #needed? How does naming work?
    image_alt = db.Column(db.String(80)) 
    article_categories = db.relationship('ArticleCategory', backref='article', lazy=True)


class Category(db.Model, CRUDMixin):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String(30))
    article_categories = db.relationship('ArticleCategory', backref='category', lazy=True)