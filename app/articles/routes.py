from flask import Blueprint, render_template
from .models import Article, Category, ArticleCategory

blueprint = Blueprint('articles', __name__)
    
@blueprint.route('/blog/<slug>')
def blog(slug):
    blogs = Article.query.all()
    for article in blogs:
        if slug.title() == article.title:
            text = article.text
            title = article.title

            categories = []
            article_categories = ArticleCategory.query.filter_by(article_id=article.id).all()
            for article_category in article_categories:
                category = Category.query.with_entities(Category.category).filter_by(id=article_category.category_id).first()
                categories.append(category[0])

            return render_template('articles/article_template.html', text=text, article=article, title=title, categories=categories)
            break
    else:
        message = "Sorry, we couldn't find the article about " + slug + " :( "
        return render_template('/base.html', message=message)
    