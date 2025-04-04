from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import CustomUser

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None
        
        user = CustomUser.objects.filter(
            Q(email__iexact=username) | Q(phone_no=username)
        ).first()  # Retrieves the first matching user or None

        if user and user.check_password(password):
            return user
        
        return None
