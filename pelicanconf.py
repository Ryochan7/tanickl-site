#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tanickl'
SITENAME = u'Travis Nickles'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = ['index']
THEME = "themes/portfolio"
ARTICLE_URL = "blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"
PAGE_URL = "{parent_dir}{slug}/"
PAGE_SAVE_AS = "{parent_dir}{slug}/index.html"
#SITEURL = "http://localhost:8000"
SITEURL = "https://ryochan7.github.io/tanickl-site"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
