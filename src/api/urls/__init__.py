# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework.routers import DefaultRouter


from api.views import (
    UserViewset
)

app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewset, basename='users')

urlpatterns = router.urls


