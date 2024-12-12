# Интернет магазин
## Описание:
Интернет магазин
## Установка:
1. Клонируйте репозиторий:
```
[https://github.com/IvanRas/project23]
```
2. Установите зависимости:
```
pip install poetry
poetry install
poetry add requests
pip install pytest
pip install  pytest-cov
poetry add python-dotenv 
poetry add --group lint mypy
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint flake8 
poetry add requests-mock

```
