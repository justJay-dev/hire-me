import os
import platform
import pygments, markdown
from flask import render_template_string
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from app import debug


#setup articles, this is where you can do code highlight templates and stuff.
def the_markdown(text):
    markdown_text = render_template_string(text)
    pygmented_text = markdown.markdown(markdown_text, extensions=FLATPAGES_MARKDOWN_EXTENSIONS)
    return pygmented_text


def get_url():
    if debug == True:
        return 'http://test-url'
    else:
        return 'https://production-url'


def gen_connection_string():
    if debug == True:
        #local
        return 'your development connection string'
    else:
        #not local
        return 'your production connection string'

BLOG_NAME = 'blog name'
APP_URL = get_url()

SECRET_KEY = 'GOOD_SECRET_KEY'

TARGET_MAILBOX = 'where_you_want@emails_to_go'
GEOIPIFY_API_KEY='GEOIPKEY'

FLATPAGES_EXTENSION = '.md'
FLATPAGES_HTML_RENDERER = the_markdown
FLATPAGES_MARKDOWN_EXTENSIONS = [
    'codehilite', 
    'tables', 
    'fenced_code', 
    'md_in_html',
    'wikilinks',
    'smarty'
    ]
    
SQLALCHEMY_DATABASE_URI = gen_connection_string()
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size': 15,
    'max_overflow': 2,
    'pool_timeout': 30,
    'pool_recycle': 1800,
    'pool_pre_ping': True
}

MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEBUG = '1'
MAIL_USERNAME = "apikey"
MAIL_PASSWORD = "your_sendgrid_password"
MAIL_DEFAULT_SENDER = 'your_default_sender'
MAIL_MAX_EMAILS = 'None'
MAIL_ASCII_ATTACHMENTS = 'False'