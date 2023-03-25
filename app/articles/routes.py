from flask import Blueprint, render_template

blueprint = Blueprint('articles', __name__)

article_list = [
    {'title': 'Cars', 'icon': '🚗', 'image_name': 'car.png', 'alt': 'Blue oldtimer on a road in a forest"'},
    {'title': 'Planes', 'icon': '✈️','image_name': 'plane.png', 'alt': 'Yacht on the ocean'},
    {'title': 'Boats', 'icon': '⛵️','image_name': 'boat.png', 'alt': 'Jumbo Jet from Quantas in the air flying a right-hand turn'},
    {'title': 'Bikes', 'icon': '🚲','image_name': 'bike.jpg', 'alt': 'Bicycle standing against a wall'},
    ]

@blueprint.route('/blog/<slug>')
def blog(slug):
    articles = article_list
    for article in article_list:
        if slug.title() == article['title']:
            url = "articles/" + slug.lower() + ".html"
            return render_template(url)
            break
    else:
        message = "Sorry, we couldn't find the article about " + slug + " :( "
        return render_template('/base.html', message=message) 
