from django.contrib.auth.backends import BaseBackend

from users.models import User


class UserAuthenticator(BaseBackend):
    def authenticate(self, request, username=None,password=None):
        try:
            user = User.objects.get(username=username,password=password)
        except User.DoesNotExist:
            return None
        return user
