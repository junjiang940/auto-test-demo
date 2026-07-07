import requests

# 请求信息
method = "POST"
url = "http://api.fbi.com:9225/rest-v2/login/access_token"
headers = {
    'content-type': 'application/json'
}
payload = {
    "email": "bf@qq.com",         # 换成正确的账号
    "password": "bf1234561111"    # 换成正确的密码
}

# 发送请求
response = requests.request(method, url, headers=headers, json=payload)

# 打印原始响应内容
print("状态码:", response.status_code)
print("响应正文:", response.text)

# 如果返回的是 JSON，可以这样解析
try:
    print("JSON 格式:", response.json())
except:
    print("响应不是 JSON 格式")

# 断言（测试检查点）
assert response.status_code == 200, f"期望200，实际{response.status_code}"
assert "access_token" in response.text, "响应中未包含 access_token"