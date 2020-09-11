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

BLOG_NAME = 'blog name'
APP_URL = get_url()
SECRET_KEY = 'GOOD_SECRET_KEY'


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
    

