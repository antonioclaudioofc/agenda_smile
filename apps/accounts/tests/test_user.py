from rest_framework.test import APITestCase
from django.urls import reverse


class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('register')

        data = {
            'first_name': 'Antonio',
            'username': 'antonio',
            'email': 'antonio@example.com',
            'password': '123456'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['email'], data['email'])

    def test_duplicate_email(self):
        url = reverse('register')

        data = {
            'first_name': 'Antonio',
            'username': 'antonio',
            'email': 'antonio@example.com',
            'password': '123456'
        }

        self.client.post(url, data)
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

    def test_username_with_spaces(self):
        url = reverse('register')

        data = {
            'first_name': 'Antonio',
            'username': 'antonio claudio',
            'email': 'antonio@example.com',
            'password': '123456'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

    def test_username_case_insensitive(self):
        url = reverse('register')

        data1 = {
            'first_name': 'Antonio',
            'username': 'antonio',
            'email': 'antonio@example.com',
            'password':  '123456'
        }

        data2 = {
            'first_name': 'Antonio',
            'username': 'Antonio',
            'email': 'antonio1@example.com',
            'password': '123456'
        }

        self.client.post(url, data1)
        response = self.client.post(url, data2)

        self.assertEqual(response.status_code, 400)
