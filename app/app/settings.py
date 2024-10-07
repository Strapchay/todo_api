"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "changeme")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG", 0)))

ALLOWED_HOSTS = []

DEV_MODE = os.environ.get("DEV")

if DEV_MODE:
    ALLOWED_HOSTS.append("*")
else:
    ALLOWED_HOSTS.extend(
        filter(
            None,
            os.environ.get("ALLOWED_HOSTS", "").split(","),
        )
    )

# Application definition
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = []
CORS_ORIGIN_WHITELIST.extend(
    filter(
        None,
        os.environ.get("ALLOWED_HOSTS", "").split(","),
    )
)

CSRF_TRUSTED_ORIGINS = []
CSRF_TRUSTED_ORIGINS.extend(
    filter(
        None,
        os.environ.get("ALLOWED_HOSTS", "").split(","),
    )
)

CSRF_ALLOWED_ORIGINS = []
CSRF_ALLOWED_ORIGINS.extend(
    filter(
        None,
        os.environ.get("ALLOWED_HOSTS", "").split(","),
    )
)

CORS_ALLOW_HEADERS = ["X-Custom-Header", "Authorization", "Content-Type"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "core",
    "rest_framework",
    "rest_framework.authtoken",
    "user",
    "drf_spectacular",
    "corsheaders",
    "todo",
    "dj_rest_auth",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
]

SITE_ID = 1

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "PORT": int(os.environ.get("DB_PORT", 5432)),
    }
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "testuser@example.com")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 547))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "testuser@example.com")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "Testuser123")
EMAIL_USE_TLS = bool(int(os.environ.get("EMAIL_USE_TLS", 1)))
EMAIL_USE_SSL = bool(int(os.environ.get("EMAIL_USE_SSL", 0)))
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/static/"
MEDIA_URL = "/static/media/"

MEDIA_ROOT = "/vol/web/media"
STATIC_ROOT = "/vol/web/static"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "core.User"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "user.authentication.ExpiringTokenAuthentication",
    ),
    "PASSWORD_RESET_SERIALIZER": "user.serializers.ResetPasswordSerializer",
    "PASSWORD_RESET_CONFIRM_SERIALIZER": "user.serializers.ResetPasswordConfirmSerializer",
}

REST_AUTH_SERIALIZERS = {
    "PASSWORD_RESET_SERIALIZER": "user.serializers.ResetPasswordSerializer",
    "PASSWORD_RESET_CONFIRM_SERIALIZER": "user.serializers.ResetPasswordConfirmSerializer",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Todo API",
    "DESCRIPTION": "An API which allows creation of todos for users",
    "COMPONENT_SPLIT_REQUEST": True,
}
