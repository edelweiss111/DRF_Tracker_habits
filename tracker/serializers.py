from rest_framework import serializers

from tracker.models import Habit
from tracker.validators import PleasantHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор модели Habit"""

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [PleasantHabitValidator(field='related_habit')]
