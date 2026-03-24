import factory

from apps.accounts.tests.factories import UserFactory
from apps.patients.models import Patient


class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    name = factory.Faker('name')
    cpf = factory.Sequence(lambda n: f'000000000{n}')
    user = factory.SubFactory(UserFactory)
