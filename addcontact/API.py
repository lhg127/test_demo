import json
from addcontact.base import Base
import logging
from addcontact.base_api import BaseApi

logging.basicConfig(level=logging.DEBUG)


class AddContact(Base, BaseApi):

    def add_contact(self):
        # 添加成员
        __url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        __userid = "huo"
        __name = "火狐"
        __department = [1]
        __mobile = "13423361236"

        data = {"method": "post",
                "url": __url,
                "params": {"access_token": self.get_token()},
                "json": {"userid": __userid,
                         "name": __name,
                         "department": __department,
                         "mobile": __mobile}}
        r = self.request(data)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        logging.info(f"添加成员日志:{data}")
        return r

    def update_member(self):
        # 修改成员
        __url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        __userid = "huo"
        __name = "吃鸡"

        data = {"method": "post",
                "url": __url,
                "params": {"access_token": self.get_token()},
                "json": {"userid": __userid, "name": __name}}
        r = self.request(data)
        logging.info(f"更新成员日志：{data}")
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def delete_member(self):
        # 删除成员
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        userid = "huo"

        data = {"method": "get",
                "url": url,
                "params": {"access_token": self.get_token(), "userid": userid},
                "json": {}}
        r = self.request(data)
        logging.info(f"删除成员日志：{data}")
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def get_member(self):
        # 获取成员
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        userid = "huo"

        data = {"method": "get",
                "url": url,
                "params": {"access_token": self.get_token(), "userid": userid},
                "json": {}}
        r = self.request(data)
        logging.info(f"获取成员日志{data}")
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r
