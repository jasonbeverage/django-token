from django.http import HttpResponseBadRequest
from django.contrib import auth


class TokenMiddleware(object):
    """
    Middleware that authenticates against a token in the http authorization header.
    """

    def process_request(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', b'').partition(' ')

        if auth_header[0].lower() != b'token':
            return None

        # If they specified an invalid token, let them know.
        if not auth_header[2]:
            return HttpResponseBadRequest("Improperly formatted token")

        user = auth.authenticate(token=auth_header[2])
        if user:
            request.user = user
