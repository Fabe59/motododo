from . import *

SECRET_KEY = '+09^7okw6r3be!udnmpdikdb0*mlz4v%$4dz18yf#=p7fuy1*+'
ALLOWED_HOSTS = "127.0.0.1"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}