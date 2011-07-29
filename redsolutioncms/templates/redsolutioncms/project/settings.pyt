# -*- coding: utf-8 -*-

import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

gettext_noop = lambda s: s

ADMINS = (
#    ('src', 'src@redsolution.ru'),
)

MANAGERS = (
#    ('manager', 'manager@redsolution.ru'),
)

EMAIL_SUBJECT_PREFIX = '[{{ cms_settings.project_name }}]'
DEFAULT_FROM_EMAIL = '{{ cms_settings.default_from_email }}'
SERVER_FROM_EMAIL = DEFAULT_FROM_EMAIL 

DATABASE_ENGINE = '{{ cms_settings.database_engine }}'
{% ifequal cms_settings.database_engine 'sqlite3' %}
DATABASE_NAME = os.path.join(os.path.dirname(os.path.dirname(__file__)), '{{ cms_settings.database_name }}')
{% else %}
DATABASE_NAME = '{{ cms_settings.database_name }}'
{% endifequal %}
DATABASE_USER = '{{ cms_settings.database_user }}'
DATABASE_PASSWORD = '{{ cms_settings.database_password }}'
DATABASE_HOST = '{{ cms_settings.database_host }}'
{% if cms_settings.database_port %}
DATABASE_PORT = '{{ cms_settings.database_port }}'
{% else %}
DATABASE_PORT = ''
{% endif %}

TIME_ZONE = None

LANGUAGE_CODE = 'ru' # Fix me

SITE_ID = 1

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
UPLOAD_DIR = 'upload'

MEDIA_URL = '/media/'
UPLOAD_URL = MEDIA_URL + UPLOAD_DIR

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '{{ secret }}'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = '{{ cms_settings.project_name }}.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
]

TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
]

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'templates'),
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, 'fixtures'),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
]

# Server settings
FORCE_SCRIPT_NAME = ''

CACHE_BACKEND = 'locmem:///?max_entries=5000'

#------------------------------------------------------------------------------
#                       Custom applicaitons settings
#------------------------------------------------------------------------------
