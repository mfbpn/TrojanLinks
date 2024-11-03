import os
import requests
import json
import time
import uuid
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from datetime import datetime, timedelta
from Telegram_bot import send_message

# 解密函数
def encrypt_aes(data, key, iv):
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    ct_bytes = cipher.encrypt(pad(data.encode("utf-8"), AES.block_size))
    return base64.b64encode(ct_bytes).decode("utf-8")


def decrypt_aes(encrypted_data, key, iv):
    encrypted_bytes = base64.b64decode(encrypted_data)
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    decrypted_padded = cipher.decrypt(encrypted_bytes)
    decrypted = unpad(decrypted_padded, AES.block_size)
    return decrypted.decode("utf-8")


# 请求头
def prepare_headers(session, device_uuid):
    current_timestamp = str(int(time.time()))
    header_data = {
        "h-time": current_timestamp,
        "h-client": "android",
        "h-oem": "website",
        "jOlaWEOrIfkemD11xzNwyjNSijWwyzncv": device_uuid,
        "h-version": "2.2.3",
        "h-language": "CN",
    }
    key = iv = "ubje0xtjWTpZyGTV"
    encrypted_header = encrypt_aes(json.dumps(header_data), key, iv)
    #print(encrypted_header)
    return {"jOlaACOrIfkemD12xzNwxjNSijWwyzncv": encrypted_header}


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def lines_list(session, device_uuid, url):
    headers = prepare_headers(session, device_uuid)
    response = requests_retry_session(session=session).post(
        url, data={}, headers=headers, timeout=10
    )
    return response.text


def node_protocol(session, device_uuid, code, url):
    data = {"code": code}
    headers = prepare_headers(session, device_uuid)
    response = requests_retry_session(session=session).post(
        url, data=data, headers=headers, timeout=10
    )
    return response.text


# 保存节点
def save_to_file(urls):
    with open("赛盾.txt", "a", encoding="utf-8") as file:
        for url in urls:
            file.write(url + "\n")
    print("节点已经报保存到赛盾.txt文件")


# 生成随机ID
def load_or_generate_uuid():
    uuid_file = "device_uuid.txt"
    current_time = datetime.now()

    if os.path.exists(uuid_file):
        with open(uuid_file, "r") as file:
            lines = file.readlines()
            if len(lines) == 2:
                stored_uuid = lines[0].strip()
                stored_time = datetime.fromisoformat(lines[1].strip())

                # 检查是否已经过去 60 分钟
                if current_time - stored_time < timedelta(minutes=60):
                    return stored_uuid

    # 生成新的 UUID 并与当前时间一起保存
    new_uuid = str(uuid.uuid4())
    with open(uuid_file, "w") as file:
        file.write(new_uuid + "\n")
        file.write(current_time.isoformat() + "\n")
    return new_uuid


# 从 API 获取数据
def fetch_from_api(lines_list_url, node_protocol_url, device_uuid):
    session = requests.Session()
    urln = ''
    urls = []
    try:
        lines_list_result = lines_list(session, device_uuid, lines_list_url)
        # print(lines_list_result)
        linesOjb = json.loads(lines_list_result)
        nodes = linesOjb["result"]["nodes"]
        for n in nodes:
            code = n["code"]
            node_protocol_result = node_protocol(
                session, device_uuid, code, node_protocol_url
            )
            nodeProtocolObj = json.loads(node_protocol_result)
            #print(nodeProtocolObj)
            url = nodeProtocolObj["result"]["url"]
            decrypted_url = decrypt_aes(url, "TmPrPhkOf8by0cvx", "TmPrPhkOf8by0cvx")
            #print(decrypted_url)
            urls.append(decrypted_url)
    except Exception as e:
        print(f"API 发生错误: {e}")
    for url in urls:
        # urln += url.replace("InBzIjoiMSI", "InBzIjoi8J2ZqfCdmZxA8J2ZovCdmZvwnZmX8J2ZpfCdmaMi") + '\n'
        urln += url + ' @𝙢𝙛𝙗𝙥𝙣\n'
    print(urln)    
    with open("./links/sd2", "w") as f:
        f.write(base64.b64encode(urln.encode()).decode())
    #save_to_file(urls)


if __name__ == "__main__":
    # device_uuid = load_or_generate_uuid()
    device_uuid = os.environ['sd_uuid']
    # fetch_from_api(
    #     "http://api.saidun666.com/vpn/lines_list",
    #     "http://api.saidun666.com/vpn/node_protocol",
    #     device_uuid
    # )

    fetch_from_api(
        "http://api.deke7.cn/vpn/lines_list",
        "http://api.deke7.cn/vpn/node_protocol",
        device_uuid,
    )
