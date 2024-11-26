# doc: https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN?lang=en-US

# Test
# curl -X POST -H "Content-Type: application/json" \
# 	-d '{"msg_type":"text","content":{"text":"Task completed: well done! please check your email ~"}}' \
#   https://open.feishu.cn/open-apis/bot/v2/hook/{ID}

import base64
import hashlib
import hmac
from datetime import datetime

import requests

# replace your own webhook url
WEBHOOK_URL = 'TODO'


class LarkBot:
    def __init__(self, secret: str) -> None:
        if not secret:
            raise ValueError("invalid secret key")
        self.secret = secret

    def gen_sign(self, timestamp: int) -> str:
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        hmac_code = hmac.new(
            string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
        ).digest()
        sign = base64.b64encode(hmac_code).decode('utf-8')

        return sign

    def send(self, content: str) -> None:
        timestamp = int(datetime.now().timestamp())
        sign = self.gen_sign(timestamp)

        params = {
            "timestamp": timestamp,
            "sign": sign,
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "TASK COMPLETED: ",
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "text": content
                                }
                            ]
                        ]
                    }
                }
            }
        }
        resp = requests.post(url=WEBHOOK_URL, json=params)
        resp.raise_for_status()
        result = resp.json()
        if result.get("code") and result["code"] != 0:
            print(result["msg"])
            return
        print("消息发送成功")
