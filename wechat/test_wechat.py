import pytest

from wechat.wechat_data import TestWe


class TestWechat:
    def setup_class(self):
        self.wechat = TestWe()
        self.wechat.get_token()

    def test_search(self):
        # 获取所有标签
        r = self.wechat.test_search()
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0

    @pytest.mark.parametrize("group,nam", [["测试", "试点5"]])
    def test_add(self, group, nam):
        r = self.wechat.test_add(group, nam)
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        # 断言json体里的["group_name"] == "测试"
        assert r.json()["tag_group"]["group_name"] == "测试"

    @pytest.mark.parametrize("del_id", [["etxlQuEAAAd5W209w3rFSRfiDnvODdOQ"]])
    def test_delete(self, del_id):
        # __del_id = "etxlQuEAAAWyZRfHNLBxnBhP3Goh2drA"
        r = self.wechat.test_delete(del_id)
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
        # 断言json体里的["errmsg"] == "ok"
        assert r.json()["errmsg"] == "ok"

    @pytest.mark.parametrize("test_id,test_name", [["etxlQuEAAAz6N5Ely_RcMu6-2ratl8Ow", "哈哈"]])
    def test_edit(self, test_id, test_name):
        # __test_id = "etxlQuEAAAGTgm3bHEgiE4J-bKDDpUlw"
        # __test_name = "美女"
        r = self.wechat.test_edit(test_id, test_name)
        # 断言json体里的["errcode"] == 0
        assert r.json()["errcode"] == 0
