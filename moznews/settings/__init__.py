from django.core.exceptions import ImproperlyConfigured


try:
    from .local import *
except ImportError as e:
    raise ImproperlyConfigured('Could not import local settings: %r' % e)

if SECRET_KEY is None:
    raise ImproperlyConfigured('SECRET_KEY must be set!')
