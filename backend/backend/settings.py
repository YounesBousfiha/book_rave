from pathlib import Path
from datetime import timedelta
import environ
import os
# Import dj-database-url at the beginning of the file.
import dj_database_url

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if env('DEBUG') == 'true' else False

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')

# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    'rest_framework.authtoken',
    'djoser',
    'rest_framework_simplejwt.token_blacklist',  # this one is for the logout
    'corsheaders',

    "comment.apps.CommentConfig",
    "favorite.apps.FavoriteConfig",
    "vote.apps.VoteConfig",
    "user.apps.UserConfig",
    "book.apps.BookConfig",
    "review.apps.ReviewConfig",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if env('PRODUCTION') == 'yes':
    DATABASES = {
        'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgres://younes_dev:qGgu4b0Po35BfCy9dk6AoVKtGIQx5XAz@dpg-cnv27qf79t8c73d4s630-a.frankfurt-postgres.render.com/my_db_7ns2',
        conn_max_age=600
    )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=999)
}

# print email content into the console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DJOSER = {

    'SEND_ACTIVATION_EMAIL': False,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'USER_CREATE_PASSWORD_RETYPE': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,

}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
if not DEBUG:/
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',
#     'https://book-rave-git-reviews-escapers-projects.vercel.app'
# ]

# CORS_ORIGIN_WHITELIST = [
#     'http://127.0.0.1:3000',
#     'http://localhost:3000',
# ]

# set it to true and comment CORS_ALLOWED_ORIGINS to fill your db with fake data

CORS_ALLOW_ALL_ORIGINS = True
