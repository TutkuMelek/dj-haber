import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = "django-insecure-$6jo%!&pc#!rb+$0^rahf++!yk95j)uc9ej9e8w9!rs*#fj+0c"

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tcore",
    "tinymce",
]
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 920,
    'menubar': True,
    'plugins': 'advlist autolink lists link image charmap print preview anchor',
    'toolbar': 'undo redo | formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
    'content_css': '//www.tiny.cloud/css/codepen.min.css',
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "corporate.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "tcore.context_processors.SettingList",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "corporate.wsgi.application"



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "tr"

LANGUAGES=[
    ('tr', _('Turkish')),
    ('en', _('English')),
]


MODELTRANSLATION_DEFAULT_LANGUAGE="tr"

MODELTRANSLATION_LANGUAGE=("tr","en")

TIME_ZONE = "UTC"

USE_I18N = True
USE_L10N = True
USE_TZ = True



STATIC_URL = "static/"
STATICFILES_DIRS=(BASE_DIR,"static")

LOCALE_PATHS=[os.path.join(BASE_DIR,"locale")]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField" 
