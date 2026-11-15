import requests


BASE_URL = "https://httpbin.org"


def show_response(name, response):
    print(f"--- {name} ---")
    print("状态码:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("响应体前200个字符:", response.text[:200])
    print()


def main():
    # GET 查询
    response = requests.get(
        f"{BASE_URL}/get",
        params={"keyword": "python", "page": 1},
        timeout=10
    )
    show_response("GET 查询", response)

    # POST 发送 JSON
    response = requests.post(
        f"{BASE_URL}/post",
        json={"username": "student", "password": "123456"},
        timeout=10
    )
    show_response("POST 新增", response)

    # 带 Token 请求
    response = requests.get(
        f"{BASE_URL}/bearer",
        headers={"Authorization": "Bearer testtoken123"},
        timeout=10
    )
    show_response("带 Token 请求", response)

    # 404 错误
    response = requests.get(
        f"{BASE_URL}/status/404",
        timeout=10
    )
    show_response("404 错误", response)


if __name__ == "__main__":
    main()