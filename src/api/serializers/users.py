# -*- coding: utf-8 -*-
from rest_framework import serializers

from users.models import EmailUser


class EmailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailUser
        fields = ['id', 'email']
