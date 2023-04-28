def serialize_articles(articles):
    articles_list = []

    for article in articles:
        articles_list.append({
            'id': article.id,
            'title': article.title,
            'icon': article.icon,
            'text': article.text,
            'date': article.date,
        })
    
    return articles_list

def serialize_users(users):
    users_list = []

    for user in users:
        users_list.append({
            'id': user.id,
            'name': user.name,
        })
    return users_list

def serialize_categories(categories):
    categories_list = []

    for category in categories:
        categories_list.append({
            'id': category.id,
            'categories': category.categories,
        })
    return categories_list

def serialize_article_categories(article_categories):
    article_categories_list = []

    for article_category in article_categories:
        article_categories_list.append({
            'id': article_category.id,
            'article_id': article_category.article_id,
        })
    return article_categories_list