#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The Python Astrodynamics Developers'
SITENAME = 'Python Astrodynamics'
# SITEURL = 'http://www.python-astrodynamics.org'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Github', 'https://github.com/python-astrodynamics/astrodynamics'),
    ('Issues', 'https://github.com/python-astrodynamics/astrodynamics/issues'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
)

# # Social widget
SOCIAL = ()
BANNER = 'images/spacexlaunch.jpeg'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/bootstrap3'
BOOTSTRAP_THEME = 'flatly'

