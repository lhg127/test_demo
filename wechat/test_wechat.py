from wechat.wechat_data import TestWe


class TestWechat:
    def setup_class(self):
        self.wechat = TestWe()
        self.wechat.get_token()

    def test_search(self):
        r = self.wechat.test_search()
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0

    def test_add(self):
        __group = "组名"
        __nam = "表情1"
        r = self.wechat.test_add(__group, __nam)
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        # 断言json体里的["group_name"] == "组名"
        assert r.json()["tag_group"]["group_name"] == "组名"

    def test_delete(self):
        __del_id = "etxlQuEAAAWyZRfHNLBxnBhP3Goh2drA"
        r = self.wechat.test_delete(__del_id)
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        # 断言json体里的["errmsg"] == "ok"
        assert r.json()["errmsg"] == "ok"

    def test_edit(self):
        __test_id = "etxlQuEAAAGTgm3bHEgiE4J-bKDDpUlw"
        __test_name = "美女"
        r = self.wechat.test_edit(__test_id, __test_name)
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
