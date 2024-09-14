# backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import *
from django.core.exceptions import MultipleObjectsReturned
class BloggersBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            users = Bloggers.objects.filter(email=email)
            if users.exists():
                for user in users:
                    if check_password(password, user.password):
                        return user
           # user = students.objects.get(email=email)
            return None
        except MultipleObjectsReturned:
            users = Bloggers.objects.filter(email=email)[:1]
            if users:
                user = users[0]
                if check_password(password, user.password):
                    return user
            return None
        except Bloggers.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Bloggers.objects.get(pk=user_id)
        except Bloggers.DoesNotExist:
            return None
