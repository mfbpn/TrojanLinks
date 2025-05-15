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
    c = os.environ['skr2_c']
    d = os.environ['skr_d']
    e = os.environ['skr_e']
    b = headers = {
        "User-Agent": "okhttp/3.8.0",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "devicetype": "1",
        "bundleid": "com.skr.shadowsocks",
        "appversion": "1.0.6",
        "accountid": "406496",
    }

def f(g, d, e):
    h = pyaes.AESModeOfOperationCBC(d, iv=e)
    i = b''.join(h.decrypt(g[j:j+16]) for j in range(0, len(g), 16))
    return i[:-i[-1]]

j = requests.post(a, headers=b, data=c)
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
  
