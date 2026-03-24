from rest_framework.test import APITestCase
from django.urls import reverse

from apps.accounts.tests.factories import UserFactory
from apps.dentists.tests.factories import DentistFactory


class DentistTests(APITestCase):
    def setUp(self):
        self.user = UserFactory()

        response = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user.username,
            'password': '123456'
        })

        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_dentist(self):
        response = self.client.post('/api/dentists/', {
            'name': 'Antonio',
            'specialty': 'Dentista',
            'start_time': '08:00',
            'end_time': '17:00'
        })

        self.assertEqual(response.status_code, 201)

    def test_list_dentists(self):
        DentistFactory(user=self.user)
        DentistFactory()

        response = self.client.get('/api/dentists/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_dentist(self):
        dentist = DentistFactory(user=self.user)

        response = self.client.patch(f'/api/dentists/{dentist.id}/', {
            'name': 'Maria'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Maria')

    def test_delete_dentist(self):
        dentist = DentistFactory(user=self.user)

        response = self.client.delete(f'/api/dentists/{dentist.id}/')

        self.assertEqual(response.status_code, 204)

    def test_cannot_access_other_user_dentist(self):
        other_dentist = DentistFactory()

        response = self.client.get(f'/api/dentists/{other_dentist.id}/')

        self.assertEqual(response.status_code, 404)
