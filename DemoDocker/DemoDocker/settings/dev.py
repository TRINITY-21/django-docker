from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-+0x)*rx2(gy-(4_8-%pbcnsf1lyvo@8)7q9f=fy3+hslk1lxlr'

# SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = ['*']


SECRET_KEY = os.environ.get("SECRET_KEY",'django-insecure-+0x)*rx2(gy-(4_8-%pbcnsf1lyvo@8)7q9f=fy3+hslk1lxlr')

DEBUG = int(os.environ.get("DEBUG", default=1))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1").split(" ")


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
