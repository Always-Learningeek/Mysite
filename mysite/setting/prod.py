from mysite.settings import *


SECRET_KEY = 'django-insecure-zh#2jsm0t+i%+--i8-=ai+(funu2-ye7ar_(+15yz%0x_no5xp'

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'statics',
    BASE_DIR / 'accounts/statics_accounts',
]
