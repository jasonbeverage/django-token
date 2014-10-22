from django_token.models import Token

from django.contrib.auth import get_user_model

User = get_user_model()


class TokenBackend(object):
    def authenticate(self, token=None):
        """
        Try to find a user with the given token
        """
        try:
            t = Token.objects.get(key=token)
            return t.user
        except Token.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
