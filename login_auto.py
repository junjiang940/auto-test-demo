import requests
import json

# ---------- 1. 登录接口 ----------
url = "http://172.16.48.31:8800/ltc/user/login"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "Name": "admin",
    "Password": "7487650ba9ad1c7ce7b4375f75d82e",
    "Version": "TS-86d1B-V1.6.2",
    "OrgPassword": "zfr1gU68"
}

# 发送 POST 请求
response = requests.post(url, json=payload, headers=headers, timeout=10)

# 打印调试信息
print("状态码:", response.status_code)
print("响应内容:", response.text)

# 断言请求成功
assert response.status_code == 200, f"登录失败，状态码 {response.status_code}"

# ---------- 2. 提取 Token ----------
try:
    resp_json = response.json()
    token = resp_json.get("data", {}).get("Token")
    if not token:
        raise ValueError("未找到 Token 字段")
    print(f"获取到的 Token: {token}")
except Exception as e:
    print("解析响应 JSON 失败，错误:", e)
    exit(1)

# ---------- 3. （可选）使用 Token 调用其他接口 ----------
# 例如：查询会议列表（假设接口为 /ltc/meeting/list）
# 具体路径和方法请参考实际接口文档
def call_another_api():
    another_url = "http://172.16.48.31:8800/ltc/meeting/list"  # 仅为示例
    another_headers = {
        "Authorization": token,          # 根据截图，直接放 token
        "Content-Type": "application/json"
    }
    resp = requests.get(another_url, headers=another_headers, timeout=10)
    print("会议列表状态码:", resp.status_code)
    print("会议列表响应:", resp.text)

# 如果需要调用，取消下面注释
# call_another_api()

print("登录自动化脚本执行完毕！")