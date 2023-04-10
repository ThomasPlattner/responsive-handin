from flask import Blueprint, render_template, request
from app.articles.models import Category, Article, User

blueprint = Blueprint('new_article', __name__)

@blueprint.get('/new')
def get_article():
    categories = Category.query.all()
    return render_template('new_article/new.html', categories=categories)

@blueprint.post('/new')
def post_article():
    # create an article
    article = Article(
        icon = request.form['icon']
    )
    article.save()

    categories = Category.query.all()
    return render_template('new_article/new.html', categories=categories)