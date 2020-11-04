#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = 'Meven Lennon-Bertrand'
SITENAME = 'Meven Lennon-Bertrand'
SITEURL = 'https://www.meven.ac'

PATH = 'content'
STATIC_PATHS = ['documents','images']

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['i18n_subsites', 'pin_to_top', 'dateish','add_cname']
JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.i18n']
}

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%B %Y'

DEFAULT_LANG = 'en'
LOCALE = 'en_GB.utf8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
#SOCIAL = (('GitHub', 'https://github.com/MevenBertrand'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Remove tag-related stuff
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

#Theme
THEME = "themes/green-notmyidea"

#Internationalization

I18N_SUBSITES = {
    'fr': {'LOCALE': 'fr_FR.utf8',},
    }

#Dates

DATEISH_PROPERTIES = ['start','end']

#Authors webpage
author_webpage = {
             "Nicolas Tabareau": "http://tabareau.fr",
             "Éric Tanter": "https://pleiad.cl/people/etanter",
             "Hugo Herbelin": "http://pauillac.inria.fr/~herbelin/",
             "Jurriaan Rot": "http://jurriaan.me/",
             "Meven Lennon-Bertrand": '',
             "Kenji Maillard": "https://kenji.maillard.blue/",
             }

def lookup_author_webpage(author):
  return author_webpage[author.name]

#def is_publication(article):
#  return(article.category == "Publications")

JINJA_FILTERS = {
             'lookup_author_webpage': lookup_author_webpage,
             }

#JINJA_TESTS = {
#            'publication': is_publication,
#}