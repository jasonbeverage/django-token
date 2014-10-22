from django.core.management.base import BaseCommand, CommandError
from django.utils.six.moves import input

from django.contrib.auth import get_user_model
User = get_user_model()

from django_token.models import Token

class Command(BaseCommand):
    help = "Resets the tokens for all users."

    def handle(self, *args, **options):
        message = ['\n']
        message.append('This will reset the tokens for ALL users in the database.'
                       'Are you sure you want to do this?\n\n'
                       "Type 'yes' to continue, or 'no' to cancel")
        if input("".join(message)) != 'yes':
            raise CommandError("Reset tokens cancelled.")

        for u in User.objects.all():
            # Delete any existing tokens
            Token.objects.filter(user=u).delete()
            # Create the new token
            token = Token.objects.create(user=u)
            print "Resetting token for user %s: token = %s" % (token.user, token)
