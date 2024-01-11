from datetime import datetime, timezone, timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from tracker.models import Habit
from users.models import User

TIME = datetime.now(tz=timezone(timedelta(hours=3)))


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='testuser@mail.ru', password='test1234')
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place="test place",
            time=TIME,
            action="test action",
            complete_time=100,
            author=self.user,
            reward='test reward',
            is_public=True,
        )

    def test_create_habit(self):
        """Тестирование создание привычки"""
        data = {
            "place": 'место',
            "time": "2024-11-11 11:20",
            "action": "действие",
            "complete_time": 100,
            "reward": "награда",
        }
        response = self.client.post(
            'http://127.0.0.1:8000/habits/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 2, 'author': self.user.pk, 'place': 'место', 'time': '2024-11-11T11:20:00+03:00',
             'action': 'действие', 'pleasant': False, 'related_habit': None, 'periodisity': 1,
             'reward': 'награда', 'complete_time': 100, 'is_public': False}
        )

    def test_habit_list(self):
        """Тестирование списка привычек"""

        response = self.client.get(
            'http://127.0.0.1:8000/habits/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.habit.id,
                        "place": self.habit.place,
                        "time": self.habit.time.isoformat(),
                        "action": self.habit.action,
                        "pleasant": self.habit.pleasant,
                        "periodisity": self.habit.periodisity,
                        "reward": self.habit.reward,
                        "complete_time": self.habit.complete_time,
                        "is_public": self.habit.is_public,
                        "author": self.habit.author.pk,
                        "related_habit": self.habit.related_habit
                    }
                ]
            }
        )

    def test_user_habit_list(self):
        """Тестирование списка привычек пользователя"""

        response = self.client.get(
            reverse('tracker:user_habit'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.habit.id,
                    "place": self.habit.place,
                    "time": self.habit.time.isoformat(),
                    "action": self.habit.action,
                    "pleasant": self.habit.pleasant,
                    "periodisity": self.habit.periodisity,
                    "reward": self.habit.reward,
                    "complete_time": self.habit.complete_time,
                    "is_public": self.habit.is_public,
                    "author": self.habit.author.pk,
                    "related_habit": self.habit.related_habit,
                }
            ]
        )

    def test_habit_retrieve(self):
        """Тестирование одной привычек"""

        response = self.client.get(
            f'http://127.0.0.1:8000/habits/{self.habit.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "place": self.habit.place,
                "time": self.habit.time.isoformat(),
                "action": self.habit.action,
                "pleasant": self.habit.pleasant,
                "periodisity": self.habit.periodisity,
                "reward": self.habit.reward,
                "complete_time": self.habit.complete_time,
                "is_public": self.habit.is_public,
                "author": self.habit.author.pk,
                "related_habit": self.habit.related_habit,
            }
        )

    def test_update_habit(self):
        """Тестирование обновления привычки"""
        data = {
            "place": 'new test place',
        }
        response = self.client.patch(
            f'http://127.0.0.1:8000/habits/{self.habit.pk}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "place": 'new test place',
                "time": self.habit.time.isoformat(),
                "action": self.habit.action,
                "pleasant": self.habit.pleasant,
                "periodisity": self.habit.periodisity,
                "reward": self.habit.reward,
                "complete_time": self.habit.complete_time,
                "is_public": self.habit.is_public,
                "author": self.habit.author.pk,
                "related_habit": self.habit.related_habit,
            }
        )

    def test_delete_habit(self):
        """Тестирование удаления привычки"""

        response = self.client.delete(
            f'http://127.0.0.1:8000/habits/{self.habit.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
