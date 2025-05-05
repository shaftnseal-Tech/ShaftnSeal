from pathlib import Path
import os
from django.contrib.messages import constants as messages
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!


ALLOWED_HOSTS = ['*']
  # Add your server's IP or domain here

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    # "Customers",
    "Spares",
    "Products",
    "Energy_efficiency",
    "service_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ShaftSeal_Website.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "ShaftSeal_Website.wsgi.application"

# Database






# Load environment variables from .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')  # makes it platform independent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
    }
}




SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-secret-key')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Make sure it's pointing to Redis
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


# Password validation
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
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]

# Directory where collectstatic will place static files for Nginx
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Optional: Additional static files locations (if needed)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  
]

# Media files (user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#
AUTH_USER_MODEL = 'accounts.Account'
AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    ]

# AUTH_USER_MODEL = "Customers.CustomUser"
# LOGIN_URL = '/Customer/login/'

# SESSION_ENGINE = 'django.contrib.sessions.backends.db'

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

#SMTP Configuration
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER= 'pandapritirekha2@gmail.com'
EMAIL_HOST_PASSWORD= 'ykns inoe vvll wdwj'
EMAIL_USE_TLS= True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis broker URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'UTC'
