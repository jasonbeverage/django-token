from django import http
from django.contrib import auth
from django.core import exceptions


class TokenMiddleware(object):
    """
    Middleware that authenticates against a token in the http authorization
    header.
    """
    get_response = None

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if not self.get_response:
            return exceptions.ImproperlyConfigured(
                'Middleware called without proper initialization')

        self.process_request(request)

        return self.get_response(request)

    def process_request(self, request):
        auth_header = str(request.META.get('HTTP_AUTHORIZATION', '')).partition(' ')

        if auth_header[0].lower() != 'token':
            return None

        # If they specified an invalid token, let them know.
        if not auth_header[2]:
            return http.HttpResponseBadRequest("Improperly formatted token")

        user = auth.authenticate(token=auth_header[2])
        if user:
            request.user = user
