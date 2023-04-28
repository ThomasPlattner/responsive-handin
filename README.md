# Foundations Handin - Thomas' Blog

## Description
The foundations handin is a personal blog. It has the following general pages:
- Index: overview of blog articles
- Contact: How to contact the author
- About: More info about the author
- Categories: Overview of blog articles seperated into different categories

The main parts are articles. There is a script loading four articles by default:
- Cars
- Boats
- Planes
- Bikes

For creating new articles, a user has to be logged in. After logging in, a button in the top navbar appears which leads to an interface to manage articles.
Now the user can create, edit and delete articles.

Every article can be assigned to a list of category tags. When creating or editing an article, the categories can be updated. For creating, updating and deleting new categeries, there is one form accessible through the manage articles interface.

As of this point, there are three areas where there is client-side JavaScript. One removes the top navbar menu items and replaces it with a hamburger menu for phone screens (<576px screen width). The second one allows to read articles in darkmode. The third one is in the category management interface and saves categories once the user removes the focus away from the field.


## Technologies used:
1. **Frontend**
    - HTML
    - CSS
    - JavaScript

2. **Backend**
    - Flask
    - jinja2 Templates

3. **Database**
    - SQLite/SQLAlchemy locally
    - PostgreSQL for deployment
        
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

## Changelog
- added styles for manage articles interface
- improved form to manage categories
- repaired many-to-many relationship between Article and Category model
- form when creating articles can display existing data from the database as default input to edit the article
- authentication


## Upcoming features
- contact form
- Intro to the author in /about
- remove /category page and add filter form on index to bundle /index and /categories