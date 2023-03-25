from flask import Flask, redirect, url_for, render_template
from .articles.routes import article_list
from . import articles

app = Flask(__name__)
app.config.from_object('app.config')

@app.route('/')
def index():
    articles = article_list
    return render_template('index.html', articles=articles)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-me')
def about_me():
    return redirect('/about')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/<slug>')
def none(slug):
    message = "Sorry, the page about " + slug + " doesn't exist."
    return render_template('/base.html', message=message)

app.register_blueprint(articles.routes.blueprint)