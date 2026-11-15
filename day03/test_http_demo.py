import requests


BASE_URL = "https://httpbin.org"


def test_get_request():
    response = requests.get(
        f"{BASE_URL}/get",
        params={"keyword": "python", "page": 1},
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()
    assert data["args"]["keyword"] == "python"
    assert data["args"]["page"] == "1"


def test_post_request():
    response = requests.post(
        f"{BASE_URL}/post",
        json={"username": "student", "password": "123456"},
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()
    assert data["json"]["username"] == "student"
    assert data["json"]["password"] == "123456"


def test_404():
    response = requests.get(
        f"{BASE_URL}/status/404",
        timeout=10
    )

    assert response.status_code == 404