from app.models import *
from app.serializers import *


from rest_framework.response import Response
from rest_framework import viewsets, permissions, filters, status
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

class UsersTableViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = UserTable.objects.all()
    serializer_class = UsersSerializer

class UserTypeClientViewSet(viewsets.ModelViewSet):
    queryset = UserTable.objects.all()
    serializer_class = UserTypeClientSerializer

class UserBasicaViewSet(viewsets.ModelViewSet):
    queryset = UserTable.objects.all()
    serializer_class = UserBasicSerializer


class RegisterUserTableViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = UserTable.objects.all()
    serializer_class = RegisterSerializer

