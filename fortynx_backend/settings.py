from pathlib import Path
import os
from decouple import config
import dj_database_url
from dotenv import load_dotenv

# Load .env early
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default='False').lower() in ('1', 'true', 'yes')

# Domains
FRONTEND_DOMAIN = config("FRONTEND_DOMAIN", default="fortynx.in")
WWW_DOMAIN = f"www.{FRONTEND_DOMAIN}"

ALLOWED_HOSTS = [
    FRONTEND_DOMAIN,
    WWW_DOMAIN,
    "api.fortynx.in",  # if this backend is directly accessed via this subdomain
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'contact',
    'services',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # must come before SecurityMiddleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # static file serving
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fortynx_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # add if you have custom template dirs
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

WSGI_APPLICATION = 'fortynx_backend.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

# Password validation (empty for now)
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static / media
STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS: restrict to your actual frontend origins
CORS_ALLOWED_ORIGINS = [
    f"https://{FRONTEND_DOMAIN}",
    f"https://{WWW_DOMAIN}",
]

# HTTPS / security hardening (only when not in debug)
if not DEBUG:
    SECURE_SSL_REDIRECT = True  # redirect HTTP to HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # HSTS
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
