from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_register(self):
        data = {
            'email': 'testuser@mail.ru',
            'password': 'testpassword',
            'telegram_id': '1234567890'
        }

        response = self.client.post(
            reverse('users:register'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 1, 'email': 'testuser@mail.ru'}
        )
