import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def test_create_post_post():
    """CREATE (POST): Создание новой записи и проверка статуса 201"""
    payload = {
        "title": "QA Automation Engineering",
        "body": "Testing full CRUD cycle with Pytest and Requests",
        "userId": 101
    }
    response = requests.post(BASE_URL, json=payload)
    data = response.json()

    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_read_post_get():
    """READ (GET): Получение существующей записи и проверка структуры JSON"""
    response = requests.get(f"{BASE_URL}/1")
    data = response.json()

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_update_post_put():
    """UPDATE (PUT): Полное обновление записи и проверка изменённых данных"""
    updated_payload = {
        "id": 1,
        "title": "Updated QA Automation Title",
        "body": "Updated content via PUT request",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/1", json=updated_payload)
    data = response.json()

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert data["title"] == "Updated QA Automation Title"
    assert data["body"] == "Updated content via PUT request"


def test_delete_post_delete():
    """DELETE (DELETE): Удаление записи и проверка успешного ответа сервера"""
    response = requests.delete(f"{BASE_URL}/1")

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert response.json() == {}
