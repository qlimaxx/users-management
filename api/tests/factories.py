import factory

from api.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    birthday = factory.Faker('date')

    @classmethod
    def bulk_create(cls, *items):
        for item in items:
            cls(**item)
