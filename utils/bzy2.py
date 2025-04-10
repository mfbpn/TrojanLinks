import json
import os
import uuid
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


if __name__ == '__main__':
    def uuid_a():
        characters = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choice(characters) for i in range(8))
        return (random_string)
    uuid = uuid_a()
    def aes_encrypt(key: bytes, iv: bytes, plaintext: str) -> str:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = pad(plaintext.encode(), AES.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        return binascii.hexlify(ciphertext).decode().upper() # 强制大写字母

    key_text = os.environ['bzy2_key']
    iv_text = os.environ['bzy2_iv']
    key_bytes = key_text.encode('utf-8')
    iv_bytes = iv_text.encode('utf-8')
    key_text2 = os.environ['bzy2_key2']
    iv_text2 = os.environ['bzy2_iv2']
    key_bytes2 = key_text2.encode('utf-8')
    iv_bytes2 = iv_text2.encode('utf-8')
    
    session = requests.Session()
    # apiurl0 = os.environ['bzy_url0']
    headers10 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    # apiurl = requests.get(apiurl0, headers=headers10).text
    # apiurl1=parse.urljoin(apiurl0, os.environ['bzy_url']) 
    # apiurl2=parse.urljoin(apiurl0, os.environ['bzy2_url2'])
    # apiurl3=parse.urljoin(apiurl0, os.environ['bzy2_url3'])
    apiurl2= os.environ['bzy2_url2']
    apiurl3= os.environ['bzy2_url3']
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
    url = f'https://api.ymvpnpro.cc:8700/netbarcloud/vpn/appRegister2?data={paramss}'
    # print(url)
    phonenm = session.post(url, headers=headers).json().get("data").get("phoneNumber")
    # phonenm = os.environ['bzy_email']
    print(phonenm)
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
    url3 = apiurl3
    params3 = {
        'phToken': phToken,
        'phoneNumber': phonenm
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
    with open("./links/ss", "wb") as f:
            f.write(abcd3)
    message = '#SS ' + '#订阅' + '\n' + datetime.now().strftime(
            "%Y年%m月%d日%H:%M:%S") + '\n' + 'bzy订阅每天自动更新bbb：' + '\n' + f'{porxy_url}'
    send_message(os.environ['chat_id'], message, os.environ['bot_token'])
