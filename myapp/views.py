from django.shortcuts import render
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

