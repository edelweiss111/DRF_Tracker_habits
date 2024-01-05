from rest_framework.serializers import ValidationError


class PleasantHabitValidator:
    """Валидатор поля related_habit модели Habit"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if field_value:
            if field_value.pleasant is False:
                raise ValidationError('Связанной может быть только приятная привычка')
