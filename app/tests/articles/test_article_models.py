from app.extensions.database import db
from app.articles.models import Article

def test_article_update(client):
    # updates article's properties
    article = Article(title='balloon', icon='🎈')
    db.session.add(article)
    db.session.commit()

    article.name = 'Balloons'
    article.save()

    updated_article = Article.query.filter_by(title='balloon').first()
    assert updated_article.name == 'Balloons'

def test_article_delete(client):
    # deletes article
    article = Article(title='balloon', icon='🎈')
    db.session.add(article)
    db.session.commit()

    article.delete()

    deleted_article = Article.query.filter_by(title='balloon').first()
    assert deleted_article is None