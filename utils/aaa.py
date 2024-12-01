import requests
import yaml
import os
from datetime import datetime
import base64
from urllib.parse import quote

def parse_proxies_and_convert(url):
    SS_link = ""
    try:
        # 下载配置文件
        response = requests.get(url)
        response.raise_for_status()

        # 解析为字典
        config = yaml.safe_load(response.text)

        # 提取代理信息
        proxies = config.get("proxies", [])
        if not proxies:
            print("未找到代理信息")
            return

        # print("以下是转换后的SS链接：\n")
        for proxy in proxies:
            if proxy.get("type") == "ss":
                # 构造SS链接
                name = proxy.get("name")
                cipher = proxy.get("cipher")
                password = proxy.get("password")
                server = proxy.get("server")
                port = proxy.get("port")

                if all([cipher, password, server, port]):
                    credentials = f"{cipher}:{password}"
                    credentials_base64 = base64.urlsafe_b64encode(credentials.encode()).decode().rstrip('=')
                    name_encoded = quote(name)
                    # 构造 SS 链接
                    ss_link = f"ss://{credentials_base64}@{server}:{port}#{name_encoded} @mfbpn\n"
                    # SS_link += ss_link + " @mfbpn\n"
                    SS_link += ss_link
                    # print(ss_link)
                else:
                    print(f"代理 {name} 的信息不完整，跳过")
        print(SS_link)
        with open("./links/ss", "w") as f:
            f.write(base64.b64encode(SS_link.encode()).decode())
    except requests.RequestException as e:
        print(f"请求失败: {e}")
    except yaml.YAMLError as e:
        print(f"解析YAML失败: {e}")

SS_link = ""
# URL 指向目标配置文件
url = os.environ['bzydz_url']
parse_proxies_and_convert(url)

