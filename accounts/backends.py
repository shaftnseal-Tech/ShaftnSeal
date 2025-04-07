from django.contrib.auth.backends import ModelBackend
from .models import Account

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
