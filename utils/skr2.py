import os
import time
import uuid
import urllib3

from base64 import b64decode
from Telegram_bot import send_message

import requests
import base64
import json
import pyaes
import binascii
from datetime import datetime

if __name__ == '__main__':
    a = os.environ['skr_a']
    # c = os.environ['skr2_c']
    c = {
        "time": "1747303695",
        "token": "99fa19a64cfb4674bd5fc1a10ec1740f",
        "data": "8F1352301A8D4B4F6F80A6DDC2A8E7FB096CE5FE65D6D7AF1230BC6EE07944AFA2767165897426386AEACDD208858AA10BF5CDC6B59801936A4D5905A23629B9915CC8464FAB3D037A29DC0501FE80F6D3681B6BE6C876842BFA8671B80FACAA485F7F9A12F06B94759BB42962AA7388",
    }
    d = os.environ['skr_d']
    e = os.environ['skr_e']
    b = {
        "User-Agent": "okhttp/3.8.0",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "devicetype": "1",
        "bundleid": "com.skr.shadowsocks",
        "appversion": "1.0.6",

    }

def f(g, d, e):
    h = pyaes.AESModeOfOperationCBC(d, iv=e)
    i = b''.join(h.decrypt(g[j:j+16]) for j in range(0, len(g), 16))
    return i[:-i[-1]]

j = requests.post(a, headers=b, data=c)
print(j.text)
skr = ''
if j.status_code == 200:
    k = j.text.strip()
    l = binascii.unhexlify(k)
    m = f(l, d.encode(), e.encode())
    n = json.loads(m)
    for o in n['data']:
        p = f"aes-256-cfb:{o['password']}@{o['ip']}:{o['port']}"
        q = base64.b64encode(p.encode('utf-8')).decode('utf-8')
        r = f"ss://{q}#{o['title']}"
        skr += r + ' @mfbpn\n'
    print(skr)
    with open("./links/skr", "w") as f:
        f.write(base64.b64encode(skr.encode()).decode())
    message = '#ss ' + '#订阅' + '\n' + datetime.now().strftime("%Y年%m月%d日%H:%M:%S") + '\n' + 'skr订阅每天自动更新：' + '\n' + 'https://raw.githubusercontent.com/mfbpn/TrojanLinks/master/links/skr'
    send_message(os.environ['chat_id'], message, os.environ['bot_token'])
  
