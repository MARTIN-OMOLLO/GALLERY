import os
import django_heroku
# from decouple import config,Csv
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# MODE=config("MODE", default="dev")
MODE="dev"
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'django-insecure-8m*z0b91om85k!sgjnr_*1uccu+szolkf@fu8149!oq#6i$qp1'
DEBUG = os.environ.get('DEBUG', True)
# development
DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'tgallery',
           'USER': 'martin',
           'PASSWORD':'martin@123',
            
             }
       
   }
# if config('MODE')=="dev":
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2',
#            'NAME': config('DB_NAME'),
#            'USER': config('DB_USER'),
#            'PASSWORD': config('DB_PASSWORD'),
#            'HOST': config('DB_HOST'),
#            'PORT': '',
#        }
       
#    }
# # production
# else:
#    DATABASES = {
#        'default': dj_database_url.config(
#            default=config('DATABASE_URL')
#        )
#    }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
ALLOWED_HOSTS=[]
"""
Django settings for gallery project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see.
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see.
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.

#.........
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Configure Django App for Heroku.



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-8m*z0b91om85k!sgjnr_*1uccu+szolkf@fu8149!oq#6i$qp1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'GALLERY.apps.GalleryConfig',
    'cloudinary',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'gallery.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'gallery.wsgi.application'


# Database.
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True

django_heroku.settings(locals())


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),

)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# adding config
cloudinary.config( 
  cloud_name = "drnrh0spo", 
  api_key = "921676172689963", 
  api_secret = "ZlJCPPe0gVA4sHzLC4y-rlPld7A" 
)
