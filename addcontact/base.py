import json

import requests


class Base:
    def get_token(self):
        # 获取token
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": "ww61442f3aeb23fddf",
                                 "corpsecret": "m9jRk5y10w58mSMKvB1a7ohXmaHrwzN2_Vtof2D-PlA"})
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()["errcode"] == 0
        self.token = r.json()["access_token"]  # token必须放在前置初始化里，不然其他用例无法复用token 容易忘记
        return self.token
