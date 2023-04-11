from flask import Blueprint, render_template, request
from app.articles.models import Category, Article, User, ArticleCategory

blueprint = Blueprint('new_article', __name__)

@blueprint.get('/new')
def get_article():
    categories = Category.query.all()
    return render_template('new_article/new.html', categories=categories)

@blueprint.post('/new')
def post_article():
    # user_name = request.form['user']
    # user = User.query.filter(User.id == user_name).first()

    # create an article
    article = Article(
        title = request.form['title'],
        icon = request.form['icon'],
        text = request.form['text'],
        user_id = request.form['user'],
    )
    article.save()

    categories = Category.query.all()
    users = User.query.all()
    return render_template('new_article/new.html', categories=categories, users=users)

@blueprint.get('/new-category')
def get_new_article():
    return render_template('new_article/new_category.html')

@blueprint.post('/new-category')
def post_new_article():
    # create a new category
    category = Category(
        categories = request.form['new_categories']
    )
    category.save()
    return render_template('new_article/new_category.html')

@blueprint.get('/new-user')
def get_new_user():
    return render_template('new_article/new_user.html')

@blueprint.post('/new-user')
def post_new_user():
    # create a new user
    user = User(
        name = request.form['new_user'],
    )
    user.save()
    return render_template('new_article/new_user.html')
