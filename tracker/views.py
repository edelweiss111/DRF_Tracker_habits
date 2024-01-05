from rest_framework import viewsets

from tracker.models import Habit
from tracker.paginators import HabitPagination
from tracker.permissions import IsOwner
from tracker.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """Вьюсет модели Habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination

    def get_permissions(self):
        """Разрешения для разных типов запроса"""
        if self.action == 'retrieve' or 'update' or 'destroy':
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = Habit.objects.filter(is_public=True)
    #     return queryset

    def perform_create(self, serializer):
        """Присваивание автора к привычке"""
        new_habit = serializer.save()
        new_habit.author = self.request.user
        new_habit.save()