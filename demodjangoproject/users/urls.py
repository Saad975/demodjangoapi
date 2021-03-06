from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CreateUser, UserAuthToken
from rest_framework.authtoken import views


router = DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'users', CreateUser, basename='api-user')

urlpatterns = [
    path('', include(router.urls)),
]