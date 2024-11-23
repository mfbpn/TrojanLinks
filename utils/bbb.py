import json
import os
import uuid
import httpx
from datetime import datetime
from Crypto.Hash import MD5
from Crypto.Cipher import AES
from Telegram_bot import send_message

import requests
import random
import base64
import re
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
import re
import time
from bs4 import BeautifulSoup
from urllib import parse
from urllib.parse import unquote


class Emailnator:
    def __init__(self):
        self.base_url = os.environ['bzy_urlcode']
        self.session = httpx.Client()

        # 设置初始请求头
        self._setup_headers()

    def _setup_headers(self):
        self.session.headers = {
            # ... 保留原有的头信息 ...
        }

        self.session.get(self.base_url)
        self.session.headers.update(
            {
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Origin": self.base_url.rstrip("/"),
                "Referer": self.base_url,
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
                "X-KL-kfa-Ajax-Request": "Ajax_Request",
                "X-Requested-With": "XMLHttpRequest",
                "X-XSRF-TOKEN": str(self.session.cookies["XSRF-TOKEN"]).replace(
                    "%3D", "="
                ),
            }
        )

    def generate_mail(self, mail_type: list = None):
        mail_json = {"email": ["dotGmail"] if mail_type is None else mail_type}
        try:
            response = self.session.post(
                self.base_url + "generate-email", json=mail_json
            )
            response.raise_for_status()
            return response.json()["email"][0]
        except Exception as e:
            # logger.error(f"生成邮箱失败: {e}")
            return None

    def fetch_messages(self, mail: str):
        while True:
            try:
                response = self.session.post(
                    self.base_url + "message-list", json={"email": mail}
                )
                response.raise_for_status()
                return response.json()["messageData"]
            except Exception as e:
                # logger.warning(f"获取邮件列表失败: {e}")
                time.sleep(5)

    def extract_verification_info(self, message):
        # 匹配包含“八爪鱼”的验证码邮件信息
        pattern = re.compile(
            r"【八爪鱼】您的验证码是：(\d{4})。请不要把验证码泄露给其他人。"
        )
        match = re.search(pattern, message.text)
        if match:
            return match.group(1)  # 返回验证码部分
        return None

    def get_verification_link(self, mail: str):
        while True:
            messages = self.fetch_messages(mail)
            for message_data in messages:
                # print(message_data)
                if len(str(message_data["messageID"])) > 12:
                    message = self.session.post(
                        self.base_url + "message-list",
                        json={"email": mail, "messageID": message_data["messageID"]},
                    )
                    verification_info = self.extract_verification_info(message)
                    if verification_info:
                        # logger.info(f"验证码是: {verification_info}")
                        return verification_info
            time.sleep(5)  # 避免频繁请求



if __name__ == '__main__':

    def uuid_a():
        characters = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choice(characters) for i in range(8))
        return (random_string)
    uuid = uuid_a()
    # 使用时
    emailnator = Emailnator()
    mail = emailnator.generate_mail()
    if mail:
        print(mail)
        time.sleep(10)
        # print(emailnator.get_verification_link(mail))
    else:
        print("生成邮箱失败")

    # 自定义请求头
    headers11 = {
        "User-Agent": "Octopus_Android",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    url4 = os.environ['bzy_url4']
    params4 = {"phoneNumber": mail}

    # 发送 POST 请求
    porxy_phone = requests.post(url4, headers=headers11, params=params4).json()

    # print(porxy_phone)

    def aes_encrypt(key: bytes, iv: bytes, plaintext: str) -> str:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = pad(plaintext.encode(), AES.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        return binascii.hexlify(ciphertext).decode().upper() # 强制大写字母

    key_text = os.environ['bzy_key']
    iv_text = os.environ['bzy_iv']
    key_bytes = key_text.encode('utf-8')
    iv_bytes = iv_text.encode('utf-8')
    key_text2 = os.environ['bzy_key2']
    iv_text2 = os.environ['bzy_iv2']
    key_bytes2 = key_text2.encode('utf-8')
    iv_bytes2 = iv_text2.encode('utf-8')
    
    session = requests.Session()
    apiurl0 = os.environ['bzy_url0']
    headers10 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    # apiurl = requests.get(apiurl0, headers=headers10).text
    # apiurl1=parse.urljoin(apiurl0, os.environ['bzy_url']) 
    apiurl2=parse.urljoin(apiurl0, os.environ['bzy_url2'])
    apiurl3=parse.urljoin(apiurl0, os.environ['bzy_url3'])
    headers = {
        'User-Agent': 'Octopus_Android',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    params = {  
    'password': '123456',
    'checkPassword': '123456',
    'invitationCode': '182227',
    'clientIp': '192.168.31.102',
    'from': '5',
    'androidDevice': uuid
    }
    paramss = aes_encrypt(key_bytes2, iv_bytes2, json.dumps(params))
    url = f'https://api.lead2win.cc:18003/netbarcloud/vpn/appRegister2?data={paramss}'
    # print(url)
    phonenm = session.post(url, headers=headers).json().get("data").get("phoneNumber")
    # phonenm = os.environ['bzy_email']
    # print(phonenm)
    url2 = apiurl2
    params2 = {
        'phoneNumber': aes_encrypt(key_bytes, iv_bytes, phonenm),
        'password': '255A42F2A6863798DBB392033F9D2FD7',
        'osType': 'android'
    }
    headers2 = {
        'User-Agent': 'Octopus_Android',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    response3 = requests.post(url2, headers=headers2, params=params2)
    phToken  = response3.json().get("data").get("phToken")
    token = response3.json().get("data").get("vpnToken")


    url5 = os.environ['bzy_url5']

    params5 = {
        "phoneNumber": mail,
        "vpnAccount": phonenm,
        "SMSCode": emailnator.get_verification_link(mail),
        "phToken": phToken,
    }

    response5 = requests.post(url5, params=params5, headers=headers2)
    # print(response5.text)
    # 设置请求参数
    params2 = {
        "phoneNumber": aes_encrypt(key_bytes, iv_bytes, mail),
        "password": "255A42F2A6863798DBB392033F9D2FD7",
        "osType": "android",
    }
    #response3 = requests.post(url2, headers=headers2, params=params2)
   phToken = response3.json().get("data").get("phToken")
   token = response3.json().get("data").get("vpnToken")

    url3 = apiurl3
    params3 = {
        'phToken': phToken,
        'phoneNumber': mail
    }
    headers3 = {
        'User-Agent': 'Octopus_Android',
        'token': token,
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }

    porxy_url = requests.post(url3, headers=headers3, params=params3).json().get("data").replace("\\", "")
    print(porxy_url)
    
    headers4 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    response = requests.get(porxy_url, headers=headers4).text
    abcd = base64.b64decode(response.encode('utf-8')).decode('utf-8').replace("\r\n", " @mfbpn\r\n")
    #print(base64.b64decode(response.encode('utf-8')).decode('utf-8').replace("\r\n", " @mfbpn\r\n"))

    abcd2 =abcd.replace("hk.bazhuayujiasu.cc", "tg_mfbpn.52cloud.us.kg")
    abcd3 = base64.b64encode(abcd2.encode('utf-8'))
    #print(abcd3)
    with open("./links/bbb", "wb") as f:
            f.write(abcd3)
    message = '#SS ' + '#订阅' + '\n' + datetime.now().strftime(
            "%Y年%m月%d日%H:%M:%S") + '\n' + 'bzy订阅每天自动更新bbb：' + '\n' + f'{porxy_url}'
    send_message(os.environ['chat_id'], message, os.environ['bot_token'])
