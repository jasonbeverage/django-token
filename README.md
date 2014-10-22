django-token
============

Simple token based authentication for Django.

This draws inspiration from the Django Rest Framework token based authentication scheme but allows you to use it without using Django Rest Framework.

## Installing

Install from pip
```
sudo pip install django_token
```

Add the middleware to your MIDDLEWARE_CLASSES

```python
MIDDLEWARE_CLASSES = (
    # Other middleware
    'django_token.middleware.TokenMiddleware',
 )
```

Add the authenticaton backend to your AUTHENTICATION_BACKENDS
```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_token.backends.TokenBackend'
)
```

## Creating tokens
You can create tokens for users using whatever workflow you'd like.
```python
from django_token.models import Token

token = Token.objects.create(user=myuser)
```

