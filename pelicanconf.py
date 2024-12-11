#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Remove output directory on re-generation

DELETE_OUTPUT_DIRECTORY = False

# AUTHOR =
SITEAUTHOR = "Meven Lennon-Bertrand"
SITENAME = 'Meven Lennon-Bertrand'
SITEURL = "http://localhost:8000"

PATH = 'content'
STATIC_PATHS = ['documents','images']

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['i18n_subsites', 'pin_to_top', 'dateish','add_cname','category-custom-order']
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
SOCIAL = (
  ('github', 'https://github.com/MevenBertrand'),
  ('mastodon','https://lipn.info/@mevenlennonbertrand'),
  ('stack-exchange','https://proofassistants.stackexchange.com/users/367/meven-lennon-bertrand'),
  ('orcid','https://orcid.org/0000-0002-7079-8826')
)

ACADEMIA = (
  ('zenodo','https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Lennon-Bertrand%2C%20Meven%22&l=list&p=1&s=10&sort=bestmatch'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Remove tag-related stuff
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

#Theme
THEME = "themes/pelican-svbhack"
USER_LOGO_URL = "moi.jpg"
ROUND_USER_LOGO = True
MYNAME = "Meven <br> Lennon-Bertrand"
TAGLINE = "Postdoc in Computer Science <br> University of Cambridge"
EMAIL = "Meven.Lennon-Bertrand[at]cl.cam.ac.uk"
SOURCE = "https://github.com/MevenBertrand/MevenBertrand.github.io/"

#Category order

CATEGORIES_CUSTOM_ORDER = [
    'About',
    'Publications',
    'Talks',
    'Formalisations',
    'Teaching',
    'Dissemination',
    'PhD Thesis',
]

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
             "Meven Lennon-Bertrand": 'https://www.meven.ac',
             "Kenji Maillard": "https://kenji.maillard.blue/",
             "Matthieu Sozeau": "https://sozeau.gitlabpages.inria.fr/www/",
             "Yannick Forster": "https://yforster.github.io/",
             "The MetaCoq Team": "https://metacoq.github.io/#team--credits",
             "Pierre-Marie Pédrot": "https://www.pédrot.fr/",
             "Arthur Adjedj": "https://github.com/arthur-adjedj",
             "Loïc Pujet": "https://pujet.fr",
             "Jakob Botch Nielsen": "https://jakobbotsch.com/",
             "Théo Winterhalter": "https://theowinterhalter.github.io/",
             "Neel Krishnaswami": "https://www.cl.cam.ac.uk/~nk480/",
             "Théo Laurent": "https://www.theolaurent.fr/",
             "Arthur Adjedj": "https://github.com/arthur-adjedj",
             "Matthew Sirman": "https://github.com/matthew-sirman",
             }

def lookup_author_webpage(author):
  return author_webpage[author.name]

#def is_publication(article):
#  return(article.category == "Articles")

JINJA_FILTERS = {
             'lookup_author_webpage': lookup_author_webpage,
             }

#JINJA_TESTS = {
#            'publication': is_publication,
#}