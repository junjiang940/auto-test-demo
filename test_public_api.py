import requests

def test_public_api():
    url = "https://httpbin.org/post"
    payload = {"test": "hello"}
    response = requests.post(url, json=payload)
    print("状态码:", response.status_code)
    print("响应内容:", response.json())
    assert response.status_code == 200
    print("✅ 测试通过！")

if __name__ == "__main__":
    test_public_api()
