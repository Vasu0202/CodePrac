"""
Django settings for core project.

Updated to support environment-configured ALLOWED_HOSTS, DEBUG and SECRET_KEY
so the same image can run locally and on an EC2 instance without editing code.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read secrets and flags from environment (useful for Docker/EC2).
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-+5zeb#itzx@d%16&pet-*xz29l*3ria1h9i1efe83ey31%_y(r"  # fallback for dev only
)

# Convert env var to boolean reliably
def env_bool(name, default=False):
    val = os.getenv(name)
    if val is None:
        return default
    return str(val).lower() in ("1", "true", "yes", "on")

DEBUG = env_bool("DJANGO_DEBUG", True)

# ALLOWED_HOSTS: comma-separated environment variable, fallback to localhost
raw_allowed = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost")
ALLOWED_HOSTS = [h.strip() for h in raw_allowed.split(",") if h.strip()]

# CSRF_TRUSTED_ORIGINS - use explicit env var if provided, otherwise derive basic http origins
raw_csrf = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "")
if raw_csrf:
    CSRF_TRUSTED_ORIGINS = [c.strip() for c in raw_csrf.split(",") if c.strip()]
else:
    # Build simple http(s) origins from ALLOWED_HOSTS (skip localhost and 127.0.0.1)
    CSRF_TRUSTED_ORIGINS = []
    for h in ALLOWED_HOSTS:
        if h and h not in ("127.0.0.1", "localhost"):
            CSRF_TRUSTED_ORIGINS.append(f"http://{h}")
            CSRF_TRUSTED_ORIGINS.append(f"https://{h}")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'compiler',
    'markdownify',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database - keep SQLite for now; if you add DATABASE_URL later you can change this.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# Where `collectstatic` will collect files for production inside the container
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/problems/'
LOGOUT_REDIRECT_URL = '/'

# Docker and Code Execution Configuration
DOCKER_CONFIG = {
    'MEMORY_LIMIT': '256m',
    'CPU_LIMIT': '1',
    'TIMEOUT_COMPILE': 30,  # seconds
    'TIMEOUT_SUBMISSION': 15,  # seconds per test case
    'MAX_OUTPUT_LENGTH': 10000,  # characters
}

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
    ],
}

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
