import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-e=ntyf%a5#*zckik=m-0#)j15&e^9ph^de@&dh_h*z(riucc1j'

DEBUG = True


ALLOWED_HOSTS = []




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # third
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'import_export',


    # own

    "account",

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS=[BASE_DIR,"static"]

MEDIA_ROOT=os.path.join(BASE_DIR,"media")
MEDIA_URL="/media/"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'






# customized

AUTH_USER_MODEL="account.User"


REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_RATES": {
        "register": "4/min",
    },

}







# kavenegar

KAVEHNEGAR_KEY='71456537783936513335477935536F64584334596C3639424C6143474C48767536696F7A364558395A34633D'
SENDER_NUMBER='09981000176'
KAVEHNEGAR_CUSTOM_TEMPLATE_MYSELF_VAR = 'Identification'



