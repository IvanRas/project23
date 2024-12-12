# Проект по модулю "Разработка веб-приложений на Django"

Проект о созданий и работе с веб-приложений

## Описание проекта

В  проекте реализованны основы по работе с Django. А имено создание и работа с классами CBV и что такое CRUD 
(Create, Read, Update, Delete) работа с шаблонами и подшаблонами, Аутентификация в веб-приложениях и права доступа, 
а также кешироание данных.
для премера работы присутствует json-файлы
применение фикстур
python manage.py loaddata product_fixture.json --format json
python manage.py loaddata category_fixture.json --format json
python manage.py loaddata user_fixture.json --format json


## Установка:

1. Клонируйте репозиторий:
```
https://github.com/IvanRas/project23/tree/develop
```

2. Установите зависимости:
```
# для первичной установки
poetry install
# для обновления
poetry update

# применение фикстур
python manage.py loaddata product_fixture.json --format json
python manage.py loaddata category_fixture.json --format json
python manage.py loaddata user_fixture.json --format json
```
## Использование:

a) Запустите redis-server
б) В терминале введите команду запуска сервера: python manage.py runserver
