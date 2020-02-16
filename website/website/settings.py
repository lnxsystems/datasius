"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT_DIR = Path(BASE_DIR).parent.as_posix()
DBPATH =  os.path.join(BASE_DIR, "data",'db.sqlite3')
STATIC_ROOT = os.path.join(PARENT_DIR, "data","static_root")
STATIC_DIR = os.path.join(BASE_DIR,"website","static")
TEMPLATE_DIR=os.path.join(BASE_DIR,"templates")

print("="*80)
print("BASE_DIR: {}".format(BASE_DIR))
print("PARENT_DIR: {}".format(PARENT_DIR))
print("DBPATH: {}".format(DBPATH))
print("STATIC_ROOT: {}".format(STATIC_ROOT))
print("STATIC_DIR: {}".format(STATIC_DIR))
print("TEMPLATE_DIR: {}".format(TEMPLATE_DIR))
print("="*80)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(e3c+6a@&$t&0yii#5w$#0&r*@ec554=z#_k=q+hk5eh7@4^v4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


STATIC_ROOT = os.path.join(PARENT_DIR, "static_root")
print("STATIC_ROOT: {}".format(STATIC_ROOT))


if (not Path(STATIC_ROOT).exists()):
    #create it.
    Path(STATIC_ROOT).mkdir()

elif Path(STATIC_ROOT).is_file():
    #This should not occur! We bail out.
    msg = "{} is not a directory! We need this as a directory. Please remove and restart."
    print(msg.format(STATIC_ROOT))
    sys.exit(-1)

ASSETS_DIR = os.path.join(PARENT_DIR, "assets")

if (not Path(ASSETS_DIR).exists()):
    #create it.
    Path(ASSETS_DIR).mkdir()

elif Path(ASSETS_DIR).is_file():
    #This should not occur! We bail out.
    msg = "{} is not a directory! We need this as a directory. Please remove and restart."
    print(msg.format(STATIC_ROOT))
    sys.exit(-1)








# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    #'django-registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DBPATH,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# Static files not tied to a particular app.
STATICFILES_DIRS = (
    os.path.join(STATIC_DIR),
)



if (not Path(STATIC_ROOT).exists()):
    #create it.
    Path(STATIC_ROOT).mkdir()

elif Path(STATIC_ROOT).is_file():
    #This should not occur! We bail out.
    msg = "{} is not a directory! We need this as a directory. Please remove and restart."
    print(msg.format(STATIC_ROOT))
    sys.exit(-1)

#EMAIL configuration. We use google smtp here for now

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='datasius@gmail.com'
EMAIL_HOST_PASSWORD ='r4bb1tMQ2020!'


#django-registration configurations

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window



