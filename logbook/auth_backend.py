from django.contrib.auth.backends import BaseBackend
from .models import User

class IDUsernameAuthBackend(BaseBackend):
    def authenticate(self, request, id=None, username=None):
        try:
            user = User.objects.get(id=id, username=username)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
