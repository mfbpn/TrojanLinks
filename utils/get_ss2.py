# -------------------------------------------------------------------------------
# Copyright (c) 2024. 挥杯劝, Inc. All Rights Reserved
# @作者         : 挥杯劝(Huibq)
# @邮件         : huibq120@gmail.com
# @文件         : TrojanLinks - get_ss.py
# @创建时间     : 2024/02/14 22:22
# -------------------------------------------------------------------------------
import json
import os
import uuid
from datetime import datetime
import urllib3
from Crypto.Hash import MD5
from Crypto.Cipher import AES
#import urllib.parse
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



urllib3.disable_warnings()




if __name__ == '__main__':
    # ss_key = os.environ['ss_key']
    # ss_iv = os.environ['ss_iv']
    # 随机生成8位字符串
    def uuid_a():
        characters = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choice(characters) for i in range(8))
        return (random_string)

    uuid = uuid_a()

    # AES加密
    def aes_encrypt(key: bytes, iv: bytes, plaintext: str) -> str:
        # 创建 AES 加密器
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # 对明文进行填充
        padded_plaintext = pad(plaintext.encode(), AES.block_size)
        
        # 加密数据
        ciphertext = cipher.encrypt(padded_plaintext)
        
        # 返回十六进制编码的密文
        return binascii.hexlify(ciphertext).decode().upper() # 强制大写字母

    # 转换密钥和 IV
    key_text = "rwb6c4e7fz$6el%0"
    iv_text = "z1b6c3t4e5f6k7w8"

    # 转换为字节
    key_bytes = key_text.encode('utf-8')
    iv_bytes = iv_text.encode('utf-8')

    # 创建会话以确保连接保持打开状态
    session = requests.Session()

    # 自定义请求头
    headers = {
        'User-Agent': 'Octopus_Android',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # URL 和参数
    url = "https://app.bazhuayujiasu.cc:18001/netbarcloud/vpn/octopusRegister.do"
    params = {
        'phoneNumber': uuid,
        'password': '123456',
        'checkPassword': '123456',
        'id': '982228',
        'clientIp': '192.168.31.102',
        'from': '5'
    }

    # 发送 POST 请求
    token = session.post(url, headers=headers, params=params).json().get("userid")


    # 定义 URL 和参数
    url2 = "https://app.bazhuayujiasu.cc:18001/netbarcloud/vpn/phLogin.do"

    # 设置请求参数
    params2 = {
        'phoneNumber': aes_encrypt(key_bytes, iv_bytes, uuid),
        'password': '255A42F2A6863798DBB392033F9D2FD7',
        'osType': 'android'
    }

    # 设置请求头
    headers2 = {
        'User-Agent': 'Octopus_Android',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }

    # 发送 POST 请求
    response3 = requests.post(url2, headers=headers2, params=params2)
    phToken  = response3.json().get("data").get("phToken")
    token = response3.json().get("data").get("vpnToken")

    # 定义URL和参数
    url3 = "https://app.bazhuayujiasu.cc:18001/netbarcloud/vpn/airportNode.do"

    # 设置请求参数
    params3 = {
        'phToken': phToken,
        'phoneNumber': uuid
    }

    # 设置请求头
    headers3 = {
        'User-Agent': 'Octopus_Android',
        'token': token,
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }

    # 发送 POST 请求
    porxy_url = requests.post(url3, headers=headers3, params=params3).json().get("data").replace("\\", "")

    # 输出响应内容
    print(porxy_url)



    # 定义 URL 和参数
    url = "https://www.otcopusapp.cc/lx3af288h5i8pz380/api/v1/client/subscribe"
    params = {
        'token': '1d045ac3eba05ddc55477f1634625683'
    }

    # 设置请求头
    headers4 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    # 发送 GET 请求
    response = requests.get(porxy_url, headers=headers4).text
    # print(base64.b64decode(response))
    #print(re.sub('#(.*)\\r\\n', 'tg@mfbpn\r\n', base64.b64decode(response)))
    abcd = base64.b64decode(response.encode('utf-8')).decode('utf-8').replace("\r\n", " tg@mfbpn\r\n")
    #print(base64.b64decode(response.encode('utf-8')).decode('utf-8').replace("\r\n", " tg@mfbpn\r\n"))

    abcd2 =abcd.replace("hk.bazhuayujiasu.cc", "tg_mfbpn.52cloud.us.kg")
    abcd3 = base64.b64encode(abcd2.encode('utf-8'))
    print(abcd3)

    with open("./links/ss", "wb") as f:
            f.write(abcd3)
    message = '#vmess ' + '#订阅' + '\n' + datetime.now().strftime(
            "%Y年%m月%d日%H:%M:%S") + '\n' + 'vmess订阅每35分钟自动更新：' + '\n' + 'https://raw.githubusercontent.com/mfbpn/TrojanLinks/master/links/ss'
    send_message(os.environ['chat_id'], message, os.environ['bot_token'])

    # ss_key = os.environ['ss_key']
    # ss_iv = os.environ['ss_iv']
    # userinfo = json.loads(os.environ['ss_userinfo'])
    # userinfo['uuid'] = str(uuid.uuid4()).replace('-', '')
    # encoded_str = encode_url(encode(json.dumps(userinfo, separators=(',', ':'), ensure_ascii=False)))
    # text = requests.post(os.environ['ss_url'], data=f'value={encoded_str}', headers=json.loads(os.environ['ss_headers']), verify=False).text
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari'
    # }
    # ss = ''
    # for line in base64.b64decode(requests.get(json.loads(decode(text))['data']['data']['token'][1], headers=headers, verify=False).text).decode('utf-8').split('\n')[3:-1]:
    #     domain = line.strip().split('@')[1].split(':')[0]
    #     ss += line.replace(domain, get_address(domain)).strip() + '|Github%E6%90%9C%E7%B4%A2TrojanLinks\n'
    # with open("./links/ss", "w") as f:
    #     f.write(base64.b64encode(ss.encode()).decode())
    # message = '#ss ' + '#订阅' + '\n' + datetime.now().strftime(
    #     "%Y年%m月%d日%H:%M:%S") + '\n' + 'ss订阅每35分钟自动更新：' + '\n' + 'https://raw.githubusercontent.com/mfbpn/TrojanLinks/master/links/ss'
    # send_message(os.environ['chat_id'], message, os.environ['bot_token'])
