#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alexander Valdez Portocarrero'
SITENAME = u'Alex@nderV.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DEFAULT_DATA_FORMAT= '%A %d %B %Y'

#Static paths will be copied without parsing thero
STATIC_PATHS= ['images','extra']

#Shift the installed location of a file
EXTRA_PATH_METADA={ 'extra/CNAME':{'path','CNAME'}}

#Extract post date from filename
FILENAME_METADA= '(?P<date>\d{4}-\d{2}-\d{2})'

#Sole author and don't  use categories... dis
AUTHOR_SAVE_AS= False
AUTHORS_SAVE_AS=False
CATEGORY_SAVE_AS=False
CATEGORIES_SAVE_AS=False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#URL settings
#Uncomment following line if you want documente-relative URLSs when developing
RELATIVE_URLS = True
ARTICLE_URL='{slug}.html'
PAGE_URL ='{slug}.html'
PAGE_SAVE_AS='{slug}.html'
TAG_URL='tag-{slug}.html' 
TAGE_SAVE_AS='tag-{slug}.html'
TAGS_URL='tags.html'
TAGS_SAVE_AS='tags.html'
ARCHIVES_URL='archives.html'
ARCHIVES_SAVE_AS='archives.html'

#Contact
EMAIL_ADDR= 'alex.valdezp22 at gmail dot com'

#Plugins
PLUGIN_PATH='/home/alex/pelican_plugins/pelican-plugins'
PLUGINS=['neighbors']

#Theme
THEME='/home/alex/pelican_themes/pelican-themes/pelican-bootstrap3'
WHOAMI_URL='/home/alex/Pictures/pelican_images/whoami.jpg'
GREETING= 'Howdy!'
#LICENCE_NAME='BY-NC-SA'
#LICENCE_URL='http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US'
#LICENCE_URL_IMG='http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png'
JINJA_EXTENSIONS=['jinja2.ext.loopcontrols']

#Social
TWITTER_URL='https://twitter.com/alexvaldez900'
GITTHUB_URL='https://github.com/alexvaldez24'

#Tag cloud
TAG_CLOUD_STEPS = 4

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
