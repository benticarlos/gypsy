"""
Django settings for gypsy project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!eq3tl+4)l7ra-q9q8lvk9d2o#oh@%_=97&!frf_1alp7vor!s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

## Email Configs, similar zendry
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'benticarlos.ucg@gmail.com'
EMAIL_HOST_PASSWORD = 'Info2002'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#### desbloquear captcha
# https://accounts.google.com/displayunlockcaptcha



# Application definition

INSTALLED_APPS = [
    #apps django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites', #activar como SITE_ID=1 , mas abajo
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps terceros
    # sudo pip install --upgrade django-crispy-forms
    # python manage.py makemigrations 
    #luego
    # python manage.py migrate
    # configurar el bootstrap 3 mas abajo CRISPY_TEMPLATE_PACK
    'crispy_forms',
    'registration',
    #mis apps
    'boletin'
]

########## Self configs of 3th party
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True # hacer el migrate. Ver arriba
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

###Crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gypsy.urls' # dentro del directorio /src

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #se debe agregar para informar al django donde van las plantillas
        'DIRS': [os.path.join(BASE_DIR, "templates")], 
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

WSGI_APPLICATION = 'gypsy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
#/static/img/img1.jpg

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_pro", "static"),
    # '/var/www/static/',
]

# donde seran enviados los staticfiles_dirs, codigo anterior (para produccion)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_env", "static_root")

#donde van las fotografias de usuarios
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_env", "media_root")
