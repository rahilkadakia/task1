from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class SignUpSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SignUp
        fields = ['user', 'username', 'first_name', 'last_name', 'email', 'phone', 'newsletter']