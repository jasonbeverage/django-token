from django.db import models
import os

from django.conf import settings

import binascii


class Token(models.Model):
    """
    An access token that is associated with a user.  This is essentially the same as the token model from Django REST Framework
    """
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="token")
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __unicode__(self):
        return self.key
