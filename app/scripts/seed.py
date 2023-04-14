from app.app import create_app
from app.articles.models import Article, Category, User
from app.extensions.database import db

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

article_list = [
    {'title': 'Cars', 'icon': '🚗', 'user_id':'1', 'image_name': 'car.png', 'image_alt': 'Blue oldtimer on a road in a forest', 'text':'cars tires doors - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam augue enim, semper ornare semper eget, facilisis non leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin mollis eu ex in maximus. Proin ultricies eros ac est facilisis, in cursus ante tincidunt. Aliquam tincidunt lectus porta lacus'},
    {'title': 'Boats', 'icon': '⛵️', 'user_id':'2', 'image_name': 'boat.png', 'image_alt': 'Yacht on the ocean', 'text':'Boats boats boats - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam augue enim, semper ornare semper eget, facilisis non leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin mollis eu ex in maximus. Proin ultricies eros ac est facilisis, in cursus ante tincidunt. Aliquam tincidunt lectus porta lacus'},
    {'title': 'Planes', 'icon': '✈️', 'user_id':'1', 'image_name': 'plane.png', 'image_alt': 'Jumbo Jet from Quantas in the air flying a right-hand turn', 'text':'747 737 727 757 767 787 717 707 Clipper - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam augue enim, semper ornare semper eget, facilisis non leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin mollis eu ex in maximus. Proin ultricies eros ac est facilisis, in cursus ante tincidunt. Aliquam tincidunt lectus porta lacu'},
    {'title': 'Bikes', 'icon': '🚲', 'user_id':'2', 'image_name': 'bike.jpg', 'image_alt': 'Bicycle standing against a wall', 'text':"Coming soon 🚧"},
    ]

user_list = [
    {'name': 'Thomas Plattner'},
    {'name': 'Anonymous'}
    ]

category_list = [
    'Motor',
    '4 wheels',
    '>4 wheels',
    'flying',
    '2 wheels',
]

for post in article_list:
    new_article = Article(title=post['title'], icon=post['icon'], image_name=post['image_name'], image_alt=post['image_alt'], user_id=post['user_id'], text=post['text'])
    db.session.add(new_article)

for person in user_list:
    new_user = User(name=person['name'])
    db.session.add(new_user)

for category in category_list:
    new_category = Category(categories=category)
    db.session.add(new_category)

db.session.commit()