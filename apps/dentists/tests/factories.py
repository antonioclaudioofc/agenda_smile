from datetime import time

import factory

from apps.accounts.tests.factories import UserFactory
from apps.dentists.models import Dentist


class DentistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dentist

    name = factory.Faker('name')
    specialty = factory.Faker('job')

    @factory.lazy_attribute
    def start_time(self):
        return time(8, 0)

    @factory.lazy_attribute
    def end_time(self):
        return time(18, 0)

    user = factory.SubFactory(UserFactory)
