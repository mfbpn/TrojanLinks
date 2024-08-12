# -------------------------------------------------------------------------------
# Copyright (c) 2024. 挥杯劝, Inc. All Rights Reserved
# @作者         : 挥杯劝(Huibq)
# @邮件         : huibq120@gmail.com
# @文件         : TrojanLinks - getvless.py
# @创建时间     : 2024/01/10 20:08
# -------------------------------------------------------------------------------
import json
import os
import time
import uuid
from datetime import datetime
import requests
import urllib3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Util.Padding import unpad
import base64
from base64 import b64decode
from Telegram_bot import send_message

urllib3.disable_warnings()


class AESCipher:
    def __init__(self, key):
        md5_hash = MD5.new()
        md5_hash.update(key.encode('utf-8'))
        self.key = md5_hash.digest()

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=authorization.encode('utf-8'))
        encrypted_bytes, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
        return base64.b64encode(encrypted_bytes + tag).decode('utf-8')

    def decrypt(self, data):
        try:
            data_bytes = base64.b64decode(data.encode('utf-8'))
            cipher = AES.new(self.key, AES.MODE_GCM, nonce=authorization.encode('utf-8'))
            decrypted_bytes = cipher.decrypt_and_verify(data_bytes[:-16], data_bytes[-16:])
            return decrypted_bytes.decode('utf-8')
        except Exception as e:
            print("Error during decryption:", e)
            return None


def encode(s):
    cipher = AESCipher(private_key)
    return cipher.encrypt(s)


def decode(s):
    cipher = AESCipher(private_key)
    return cipher.decrypt(s)



def get_node():
    url = api
    headers = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; MI 9 MIUI/20.9.4)"}
    req = requests.get(url, headers=headers).text
    node_list = json.loads(decode(req))['title']
    Vless = ''
    for i in node_list :
        host = i['ip']
        vless = 'ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU=' + '@' + host + ':' + '443' + '#' + '%F0%9F%87%AD%F0%9F%87%B0%20%F0%9D%99%8F%F0%9D%99%82%40%F0%9D%99%88%F0%9D%99%81%F0%9D%98%BD%F0%9D%99%8B%F0%9D%99%89%200'
        Vless += vless + '\n'
        if i == node_list[11]:
            break
    with open("./links/vless", "w") as f:
        f.write(base64.b64encode(Vless.encode()).decode())
    return None

if __name__ == '__main__':
    api = os.environ['vless_api']
    private_key = os.environ['vless_private_key']
    authorization = os.environ['vless_authorization']
    #text = os.environ['vless_text']
    #invite()
    get_node()
    message = '#vless ' + '#订阅' + '\n' + datetime.now().strftime("%Y年%m月%d日%H:%M:%S") + '\n' + 'vless订阅每天自动更新：' + '\n' + 'https://raw.githubusercontent.com/mfbpn/TrojanLinks/master/links/vless'
    send_message(os.environ['chat_id'], message, os.environ['bot_token'])
