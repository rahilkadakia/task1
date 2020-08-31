from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=20, null=False, blank=False, unique=True, default='no_username')
    password = models.CharField(max_length=20, null=False, blank=False, unique=True, default='no_password')
    email = models.EmailField(max_length=75, null=False, blank=False, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    newsletter = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.user.username