from app.articles.models import Article, User, Category

def test_get_new_article_renders(client):
    # page loads & renders
    response = client.get('/new-article')
    assert b'new' in response.data

def test_post_new_article_creates_article(client):
    # writes and saves the article
    response = client.post('/new-article', data={
        'title': 'test title',
    })
    assert Article.query.first() is not None