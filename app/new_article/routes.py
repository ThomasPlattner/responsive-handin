from flask import Blueprint, render_template, request, redirect, url_for
from app.articles.models import Category, Article, ArticleCategory
from app.users.models import User
from app.extensions.database import db
import os.path
from werkzeug.utils import secure_filename
from flask_login import login_required

blueprint = Blueprint('new_article', __name__)

@blueprint.get('/manage')
@login_required
def get_manage():
    articles = Article.query.all()
    return render_template('new_article/manage_articles.html', articles=articles)

@blueprint.post('/manage/<int:article_id>')
@login_required
def delete_article(article_id):
    articles = Article.query.all()
    article = Article.query.get_or_404(article_id)
    article.delete()

    return redirect(url_for('new_article.get_manage'))

@blueprint.get('/new')
@login_required
def get_article():
    categories = Category.query.all()
    return render_template('new_article/new.html', categories=categories)

@blueprint.post('/new')
@login_required
def post_article():
    categories = Category.query.all()

    if not all([
        request.form['title'],
        request.form['icon'],
        request.form['text'],
        request.files['article_image'],
        request.form['image_name'],
        request.form['image_alt'],
        ]):
            return render_template('new_article/new.html',
                categories=categories,
                error='Please fill out all fields to post your article'
                )
    
    # create an article
    article = Article(
        title = request.form['title'],
        icon = request.form['icon'],
        text = request.form['text'],
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

    return redirect(url_for('general_pages.index'))

@blueprint.get('/new-category')
@login_required
def get_new_category():
    return render_template('new_article/new_category.html')

@blueprint.post('/new-category')
@login_required
def post_new_category():
    # create a new category
    category = Category(
        categories = request.form['new_categories']
    )
    category.save()
    return render_template('new_article/new_category.html')