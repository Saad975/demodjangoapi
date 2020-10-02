from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, mixins, views, permissions

from .models import User
from .serializers import CreateUserSerializer


# Create your views here.
class CreateUser(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (permissions.AllowAny,)


class UserAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({User: {'token': token.key, 'user_id': user.pk, 'email': user.email}})