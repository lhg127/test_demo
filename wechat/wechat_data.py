import json

import requests


class TestWe:
    def setup_class(self):
        # 初始化获取token，不需要重复打开，复用就可以了
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params={
            "corpid": "ww61442f3aeb23fddf",
            "corpsecret": "cc6jz0BqLtOzhg-1olH-2AE7l-iwKeSHkbz0DuK5iJw"})
        # 以json格式显示响应数据
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        # 将token保存，供下个函数调用，复用此token
        self.token = r.json()["access_token"]

    def get_token(self):
        # --------供代码优化使用，不能于上面的同时使用---------
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params={
            "corpid": "ww61442f3aeb23fddf",
            "corpsecret": "cc6jz0BqLtOzhg-1olH-2AE7l-iwKeSHkbz0DuK5iJw"})
        # 以json格式显示响应数据
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        # 将token保存，供下个函数调用，复用此token
        self.token = r.json()["access_token"]

    def test_add(self, group, nam):
        # 添加标签，用post，在json里新增标签数据
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params={"access_token": self.token},
                          # 由于是新建标签，所以group_name，group_id必须的添加一个，不然会报40063
                          json={"group_name": group, "tag": [{"name": nam}]})
        # 以json格式显示响应数据
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        # 断言json体里的["group_name"] == "组名"
        assert r.json()["tag_group"]["group_name"] == "组名"
        return r

    def test_edit(self, test_id, test_name):
        # 编辑标签,在json体添加id和新名称
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                          params={"access_token": self.token},
                          json={"id": test_id, "name": test_name})
        # 以json格式显示响应数据
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        return r

    def test_delete(self, del_id):
        # 删除标签，在json体添加需要删除的id
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                          params={"access_token": self.token},
                          json={"tag_id": [del_id]})
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        # 断言json体里的["errmsg"] == "ok"
        assert r.json()["errmsg"] == "ok"
        return r

    def test_search(self):
        # 获取标签
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                          params={"access_token": self.token},
                          # json为空表示获取全部标签id，组id
                          json={})
        # 以json格式显示响应数据
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        return r
