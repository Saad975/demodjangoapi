from django.test import TestCase
from users.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='test', email='test@test.com', first_name='te',
                            last_name='st', password='123')
        User.objects.create(username='test2', email='test2@test.com', first_name='te2',
                            last_name='st2', password='123123')

    def test_user_register(self):
        user = User.objects.get(username='test')
        user2 = User.objects.get(username='test2')
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user2.email, 'test2@test.com')


class AuthViewsTests(APITestCase):

    def test_api_jwt(self):

        data = {'username': 'test', 'email': 'test@test.com', 'first_name': 'te',
                'last_name': 'st', 'password': '123'}

        response = self.client.post('http://127.0.0.1:8000/api/v1/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')
        self.assertTrue('username' in response.data)
        user = User.objects.filter(username='test')

        url = reverse('api-token-auth')

        # user = User.objects.create(username='test', email='test@test.com', first_name='te',
        #                           last_name='st')
        # user.set_password('123')
        # user.save()

        data = {'username': 'test', 'password': '123'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')
        self.assertTrue('token' in response.data)
        token = response.data['token']

        verify_url = reverse('api-token-verify')
        response = self.client.post(verify_url, {'token': token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        verify_url = reverse('api-token-refresh')
        response = self.client.post(verify_url, {'token': token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
