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
import base64
import pyaes

# def show_author_info():
#     print("""
# ====================================================
# |                                                  |
# |          作者: iu                                 |
# |          项目: 提取spvpn                          |
# |          GitHub: https://github.com/Yu9191        |
# |          Version: 1.0.0                          |
# |          日期: 2024-10-16                        |
# |                                                  |
# ====================================================
#     """)

# a = "c3e7254f65b8c39e9d6391fd422140f3"
# b = "3648425794742788096" 
a = os.environ['sp_a']
b = os.environ['sp_b']
Fuckme = []
def c(d, e, f):
    d = base64.b64decode(d)
    aes = pyaes.AESModeOfOperationCBC(e, iv=f)
    decrypted = b""
    while d:
        decrypted += aes.decrypt(d[:16])
        d = d[16:]
    padding_len = decrypted[-1]
    return decrypted[:-padding_len].decode('utf-8')

def i():
    # j = "https://api.9527.click/v2/node/list"
    j = os.environ['sp_j']
    k = {
        'Host': 'api.9527.click',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'International/3.3.35 (iPhone; iOS 18.0.1; Scale/3.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    # k = os.environ['sp_k']
    # l = os.environ['sp_l']
    l = {
        "key": "G8Jxb2YtcONGmQwN7b5odg==",
        "uid": b,
        "vercode": "1",
        "uuid": "0273F74A-3F2E-44FB-8F87-717C9E3518E3"
    }

    m = requests.post(j, headers=k, json=l)
    if m.status_code == 200:
        return json.loads(m.text)
    else:
        print(f"fw: {m.status_code}")
        return None

def n():
    o = b'VXH2THdPBsHEp+TY'
    p = b'VXH2THdPBsHEp+TY'
    q = i()
    if not q:
        print("dashabi")
        return
    if 'data' not in q:
        print("dashabi")
        return
    for r in q['data']:
        if 'ip' in r and r['ip']:
            r['ip'] = c(r['ip'], o, p)
        if 'host' in r and r['host']:
            r['host'] = c(r['host'], o, p)
        if 'ov_host' in r and r['ov_host']:
            r['ov_host'] = c(r['ov_host'], o, p)
        s = r.get('host') or r.get('ip')
        t = r.get('name', 'sb')
        u = f"trojan://{b}@{s}:443?allowInsecure=1#{t}"
        Fuckme.append(u)
    print(Fuckme)
    with open("./links/sp", "w") as f:
            f.write(Fuckme)
        
    # with open('Fuckme.txt', 'w') as f:
    #     for link in Fuckme:
    #         f.write(link + '\n')

if __name__ == "__main__":
    #show_author_info()  
    n()
