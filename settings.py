# Django settings for snipollector project.

SNIPPETS_PAGINATE_BY = 13
SNIPPETS_HTTP_HOST   = u'localhost'
SNIPPETS_HTTP_PORT   = u':8000'

import os.path
PROJECT_ROOT = os.path.dirname(__file__)
SNIPPET_APPL = 'snippets'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Felix Morgner', 'felix@felixmorgner.ch'),
)

MANAGERS = ADMINS

DATABASE_ENGINE   = 'sqlite3'
DATABASE_NAME     = 'database'
DATABASE_USER     = ''
DATABASE_PASSWORD = ''
DATABASE_HOST     = ''                                                                                                      
DATABASE_PORT     = ''                                                                                                      

TIME_ZONE = 'Europe/Zurich'

LANGUAGE_CODE = 'de'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join( PROJECT_ROOT, 'site-media')
# MEDIA_URL  = u'http://%s%s/%s' % (SNIPPETS_HTTP_HOST, SNIPPETS_HTTP_PORT, 'site-media',)
MEDIA_URL  = u'/site-media/'

LOGIN_REDIRECT_URL = '/'
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '()e%6g67)ai1hv%ny_lds45=c*a7^7&)yh!*2r(aidkt#8cbzp'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
		'syntax_colorize',
    SNIPPET_APPL,
)

SESSION_COOKIE_AGE = 6000 * 2
