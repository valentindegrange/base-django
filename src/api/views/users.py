# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from api.serializers.users import EmailUserSerializer
from users.models import EmailUser


class UserViewset(ModelViewSet):
    model = EmailUser
    serializer_class = EmailUserSerializer
    permission_classes = [IsAdminUser]
    queryset = EmailUser.objects.all()
