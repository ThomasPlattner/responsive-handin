# Foundations Handin - Thomas' Blog

## Description
The foundations handin is a personal blog. It has the following general pages:
- Index: overview of blog articles
- Contact: How to contact the author
- About: More info about the author
- Categories: Overview of blog articles seperated into different categories

The main parts are articles. For test purposes, there are four placeholder articles so far:
- Cars
- Boats
- Planes
- Bikes

The articles were hardcoded until now and will transition into the database and rendered from there next week. Further articles will be added to the database through HTML forms.

## Technologies used:
1. **Frontend**
    - HTML
    - CSS

2. **Backend**
    - Flask
    - jinja2 Templates

3. **Database**
    - SQLite/SQLAlchemy
        
        Models: 
        - User (admin and author of articles)
        - Article (table of blog articles)
        - Category (of article)
        - ArticleCategory (Connectortable for displaying categories of articles)

## Instructions for running app locally
1. Clone repository to local branch: 
    git clone {{ github repo URL }}
2. Install a virtual environment: 
    python3 -m venv venv
3. Activate virtual environment: 
    source venv/bin/activate
4. Install packages from requirements.txt: 
    python -m pip install -r requirements.txt
5. Add .env file to project root with the following code:
    FLASK_DEBUG=True
    DATABASE_URL=sqlite:///database.db
    FLASK_APP=run.py
6. Initialize, migrate and create database:
    flask db init
    flask db migrate -m "{{ name of migration }}
    flask db upgrade
7. Fill database with entries (rows):
    python -m app.scripts.seed
8. Run app:
    python run.py

0. Run tests:
    pytest -v

## Upcoming features
- contact form
- Intro to the author in /about
- more media queries for articles and other sites
- Categories of articles (placeholders for development purposes; e.g., vehicles, 2 wheels, 4 wheels, >4 wheels, ...)
- Articles created through HTML forms
- Articles stored in database and rendered with HTML templates