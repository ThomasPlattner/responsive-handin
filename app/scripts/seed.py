from app.app import create_app
from app.articles.models import Article, Category, User
from app.extensions.database import db

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

article_list = [
    {'title': 'Cars', 'icon': '🚗', 'image_name': 'car.png', 'alt': 'Blue oldtimer on a road in a forest'},
    {'title': 'Planes', 'icon': '✈️','image_name': 'plane.png', 'alt': 'Yacht on the ocean'},
    {'title': 'Boats', 'icon': '⛵️','image_name': 'boat.png', 'alt': 'Jumbo Jet from Quantas in the air flying a right-hand turn'},
    {'title': 'Bikes', 'icon': '🚲','image_name': 'bike.jpg', 'alt': 'Bicycle standing against a wall'},
    ]

user_list = [
    {'name': 'Thomas Plattner'},
    ]

category_list = [
    'Motor',
    '4 wheels',
    '>4 wheels',
    'flying',
    '2 wheels',
]

# for post in article_list:
#     new_article = Article(title=post['title'], icon=post['icon'], image_name=post['image_name'], image_alt=post['alt'])
#     db.session.add(new_article)

for person in user_list:
    new_user = User(name=person['name'])
    db.session.add(new_user)

for category in category_list:
    new_category = Category(categories=category)
    db.session.add(new_category)

db.session.commit()