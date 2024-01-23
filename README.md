# KR_7_DRF_Tracker

#### Структура проекта:
config/
1. settings.py - настройки приложений
2. urls.py - файл маршрутизации
3. celery.py - настройки Celery

tracker/
1. admin.py - настройки админки
2. models.py - модели приложения
3. paginators.py - настройки пагинации
4. permissions.py - настройки прав доступа
5. serializers.py - сериализаторы моделей
6. tasks.py - задачи для Celery
7. tests.py - тесты
8. validators.py - настройки валидации
9. urls.py - файл маршрутизации приложения
10. views.py - контроллеры

users/
1. admin.py - настройки админки
2. models.py - модели приложения
3. serializers.py - сериализаторы моделей
4. tests.py - тесты
5. urls.py - файл маршрутизации приложения
6. views.py - контроллеры

.env.sample - необходимые переменные окружения

manage.py - точка входа веб-приложения

pyproject.toml - список зависимостей для проекта.

#### Используется виртуальное окружение poetry

#### Для запуска web-приложения используйте команду "python manage.py runserver" либо через конфигурационные настройки PyCharm.
