"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b=cyg=dd2=fbkkij2617pn1t76u=d9jzg5_-*cxqge03xs%sh2'
#staticfiles
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]
#TEMPLATES
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'django_countries',
    'avatar',
    'easy_thumbnails',
    'sorl.thumbnail',
    'social_django',
    'album',

]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    
)

SOCIAL_AUTH_PIPELINE = (

   
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
      # <--- set the path to the function
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'accounts.models.save_profile',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_accounts',
        'USER': 'root',
        'PASSWORD': 'J@gjeet04',
        'HOST': '',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#INSTAGRAM
SOCIAL_AUTH_INSTAGRAM_KEY = '34cd688502cd4f6e829b8312b3833d89'
SOCIAL_AUTH_INSTAGRAM_SECRET = 'c56352b50a36423fb5631b61719a027d'
SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {'scope': 'likes comments relationships'}

#GOOGLE
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '693601888040-42rsmq07nfvla15tm5dcg3d2blj2cr37.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'etZ_eUzUvtk9bHWdUlSsnMGP'

SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile'


#FACEBOOK
SOCIAL_AUTH_FACEBOOK_KEY = '140406389887930'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd4643d474f8b930bfa539cc3d4060404'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'first_name, name, link, last_name, email, picture'
}

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.9'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/accounts/userpage/'
# Serving static files in development
# https://docs.djangoproject.com/en/1.10/howto/static-files/n


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/userpage/'

# Email server configuration

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'  # Eg. smtp.gmail.com
EMAIL_HOST_USER = 'imjagjeetubhi@gmail.com'  # Eg. user@domain.com
EMAIL_HOST_PASSWORD = 'J@gjeet04'
EMAIL_PORT = 587
