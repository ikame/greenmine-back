# -*- coding: utf-8 -*-

import os.path, sys, os
import djcelery

from django.utils.translation import ugettext_lazy as _

djcelery.setup_loader()

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
)

OUT_PROJECT_ROOT = os.path.abspath(
    os.path.join(PROJECT_ROOT, "..")
)

APPEND_SLASH = False


ADMINS = (
    ('Andrei Antoukh', 'niwi@niwi.be'),
)

LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
    ('ru', _('Russian')),
)



MANAGERS = ADMINS

DISABLE_REGISTRATION = False
DEFAULT_TASK_PARSER_RE = "^\s*Task\:(.+)$"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'greenmine',
    }
}

# CACHE CONFIG
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SEND_BROKEN_LINK_EMAILS = True
IGNORABLE_404_ENDS = ('.php', '.cgi')
IGNORABLE_404_STARTS = ('/phpmyadmin/',)

ATOMIC_REQUESTS = True

TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
LOGIN_URL='/auth/login/'
USE_TZ = True

#SESSION BACKEND
SESSION_ENGINE='django.contrib.sessions.backends.db'
#SESSION_ENGINE='django.contrib.sessions.backends.cache'
#SESSION_EXPIRE_AT_BROWSER_CLOSE = False
#SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 1209600 # (2 weeks)
SESSION_HEADER_NAME = "HTTP_X_SESSION_TOKEN"

API_LIMIT_PER_PAGE = 0

HOST = 'http://localhost:8000'

# MAIL OPTIONS
#EMAIL_USE_TLS = False
#EMAIL_HOST = 'localhost'
#EMAIL_HOST_USER = 'user'
#EMAIL_HOST_PASSWORD = 'password'
#EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = "niwi@niwi.be"
EMAIL_BACKEND = 'djmail.backends.default.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DJMAIL_REAL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DJMAIL_SEND_ASYNC = False
DJMAIL_MAX_RETRY_NUMBER = 3
DJMAIL_TEMPLATE_EXTENSION = 'jinja'

# Message System
#MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(OUT_PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(OUT_PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Don't forget to use absolute paths, not relative paths.
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

SECRET_KEY = 'aw3+t2r(8(0kkrhg8)gx6i96v5^kv%6cfep9wxfom0%7dy0m9e'

TEMPLATE_LOADERS = [
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'greenmine.base.middleware.GreenmineSessionMiddleware',
    'greenmine.base.middleware.CoorsMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'reversion.middleware.RevisionMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
]

ROOT_URLCONF = 'greenmine.urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

INSTALLED_APPS = [
    'grappelli.dashboard',
    'grappelli',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    'greenmine.base',
    'greenmine.base.notifications',
    'greenmine.base.users',
    'greenmine.base.mail',
    'greenmine.base.searches',
    'greenmine.projects',
    'greenmine.projects.milestones',
    'greenmine.projects.userstories',
    'greenmine.projects.tasks',
    'greenmine.projects.issues',
    'greenmine.projects.questions',
    #'greenmine.projects.documents',
    'greenmine.projects.wiki',

    'south',
    'haystack',
    'reversion',
    'rest_framework',
    'djmail'
]

WSGI_APPLICATION = 'greenmine.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s:%(asctime)s:%(module)s %(message)s'
        },
        'null': {
            'format': '%(message)s',
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'null',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'main': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}


AUTH_USER_MODEL = 'users.User'
FORMAT_MODULE_PATH = 'greenmine.base.formats'
DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y', '%b %d %Y',
    '%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y',
    '%B %d, %Y', '%d %B %Y', '%d %B, %Y'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
)

ANONYMOUS_USER_ID = -1

GRAPPELLI_INDEX_DASHBOARD = 'greenmine.dashboard.CustomIndexDashboard'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), '../search/index'),
    },
}

HAYSTACK_DEFAULT_OPERATOR = 'AND'

MAX_SEARCH_RESULTS = 100

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'greenmine.base.users.auth.SessionAuthentication',
    ),
    'FILTER_BACKEND': 'greenmine.base.filters.FilterBackend',
    'PAGINATE_BY': 50,
    'MAX_PAGINATE_BY': 1000,
    'VIEW_DESCRIPTION_FUNCTION': 'rest_framework_apidoc.apidoc.get_view_description',
}
APIDOC_DEFAULT_DOCUMENTER_CLASSES = ['rest_framework_apidoc.apidoc.RSTFilesDocumenter']
APIDOC_DOCUMENTATION_PATH = "greenmine/apidoc"

from .appdefaults import *


# NOTE: DON'T INSERT MORE SETTINGS AFTER THIS LINE

# Test conditions
if 'test' in sys.argv:
    if "settings" not in ",".join(sys.argv):
        print ("\033[1;91mNot settings specified.\033[0m")
        print ("Try: \033[1;33mpython manage.py test --settings="
               "greenmine.settings.testing -v2\033[0m")
        sys.exit(0)
