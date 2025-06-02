from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / '.env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '071192')

# Debug mode
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts
ALLOWED_HOSTS = ['*']  # Update with your domain or IP in production

# Application definition
INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "Spares",
    "Products",
    "Energy_efficiency",
    "service_app",
    "pump",
]
JAZZMIN_SETTINGS = {
    "site_title": "Shaft&Seal Administration",
    "site_header": "Shaft&Seal Admin",
    "site_brand": "Shaft&Seal",
    "site_logo": "img/Logo.jpeg",
    "welcome_sign": "Welcome to the Shaft&Seal Admin Panel",
    "copyright": "Shaft&Seal pvt ltd",
    "custom_css": "css/custom_admin.css",
    "icons": {
    "Spares": "fas fa-cogs",
    "Spares.PumpParts": "fas fa-tools",
    "Spares.PumpMaker": "fas fa-industry",
    "Spares.PumpModel": "fas fa-cubes",
    "Spares.Materials": "fas fa-toolbox",
    "Spares.PumpModelDesign": "fas fa-drafting-compass",
    "Spares.PumpModelVariant": "fas fa-sliders-h",
    "Spares.PartMaterials": "fas fa-link",
    "Spares.ModelVariantPart": "fas fa-link",
    "Spares.ModelVarientDesignParts": "fas fa-link",
    "Spares.ModelPart": "fas fa-link",
    "accounts.Account": "fas fa-user-circle",
},

    "order_with_respect_to": ["accounts","accounts.Account","accounts.UserProfile","Spares", "Spares.PumpMaker","Spares.PumpModel",
    "Spares.PumpModelVariant","Spares.PumpModelDesign","Spares.PumpParts","Spares.Materials","Spares.PartMaterials","Spares.ModelPart",
    "Spares.ModelVariantPart","Spares.ModelVarientDesignParts"],
}


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

# Database configuration

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME", "shaftseal_db"),
        'USER': os.getenv("DB_USER", "shaftseal_user"),
        'PASSWORD': os.getenv("DB_PASSWORD", "shaftseal@12345"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "3306"),
    }
}

# Caching (Redis)
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
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

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom User Model and Authentication
AUTH_USER_MODEL = 'accounts.Account'
AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Message tags
MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# Email configuration
#SMTP Configuration
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER= 'nkmbills@gmail.com'
EMAIL_HOST_PASSWORD= 'scsa llxj xqrs ozws'
EMAIL_USE_TLS= True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'UTC'

#django custom admin panel configuration using jazzmin library
