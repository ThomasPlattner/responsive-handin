from flask import Flask, redirect, url_for, render_template
from model import article_list

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

@app.route('/blog/<slug>')
def blog(slug):
    articles = article_list
    for article in article_list:
        if slug.title() == article['title']:
            url = slug.lower() + ".html"
            return render_template(url)
            break
    else:
        message = "Sorry, we couldn't find the article about " + slug + " :( "
        return render_template('/base.html', message=message) 

@app.route('/<slug>')
def none(slug):
    message = "Sorry, the page about " + slug + " doesn't exist."
    return render_template('/base.html', message=message)

