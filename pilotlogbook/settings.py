
from pathlib import Path
import os
from decouple import config
import dj_database_url


# SECRET_KEY = con'django-insecure-l93ghg^s#vehdg7kc#9bh(q5vbx&7o^6lg_qsku#h#3q547rp9'

# DEBUG = True



# DATABASE_URL="postgresql://postgres:zbePzzNAauboABuuIGwybYjgtjFbKqpW@maglev.proxy.rlwy.net:33291/railway"

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['pilotrep-production.up.railway.app','127.0.0.1']



INSTALLED_APPS = [
   'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'logbook2',#..................                  also add  rest framwork
    'rest_framework',
    'corsheaders',

       
]

MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pilotlogbook.urls'

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

WSGI_APPLICATION = 'pilotlogbook.wsgi.application'






DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'railway',
    #     'HOST': 'postgres.railway.internal',
    #     'PASSWORD':'SbndEbEIYGftYigLQcEpwHcTccDvAQUh',
    #     'PORT':'5432',
    #     'USER':'postgres',

    # }

#    'default': dj_database_url.config(default=DATABASE_URL,conn_max_age=1800)     # (This will take database credentials from environment variables)
     'default': dj_database_url.config(default=config('DATABASE_URL'), conn_max_age=1800)  


}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORS_ALLOWED_ORIGINS =  [
#     "http://localhost:3000",
# ]

CORS_ALLOW_ALL_ORIGINS = True

AUTH_USER_MODEL = 'logbook2.User'  # for def

