"""
This is the config file for the application.
"""
import os

class Config:
    """
    This is the base configuration class for the application.

    Attributes:
        SECRET_KEY: The secret key for the application.
        SQLALCHEMY_TRACK_MODIFICATIONS: This is set to False to prevent
        the app from tracking modifications.
        SQLALCHEMY_RECORD_QUERIES: This is set to True to enable recording of queries.
        SQLALCHEMY_DATABASE_URI: The URI for the database.
        WTF_CSRF_ENABLED: This is set to True to enable CSRF protection.
    """
    m_key = '341814e8a436dce5e79bd2a4014b1ac56a3b04eac32998a48e7ea232c19dc95b'
    SECRET_KEY = os.environ.get('SECRET_KEY') or m_key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    WTF_CSRF_ENABLED = True
    UPLOAD_FOLDER = 'app/static/uploads'

class TestConfig(Config):
    """
    This is the configuration class for the development environment.

    Attributes:
        DEBUG: This is set to True to enable debugging.
        SQLALCHEMY_DATABASE_URI: The URI for the test database.
        WTF_CSRF_ENABLED: This is set to False to disable CSRF protection.
        TESTING: This is set to True to enable testing mode.
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    WTF_CSRF_ENABLED = False
