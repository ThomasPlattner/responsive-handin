from flask import Flask, redirect, url_for, render_template
from . import articles, general_pages, manage, api, users
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask):
    app.register_blueprint(articles.routes.blueprint)
    app.register_blueprint(general_pages.routes.blueprint)
    app.register_blueprint(manage.routes.blueprint)
    app.register_blueprint(api.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)

# Database
def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)