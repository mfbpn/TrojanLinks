"""
Author: mfbpn
Date: 2024-11-03 11:47:36
Description: 
"""

import requests
import random
import base64
import os
import string

base_url = os.environ['xb_url']

def generate_random_qq_email():
    return f"{random.randint(100000, 999999999)}@qq.com"


EMAIL = generate_random_qq_email()
PASSWORD = "qq123456"

url = f"{base_url}/api/v1/passport/auth/register"
url2 = f"{base_url}/api/v1/client/subscribe?token="
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
    "Accept": "*/*",
}

data = {"email": EMAIL, "password": PASSWORD, "invite_code": "", "email_code": ""}

try:
    response = requests.post(url, headers=headers, data=data)
    token = response.json()["data"]["token"]
    porxy_url = f"{url2}{token}"
    # print(porxy_url)
    # print(f"{url2}{token}")
    headers4 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    response = requests.get(porxy_url, headers=headers4).text
    # print(response)
    abcd = (
        base64.b64decode(response.encode("utf-8"))
        .decode("utf-8")
        .replace("\r\n", " @𝙢𝙛𝙗𝙥𝙣\r\n")
    )

    abcd2 = base64.b64encode(abcd.encode("utf-8"))
    # print(abcd2)
    with open("./links/xb", "wb") as f:
        f.write(abcd2)
except (requests.exceptions.RequestException, KeyError, ValueError) as e:
    print("Error:", e)
