"""
Django settings for personal_website2 project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from django.core.management.utils import get_random_secret_key  
import os
import socket
from pathlib import Path
import json
import cssmin

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

data_path = BASE_DIR / "settings.json"
hostname = socket.gethostname()

def compress_file(filepath, filename):
        fn_name, fn_type = filename.split(".")
        with open(f"{filepath}{fn_name}_uncompressed.{fn_type}", "r") as f:
            file = cssmin.cssmin(f.read())

        with open(f"{filepath}{filename}", "w") as f:
            f.write(file)

def handle_both():
    css_path = "_site/static/css/"
    compress_file(css_path, "base.css")
    compress_file(css_path, "typography.css")

def handle_production():
    "Handle execution to make application production ready"
    os.chdir('/var/www/html/personal_website2/personal_website2-master')
    WSGI_APPLICATION = 'personal_website2.wsgi.application'
    STATIC_ROOT = "/var/www/html/personal_website2/static"

def handle_development():
    pass

with open(data_path, "r", encoding="utf") as f:
    data = json.load(f)

if hostname in data["production_hostnames"] or hostname not in data["development_hostnames"]:
    print("application starting with PRODUCTION settings")
    dsettings = data["production_settings"]
    handle_production()
    handle_both()
else:
    print("application starting with DEVELOPMENT settings")
    dsettings = data["development_settings"]
    handle_development()
    handle_both()



sk = get_random_secret_key()

try:
    data["secret_key"] = sk
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
except PermissionError:
    print("SECRET_KEY = " + sk)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = sk
DEBUG = dsettings["debug"]
ALLOWED_HOSTS = dsettings["allowed hosts"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'django_hosts',

    'aah',
    '_site'
]

MIDDLEWARE = [
    # 'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_hosts.middleware.HostsResponseMiddleware'
]

ROOT_URLCONF = 'personal_website2.urls'

ROOT_HOSTCONF = 'personal_website2.hosts'
DEFAULT_HOST= 'www'


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
]

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
