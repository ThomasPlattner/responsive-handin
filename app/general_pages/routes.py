from flask import Blueprint, render_template, redirect, url_for
from app.articles.models import Article

blueprint = Blueprint('general_pages', __name__)

@blueprint.route('/')
def index():
    all_articles = Article.query.all()
    return render_template('general_pages/index.html', articles=all_articles)

@blueprint.route('/about')
def about():
    return render_template('general_pages/about.html')

@blueprint.route('/about-me')
def about_me():
    return redirect('/about')

@blueprint.route('/categories')
def categories():
    return render_template('general_pages/categories.html')

@blueprint.route('/contact')
def contact():
    return render_template('general_pages/contact.html')

@blueprint.route('/<slug>')
def none(slug):
    message = "Sorry, the page about " + slug + " doesn't exist."
    return render_template('/base.html', message=message)
