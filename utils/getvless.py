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
from Telegram_bot import send_message

urllib3.disable_warnings()





def decrypt_rsa(data):
    key = RSA.importKey(base64.urlsafe_b64decode(private_key))
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(base64.b64decode(data))
    return decrypted_message.decode()



def decrypt_aes(data):
    key = private_key.encode('utf-8')
    iv = authorization.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(data)), AES.block_size)
    return decrypted_data.decode()


def get_node():
    url = api
    header =  {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 7.1.0; zh-cn; MI 9 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.5.5',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,en-US;q=0.8',
    }
    req = requests.post(url, data=text, headers=header, verify=False).json()
    node_info = decrypt_aes(req['data'])
    Vless = ''
    for server_list in json.loads(node_info):
        if server_list['title']:
            for title in server_list['title']:
                if title:
                    server = title['server']
                    ip = title['ip']
                    if ip:
                        url = f'https://ip125.com/api/{ip}?lang=zh-CN'
                        head = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                            'Cookie': '_ga=GA1.2.348223593.1668760697; _ga_XYJPKQNDKR=GS1.1.1669809730.4.1.1669809752.0.0.0; __gads=ID=e9cb6076c0188403-228d0f367edf00b9:T=1683097828:RT=1701660864:S=ALNI_MZoNQcRpP-66ZZidp6BAlct92mbOw; __gpi=UID=00000c011afd3f29:T=1683097828:RT=1701660864:S=ALNI_MZSTguCSNwyc6d4WgMIcm7m-Xepvg'
                        }
                        country_info = requests.get(url, headers=head).json()
                        address = country_info['country'] + country_info['city']
                        vless = 'ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU=' + '@' + ip + ':' + '443' + '#' + '%F0%9F%87%AD%F0%9F%87%B0%20%F0%9D%99%8F%F0%9D%99%82%40%F0%9D%99%88%F0%9D%99%81%F0%9D%98%BD%F0%9D%99%8B%F0%9D%99%89%200'
                        Vless += vless + '\n'
                    else:
                        print(server)
                else:
                    print(servers)
        else:
            print(server_list)
    with open("./links/vless", "w") as f:
        f.write(base64.b64encode(Vless.encode()).decode())


if __name__ == '__main__':
    api = os.environ['vless_api']
    private_key = os.environ['vless_private_key']
    authorization = os.environ['vless_authorization']
    get_node()
    message = '#vless ' + '#订阅' + '\n' + datetime.now().strftime("%Y年%m月%d日%H:%M:%S") + '\n' + 'vless订阅每天自动更新：' + '\n' + 'https://raw.githubusercontent.com/mfbpn/TrojanLinks/master/links/vless'
    send_message(os.environ['chat_id'], message, os.environ['bot_token'])
