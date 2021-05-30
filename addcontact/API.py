import json
import requests
from addcontact.base import Base
import logging

logging.basicConfig(level=logging.DEBUG)


class AddContact(Base):

    def add_contact(self):
        # 添加成员
        # data = {"method": "post",
        #         "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
        #         "params": {"access_token": self.get_token()},
        #         "json": {"__userid": "huo",
        #                  "__name": "火狐",
        #                  "__department": [1],
        #                  "__mobile": "13423361236"}
        #
        #         }
        __url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        __userid = "huo"
        __name = "火狐"
        __department = [1]
        __mobile = "13423361236"
        r = requests.post(__url,
                          params={"access_token": self.get_token()},
                          json={"userid": __userid,
                                "name": __name,
                                "department": __department,
                                "mobile": __mobile
                                })
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        logging.info(f"错误日志信息：{r.json()}")
        return r

    def update_member(self):
        # 修改成员
        userid = "huo"
        name = "吃鸡"
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",
                          params={"access_token": self.get_token()},
                          json={"userid": userid, "name": name})
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def delete_member(self):
        # 删除成员
        userid = "huo"
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                         params={"access_token": self.get_token(), "userid": userid},
                         json={})
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def get_member(self):
        # 获取成员
        userid = "huo"
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",
                         params={"access_token": self.get_token(), "userid": userid},
                         json={})
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r
