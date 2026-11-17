import requests


BASE_URL = "http://127.0.0.1:8000"

def test_get_students():
    response=requests.get(
        f"{BASE_URL}/students",
        timeout=10
    )
    assert response.status_code==200

    data=response.json()
    assert data["code"]==0
    assert isinstance(data["data"],list)

def test_student_crud():
    created_id=None

    try:
        create_response=requests.post(
            f"{BASE_URL}/students",
            json={"name":"自动化测试学生","score":88},
            timeout=10
        )
        assert create_response.status_code==201
        create_data=create_response.json()
        created_id=create_data["data"]["id"]

        assert create_data["code"]==0
        assert create_data["data"]["name"]=="自动化测试学生"
        assert create_data["data"]["score"]==88

        get_response = requests.get(
            f"{BASE_URL}/students/{created_id}",
            timeout=10
        )

        assert get_response.status_code==200
        assert get_response.json()["data"]["id"]==created_id

        update_response = requests.put(
            f"{BASE_URL}/students/{created_id}",
            json={"name": "自动化测试学生修改", "score": 95},
            timeout=10
        )

        assert update_response.status_code==200
        update_data=update_response.json()
        assert update_data["data"]["name"]=="自动化测试学生修改"
        assert update_data["data"]["score"]==95

        delete_response = requests.delete(
            f"{BASE_URL}/students/{created_id}",
            timeout=10
        )

        assert delete_response.status_code==200
        created_id=None

        get_after_delete = requests.get(
            f"{BASE_URL}/students/{update_data['data']['id']}",
            timeout=10
        )

        assert get_after_delete.status_code == 404

    finally:
        # 如果中途失败，尽量清理测试数据
        if created_id is not None:
            requests.delete(
                f"{BASE_URL}/students/{created_id}",
                timeout=10
            )