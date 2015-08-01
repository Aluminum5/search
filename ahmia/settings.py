"""Django project settings for ahmia."""
import os
import sys

# Set the PROJECT_HOME variable.
# This will be used to prepend to all file/directory paths.
PROJECT_HOME = os.path.join(os.getcwd(), 'ahmia')

# Define DEBUG state dynamically:
# If running server using manage.py => DEBUG = True else DEBUG = False
if 'runserver' in sys.argv or 'test' in sys.argv:
    DEBUG = True
    # In demo environment use this YaCy address
    YACY = "http://localhost:8888/"
else:
    # This is the YaCy address in the ahmia.fi
    YACY = "http://10.8.0.10:8090/"
    DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.ahmia.fi', # Allow domain and subdomains
    '.ahmia.fi.', # Also allow FQDN and subdomains
    '.msydqstlz2kzerdg.onion',
    '.msydqstlz2kzerdg.onion.',
    'localhost',
    '127.0.0.1',
]

demo_env = ['runserver', 'sqlflush', 'syncdb', 'loaddata', 'shell', 'flush',
'migrate', 'dumpdata', 'rebuild_index']

if 'test' in sys.argv:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Database engine
        'NAME': os.getcwd() + '/ahmia_db_test', # Database name
        }
    }
elif [cmd for cmd in demo_env if cmd in sys.argv]:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Database engine
        'NAME': os.getcwd() + '/ahmia_db', # Database name
        }
    }
else: # Production environment
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Database engine
        'NAME': 'ahmia_db',              # Database name
        'USER': 'ahmia_login',           # Not used with sqlite3.
        'PASSWORD': 'nakataP01Svaa',     # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost.
        'PORT': '6432', # pbbouncer port
        }
    }

SOLR_ADDRESS = "http://127.0.0.1:33433/solr"
PROXY_BASE_URL = 'http://localhost:9200/'

HAYSTACK_CONNECTIONS = {
    'default': {
        #'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'ENGINE': 'ahmia.solr_grouping_backend.GroupedSolrEngine',
        'URL': SOLR_ADDRESS,
        'INCLUDE_SPELLING': True,
    },
}

# Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'example@lol.fi'
EMAIL_HOST_PASSWORD = 'well_I_am_not_pushing_it_to_git'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
RECIPIENT_LIST = [DEFAULT_FROM_EMAIL]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

STATIC_URL = '/media/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
STATIC_ROOT = PROJECT_HOME+'/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%*ertqgmh3(t_d=i&ojuc!02wnech_nq#1*s7dbv3h=&ruf7*b'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'ahmia.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_HOME, 'templates'),
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'ahmia',
    'haystack',
)
