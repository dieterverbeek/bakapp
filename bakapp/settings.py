"""
Django settings for bakapp project.
"""

from pathlib import Path
from dotenv import load_dotenv
import os
from decouple import config

# Laad omgevingsvariabelen EENMAAL aan het begin
load_dotenv()

# --- VEILIGHEID: Laad gevoelige data uit omgevingsvariabelen (.env bestand) ---
# Zorg ervoor dat je een .env-bestand hebt met een nieuwe, sterke SECRET_KEY
SECRET_KEY = config('SECRET_KEY')
EENVOUDIGFACTUREREN_EMAIL = config('EENVOUDIGFACTUREREN_EMAIL')
EENVOUDIGFACTUREREN_PASSWORD = config('EENVOUDIGFACTUREREN_PASSWORD')
OPENROUTE_API_KEY = os.getenv('OPENROUTE_API_KEY')

# --- PRODUCTIE INSTELLING: DEBUG ---
# BELANGRIJK: Zet op False voor productie!
DEBUG = config('DEBUG', default=False, cast=bool) # Aanbevolen: beheer via .env

# --- DOMEIN CONFIGURATIE ---
ALLOWED_HOSTS = [
    'retrosnacks.be',
    'www.retrosnacks.be',
    '13.60.12.35', # Je server IP
]

# --- HTTPS & Security Instellingen voor Productie ---
# Vertrouwde origings voor CSRF (NU MET HTTPS!)
CSRF_TRUSTED_ORIGINS = [
    'https://retrosnacks.be',
    'https://www.retrosnacks.be',
]

# Dwing HTTPS af
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS (HTTP Strict Transport Security) voor extra veiligheid
SECURE_HSTS_SECONDS = 2592000  # 30 dagen, verhoog later naar 31536000 (1 jaar)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Overige security-instellingen
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = True


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'retrosnacks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- CORS (Cross-Origin Resource Sharing) ---
# VERWIJDERD: CORS_ALLOW_ALL_ORIGINS = True (onveilig)
# TOEGEVOEGD: Beperk tot je eigen domein
CORS_ALLOWED_ORIGINS = [
    "https://retrosnacks.be",
    "https://www.retrosnacks.be",
]

ROOT_URLCONF = 'bakapp.urls'
WSGI_APPLICATION = 'bakapp.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# --- Database ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'

# --- Internationalization ---
LANGUAGE_CODE = 'nl-be' # AANGEPAST
TIME_ZONE = 'Europe/Brussels' # AANGEPAST
USE_I18N = True
USE_TZ = True

# --- Static en Media files ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- Default primary key ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Email ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')