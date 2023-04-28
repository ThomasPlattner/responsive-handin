from flask import Blueprint, jsonify, request
from .services.serialize_articles import serialize_articles, serialize_users, serialize_article_categories, serialize_categories
from ..articles.models import Article, Category, ArticleCategory
from ..users.models import User
from os import environ

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/articles')
def articles():
    if environ.get('API_KEY') == request.args.get('key'):
        articles = Article.query.all()
        return jsonify(
            serialize_articles(articles)
        )
    else:
        return jsonify({'error': 'Invalid API key'}), 401

@blueprint.get('/api/v1/users')
def users():
    if environ.get('API_KEY') == request.args.get('key'):
        users = User.query.all()
        return jsonify(
            serialize_users(users)
        )
    else:
        return jsonify({'error': 'Invalid API key'}), 401


@blueprint.get('/api/v1/categories')
def categories():
    if environ.get('API_KEY') == request.args.get('key'):
        categories = Category.query.all()
        return jsonify(
            serialize_categories(categories)
        )
    else:
        return jsonify({'error': 'Invalid API key'}), 401


@blueprint.get('/api/v1/article-categories')
def article_categories():
    if environ.get('API_KEY') == request.args.get('key'):
        article_categories = ArticleCategory.query.all()
        return jsonify(
            serialize_article_categories(article_categories)
        )
    else:
        return jsonify({'error': 'Invalid API key'}), 401