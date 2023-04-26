from flask import Blueprint, render_template, request, redirect, url_for
from app.articles.models import Category, Article, ArticleCategory
from app.users.models import User
from app.extensions.database import db
import os.path
from werkzeug.utils import secure_filename
from flask_login import login_required
from sqlalchemy import select

blueprint = Blueprint('manage', __name__)

# Management interface - GET page & POST delete

@blueprint.get('/manage')
@login_required
def manage_articles():
    articles = Article.query.all()
    return render_template('manage/manage_articles.html', articles=articles)

@blueprint.post('/manage/<int:article_id>')
@login_required
def post_delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    article.delete()

    article_category_rows = ArticleCategory.query.filter_by(article_id=article.id)
    article_category_rows.delete()
    # ArticleCategory.query.filter_by(article_id=article.id).delete()

    return redirect(url_for('manage.manage_articles'))

# New article

@blueprint.get('/new')
@login_required
def get_article():
    categories = Category.query.all()
    new_article = Article.query.all()
    return render_template('manage/new.html', categories=categories, new_article=new_article)

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
            return render_template('manage/new.html',
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
    selected_categories_ids = request.form.getlist('categories')

    for item in selected_categories_ids:
        category_id = item
        article_category = ArticleCategory(
            article_id = article.id,
            category_id = category_id,
        )
        article_category.save()

    return redirect(url_for('general_pages.index'))

# edit article

@blueprint.get('/edit/<int:article_id>')
@login_required
def get_edit_article(article_id):
    article = Article.query.get_or_404(article_id)
    categories = Category.query.all()
    ticked_categories = Category.query.join(ArticleCategory.category)\
        .filter(ArticleCategory.article_id == article.id).all()
    return render_template('manage/new.html', categories=categories, article=article, ticked_categories=ticked_categories)

@blueprint.post('/edit/<int:article_id>')
@login_required
def post_edit_article(article_id):
    categories = Category.query.all()

    if not all([
    request.form['title'],
    request.form['icon'],
    request.form['text'],
    # request.files['article_image'],
    request.form['image_name'],
    request.form['image_alt'],
    ]):
        return render_template('manage/new.html',
            categories=categories,
            article=article,
            error='Please fill out all fields to post your article'
        )

    article = Article.query.get_or_404(article_id)
    article.icon = request.form['icon']
    article.title = request.form['title']
    article.text = request.form['text']
    article.image_name = request.form['image_name']
    article.image_alt = request.form['image_alt']

    article.save()


    # # save the article image
    # uploaded_file = request.files['article_image']
    # filename = secure_filename(uploaded_file.filename)
    # uploaded_file.save('app/static/images/upload/' + filename)
    
    # create rows in connector table for each article-category combination
    selected_categories_ids = request.form.getlist('categories')

    ArticleCategory.query.filter_by(article_id=article.id).delete()

    for item in selected_categories_ids:
        category_id = item
        article_category = ArticleCategory(
            article_id = article.id,
            category_id = category_id,
        )
        article_category.save()


    return redirect(url_for('general_pages.index'))

# CRUD categories

@blueprint.get('/manage/category')
@login_required
def get_category():
    categories = Category.query.order_by(Category.id.asc()).all()

    return render_template('manage/crud_category.html', categories=categories)

@blueprint.post('/manage/category')
@login_required
def post_new_category():
    categories = Category.query.all()

    # check if category already exists
    existing_category = Category.query.filter_by(categories=request.form['new_categories']).first()
    if existing_category:
        return render_template('manage/crud_category.html', 
        categories=categories,
        error = 'The category already exists.')

    # create a new category
    if request.form['new_categories']:
        category = Category(
        category = request.form['new_categories']
        )
        category.save()
        return redirect(url_for('manage.get_category'))

    return render_template('manage/crud_category.html', 
        error='You did not add a category', 
        categories=categories)

@blueprint.post('/manage/category/delete/<int:category_id>')
@login_required
def post_delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    category.delete()

    return redirect(url_for('manage.get_category'))


@blueprint.post('/manage/category/<int:category_id>')
@login_required
def post_edit_category(category_id):
    categories = Category.query.all()

    # check if input field is empty
    if not request.form['edit_categories']:
        return render_template('manage/crud_category.html',
            categories=categories,
            error = "The category has to have a name")
    
    # edit selected category
    category = Category.query.get_or_404(category_id)
    category.category = request.form['edit_categories']

    category.save()

    return redirect(url_for('manage.get_category'))