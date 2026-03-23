from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='antonio',
            email='antonio@example.com',
            password='123456'
        )

    def test_login(self):
        url = reverse('token_obtain_pair')

        response = self.client.post(url, {
            'username': 'antonio',
            'password': '123456'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

    def test_me_authenticated(self):
        response = self.client.post(
            reverse('token_obtain_pair'), {
                'username': 'Antonio',
                'password': '123456'
            }
        )

        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get(reverse('me'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'antonio')

    def test_me_unauthorized(self):
        response = self.client.get(reverse('me'))

        self.assertEqual(response.status_code, 401)
