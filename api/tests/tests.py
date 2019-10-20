from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import User

from .factories import UserFactory


class UserViewSetTestCase(APITestCase):

    def test_listing(self):
        users = UserFactory.create_batch(3)
        response = self.client.get(
            reverse('api:users-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), len(users))

    def test_filtering(self):
        UserFactory.bulk_create({'birthday': '1971-05-15'},
                                {'birthday': '1984-05-15'},
                                {'birthday': '1985-05-15'},
                                {'birthday': '1991-05-15'})
        response = self.client.get(reverse('api:users-list'),
                                   {'from': '01.01.1980', 'to': '01.01.1990'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_creating(self):
        users = []
        for user in UserFactory.stub_batch(3, birthday='01.01.1980'):
            users.append(user.__dict__)
        response = self.client.post(
            reverse('api:users-list'), data=users, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), len(users))
