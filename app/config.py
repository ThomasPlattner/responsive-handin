from dotenv import load_dotenv
from os import environ

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

ARTICLES_PER_PAGE = 4

# UPLOADS_FOLDER = 'static/images/upload'

# MAX_CONTENT_LENGTH = 4 * 1024 * 1024

# UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif', '.svg']