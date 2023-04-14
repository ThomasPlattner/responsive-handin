from flask import Blueprint, render_template, request, redirect
from app.articles.models import Category, Article, User, ArticleCategory
from app.extensions.database import db
import os.path
from werkzeug.utils import secure_filename

blueprint = Blueprint('new_article', __name__)

@blueprint.get('/manage')
def get_manage():
     articles = Article.query.all()
     return render_template('new_article/manage_articles.html', articles=articles)

# @blueprint.post('/manage')
# def delete_article(article_id):
#     delete = Article.query.filter_by(id=article_id).first()
#     if delete:
#          db.session.delete()
#     articles = Article.query.all()
#     article_delete = Article.query.get_or_404(article_id)
#     article_delete.delete()
#     return 


@blueprint.post('/manage')
def delete_article(article_id):
    articles = Article.query.all()
    article_delete = Article.query.get_or_404(article_id)
    db.session.delete(article_delete)
    db.session.commit()
    return render_template('new_article/manage_articles.html', articles=articles)

@blueprint.get('/new')
def get_article():
    categories = Category.query.all()
    return render_template('new_article/new.html', categories=categories)

@blueprint.post('/new')
def post_article():
    categories = Category.query.all()
    users = User.query.all()

    if not all([
        request.form['title'],
        request.form['icon'],
        request.form['text'],
        request.form['user_id'],
        request.files['article_image'],
        request.form['image_name'],
        request.form['image_alt'],
        ]):
            return render_template('new_article/new.html',
                categories=categories,
                users=users,
                error='Please fill out all fields to post your article'
                )
    
    # create an article
    article = Article(
        title = request.form['title'],
        icon = request.form['icon'],
        text = request.form['text'],
        user_id = request.form['user_id'],
        image_name = request.form['image_name'],
        image_alt = request.form['image_alt'],
    )
    article.save()

    # save the article image
    uploaded_file = request.files['article_image']
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save('app/static/images/upload/' + filename)

    # uploaded_file=request.files['article_image']
    # if uploaded_file.filename != '':
    #     file_ext = os.path.splitext(filename)
    #     if file_ext not in app.config['UPLOAD_EXTENSIONS']:
    #          abort(400)
    #     uploaded_file.save(os.path.join(app.config[UPLOAD_PATH], filename))

    # create rows in connector table for each article-category combination
    selected_categories = request.form.getlist('categories')
    for item in selected_categories:
        article_category = ArticleCategory(
            article_id = article.id,
            category_id = item,
        )
        article_category.save()

    return render_template('new_article/new.html', categories=categories, users=users)

@blueprint.get('/new-category')
def get_new_category():
    return render_template('new_article/new_category.html')

@blueprint.post('/new-category')
def post_new_category():
    # create a new category
    category = Category(
        categories = request.form['new_categories']
    )
    category.save()
    return render_template('new_article/new_category.html')

# @blueprint.get('/new-user')
# def get_new_user():
#     return render_template('new_article/new_user.html')

# @blueprint.post('/new-user')
# def post_new_user():
#     # create a new user
#     user = User(
#         name = request.form['new_user'],
#     )
#     user.save()
#     return render_template('new_article/new_user.html')
