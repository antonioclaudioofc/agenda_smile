from rest_framework.test import APITestCase
from django.urls import reverse

from apps.accounts.tests.factories import UserFactory
from apps.patients.tests.factories import PatientFactory


class PatientTests(APITestCase):
    def setUp(self):
        self.user = UserFactory()

        response = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user.username,
            'password': '123456'
        })

        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_patient(self):
        response = self.client.post('/api/patients/', {
            'name': 'Teste',
            'phone': '99999999999',
            'cpf': '12345678912'
        })

        self.assertEqual(response.status_code, 201)

    def test_list_patients(self):
        PatientFactory(user=self.user)
        PatientFactory()

        response = self.client.get('/api/patients/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_patient(self):
        patient = PatientFactory(user=self.user)

        response = self.client.patch(f'/api/patients/{patient.id}/', {
            'name': 'Novo nome'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Novo nome')

    def test_delete_patient(self):
        patient = PatientFactory(user=self.user)

        response = self.client.delete(f'/api/patients/{patient.id}/')

        self.assertEqual(response.status_code, 204)

    def test_cannot_access_other_user_patient(self):
        other_patient = PatientFactory()

        response = self.client.get(f'/api/patients/{other_patient.id}/')

        self.assertEqual(response.status_code, 404)
