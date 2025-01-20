"""Flask configuration."""
import os
class Config:
    """Base config. uses local database server."""
    SECRET_KEY=os.getenv('SECRET_KEY')
    # SECRET_KEY='YOURSECRETKEY'
    FLASK_DEBUG = True
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'