from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CreateUser, UserAuthToken
from rest_framework.authtoken import views


router = DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'users', CreateUser)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', UserAuthToken.as_view()),
    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    # path('user', CreateUser.as_view(), name="create-user"),
]