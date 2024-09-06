# -------------------------------------------------------------------------------
# Copyright (c) 2024. 挥杯劝, Inc. All Rights Reserved
# @作者         : 挥杯劝(Huibq)
# @邮件         : huibq120@gmail.com
# @文件         : TrojanLinks - get_ss.py
# @创建时间     : 2024/02/14 22:22
# -------------------------------------------------------------------------------
# -- coding: utf-8 --**
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
from Crypto.Util.Padding import pad, unpad
from binascii import a2b_hex, b2a_hex
import base64
from base64 import b64decode
from Telegram_bot import send_message

urllib3.disable_warnings()


# def encode_url(input_str):
#     return urllib.parse.quote(input_str, safe='')


# class AESCipher:
#     def __init__(self, key):
#         md5_hash = MD5.new()
#         md5_hash.update(key.encode('utf-8'))
#         self.key = md5_hash.digest()

#     def encrypt(self, data):
#         cipher = AES.new(self.key, AES.MODE_GCM, nonce=ss_iv.encode('utf-8'))
#         encrypted_bytes, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
#         return base64.b64encode(encrypted_bytes + tag).decode('utf-8')

#     def decrypt(self, data):
#         try:
#             data_bytes = base64.b64decode(data.encode('utf-8'))
#             cipher = AES.new(self.key, AES.MODE_GCM, nonce=ss_iv.encode('utf-8'))
#             decrypted_bytes = cipher.decrypt_and_verify(data_bytes[:-16], data_bytes[-16:])
#             return decrypted_bytes.decode('utf-8')
#         except Exception as e:
#             print("Error during decryption:", e)
#             return None


# def encode(s):
#     cipher = AESCipher(ss_key)
#     return cipher.encrypt(s)


# def decode(s):
#     cipher = AESCipher(ss_key)
#     return cipher.decrypt(s)


# def get_address(ip):
#     tap_url = f'https://ip125.com/api/{ip}?lang=zh-CN'
#     head = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
#         'Cookie': '_ga=GA1.2.348223593.1668760697; _ga_XYJPKQNDKR=GS1.1.1669809730.4.1.1669809752.0.0.0; __gads=ID=e9cb6076c0188403-228d0f367edf00b9:T=1683097828:RT=1701660864:S=ALNI_MZoNQcRpP-66ZZidp6BAlct92mbOw; __gpi=UID=00000c011afd3f29:T=1683097828:RT=1701660864:S=ALNI_MZSTguCSNwyc6d4WgMIcm7m-Xepvg'
#     }
#     country_info = requests.get(tap_url, headers=head).json()
#     return country_info['query']
# def get_node():
#     url = api
#     headers = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; MI 9 MIUI/20.9.4)"}
#     req = requests.get(url, headers=headers, verify=False).content
#     #print(req)
#     node_list = json.loads(str(decrypt_aes(req)))['data']
    # Vless = ''
#     for i in node_list :
#         host = i['ip']
#         vless = 'ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU=' + '@' + host + ':' + '443' + '#' + '%F0%9F%87%AD%F0%9F%87%B0%20%F0%9D%99%8F%F0%9D%99%82%40%F0%9D%99%88%F0%9D%99%81%F0%9D%98%BD%F0%9D%99%8B%F0%9D%99%89'
#         Vless += vless + '\n'
#         if i == node_list[11]:
#             break
#     with open("./links/vless", "w") as f:
#         f.write(base64.b64encode(Vless.encode()).decode())
#     return None

if __name__ == '__main__':
	data = {
	'LANG': 'CN',
	'server_type': 'WG'
	}
	node_list = requests.post(os.environ['ss_url'], data=data, headers=json.loads(os.environ['ss_headers']), verify=Ture)
	nodetest = node_list.text
	#print(json.loads(str(node_list)))
	print(nodetest)
	Vless = ''
	# for i in node_list :
	# 	if json.loads(i)['server_type'] == "SSR":
	# 		host = json.loads(i)['server_domain']
	# 		port = json.loads(i)['server_port']
	# 		vless = 'ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU=' + '@' + host + ':' + port + '#' + '%F0%9F%87%AD%F0%9F%87%B0%20%F0%9D%99%8F%F0%9D%99%82%40%F0%9D%99%88%F0%9D%99%81%F0%9D%98%BD%F0%9D%99%8B%F0%9D%99%89'
	# 		Vless += vless + '\n'
	# 	else:
	# 		print(server)
	with open("./links/ss", "w") as f:
		f.write(nodetest)
		# f.write(base64.b64encode(Vless.encode()).decode())
	#return None
	message = '#ss ' + '#订阅' + '\n' + datetime.now().strftime("%Y年%m月%d日%H:%M:%S") + '\n' + 'ss' + '\n' + 'https://raw.githubusercontent.com/mfbpn/TrojanLinks/master/links/ss'
	send_message(os.environ['chat_id'], message, os.environ['bot_token'])
	
