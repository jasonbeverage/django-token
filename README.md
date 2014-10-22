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

If you REALLY want to reset all the tokens in your database, you can use the reset_tokens management command.

```
python manage.py reset_tokens
```

This is useful when you've just installed django-token, but is otherwise dangerous :)

## Token in headers

The user's token should be passed in on every request in the HTTP authorization header.

Using [requests](http://docs.python-requests.org/en/latest/)
```python
import requests
response = requests.get(
    "http://myserver.com/api/stuff",
    headers={"Authorization": "token r454f2529f2cd27e1722e67a624b2b18335e6c21"}
)
```

