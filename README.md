# API CRUD Automation (Pytest + Requests)
[![API CRUD Tests](https://github.com/valga292-stack/api-crud-automation/actions/workflows/run-tests.yml/badge.svg)](https://github.com/valga292-stack/api-crud-automation/actions/workflows/run-tests.yml)
Автоматизированный набор API-тестов на Python, проверяющий полный жизненный цикл сущности (CRUD: Create, Read, Update, Delete) на базе REST API (JSONPlaceholder).

## Стек технологий
* Python 3.14
* Pytest — фреймворк для организации и запуска тестов
* Requests — библиотека для отправки HTTP-запросов и валидации JSON-ответов
* Pytest-HTML — генерация наглядных отчётов о прохождении тестов

## Покрытие тестами (test_crud_api.py)
1. **CREATE (POST /posts)** — создание новой записи, проверка статус-кода 201 Created и соответствия тела ответа.
2. **READ (GET /posts/1)** — получение существующей записи, проверка статус-кода 200 OK и обязательных полей JSON.
3. **UPDATE (PUT /posts/1)** — полное обновление записи и проверка сохранения изменённых данных.
4. **DELETE (DELETE /posts/1)** — удаление ресурса и проверка корректного ответа сервера.

## Как запустить локально

1. Клонировать репозиторий и перейти в папку проекта:
  
   git clone https://github.com/valga292-stack/api-crud-automation.git
   cd api-crud-automation
   
2. Установить зависимости:
  
   pip install -r requirements.txt
   
3. Запустить тесты с генерацией HTML-отчёта:
  
   python -m pytest -v --html=report.html --self-contained-html
