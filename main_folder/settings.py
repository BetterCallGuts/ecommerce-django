from pathlib import Path;
import os
BASE_DIR = Path(__file__).resolve().parent.parent;
SECRET_KEY = 'django-insecure-@g-f-rw$%ajjg0+!7ttins!x6y40-+=m@+%=$=zt25)hhuc21j';

DEBUG = True;
ALLOWED_HOSTS = ['*'];
LOGIN_URL           =  '/login';
LOGIN_REDIRECT_URL  =  '/';
LOGOUT_REDIRECT_URL =  '/';
INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'dashboard',
    'item',
    'conversation',
    'import_export',
    'Car',
    "rest_framework",
    'api',
    'rest_framework_xml',
    "corsheaders"

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware"
];ROOT_URLCONF = 'main_folder.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
];WSGI_APPLICATION = 'main_folder.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
};AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
];
LANGUAGE_CODE = 'en-us';
TIME_ZONE = 'UTC';
USE_I18N = True;
USE_TZ = True;
STATIC_URL = 'static/';
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main_folder/static')]
STATIC_ROOT      = os.path.join(BASE_DIR, 'static')

MEDIA_URL  = 'media/'

REST_FRAMEWORK = {
  'DEFAULT_PARSER_CLASSES': (
      "rest_framework.parsers.JSONParser",
    'rest_framework_xml.parsers.XMLParser',
  ),
    'DEFAULT_RENDERER_CLASSES': (
    'rest_framework.renderers.BrowsableAPIRenderer',
     'rest_framework.renderers.JSONRenderer',
    'rest_framework_xml.renderers.XMLRenderer',
  ),}

CORS_ORIGIN_ALLOW_ALL = True
MEDIA_ROOT = BASE_DIR / 'media';
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'