"""
Django settings for time_reg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w+(6y+i1_n4%(%rl37n*1__+shp9h933$ob(b6r++hg%&!_muh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

PROJECT_APPS = (
    'app',
    'app.profile',
)

THIRD_PARTY_APPS = (
    'django_extensions',
    'pipeline',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

TEMPLATE_DIRS = (
    'time_reg/templates',
)

ROOT_URLCONF = 'time_reg.urls'

WSGI_APPLICATION = 'time_reg.wsgi.application'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'


# Static files

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE_CSS = {
    'style': {
        'source_filenames': (
          'bootstrap/css/bootstrap-theme.css',
          'bootstrap/css/bootstrap.css',
          'scripts/bower_components/angular/angular-csp.css',
          'bootstrap-editable.css',
          'timereg/css/time_reg.css',
          'xeditable/css/xeditable.css',
          'bower_components/angularjs-toaster/toaster.css',
        ),
        'output_filename': 'style.css'
    },
}

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
          'bower_components/angular/angular.js',
          'django_extensions/js/*.js',
          'moment.min.js',
          'bower_components/angular-xeditable/dist/js/xeditable.js',
          'bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js',
          'main.js',
          'bower_components/angular-animate/angular-animate.js',
          'bower_components/angularjs-toaster/toaster.js',
          'scripts/*.js',
          'notify/notify.js',
          'bootstrap/js/bootstrap.js',
        ),
        'output_filename': 'scripts.js',
    }
}
