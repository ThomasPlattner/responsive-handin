from flask import Blueprint, render_template, redirect, request, current_app
from app.articles.models import Article

blueprint = Blueprint('general_pages', __name__)

@blueprint.route('/')
def index():
    page_number = request.args.get('page', 1, type=int)
    articles_pagination = Article.query.paginate(page=page_number, per_page=current_app.config['ARTICLES_PER_PAGE'])
    return render_template('general_pages/index.html', articles_pagination=articles_pagination)

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
