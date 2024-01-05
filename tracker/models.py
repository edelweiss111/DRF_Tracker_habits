from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель - привычка"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, verbose_name="Автор")
    place = models.CharField(max_length=50, verbose_name='Место выполнения')
    time = models.DateTimeField(verbose_name='Время выполнения')
    action = models.CharField(max_length=150, verbose_name='Действие')
    pleasant = models.BooleanField(default=False, verbose_name='Признак приятности')
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка')
    periodisity = models.PositiveIntegerField(validators=[MaxValueValidator(7)], default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name='Вознаграждение')
    complete_time = models.PositiveIntegerField(validators=[MaxValueValidator(120)], verbose_name='Время выполнения')
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.action}'

    class Meta:
        """Класс отображения метаданных"""
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    pleasant=False,
                    related_habit__isnull=True,
                    reward__isnull=False
                ) | models.Q(
                    pleasant=False,
                    related_habit__isnull=False,
                    reward__isnull=True
                ) | models.Q(
                    pleasant=True,
                    related_habit__isnull=True,
                    reward__isnull=True
                ),
                name='either_related_habit_or_reward_or_pleasant_habit'
            )
        ]
