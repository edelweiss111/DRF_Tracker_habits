from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    """Пагинатор для эндпоинтов модели Habit"""
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 50
