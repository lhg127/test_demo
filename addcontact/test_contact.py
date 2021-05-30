import pytest
from addcontact.API import AddContact
from addcontact.base import Base
import allure


class TestContact:
    def setup_class(self):
        self.contact = AddContact()
        self.token = Base()
        self.token.get_token()

    @pytest.mark.run(order=1)
    @allure.feature("添加成员")
    @allure.step("添加步骤")
    def test_add_contacts(self):
        # 添加成员
        r = self.contact.add_contact()
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "created"

    @pytest.mark.run(order=2)
    @allure.feature("获取成员")
    @allure.step("详细步骤")
    def test_get_member(self):
        # 获取成员
        r = self.contact.get_member()
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "ok"

    @pytest.mark.run(order=4)
    @allure.feature("删除成员")
    @allure.step("删除步骤")
    def test_delete_member(self):
        # 删除成员
        r = self.contact.delete_member()
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "deleted"

    @pytest.mark.run(order=3)
    @allure.feature("修改成员")
    @allure.step("修改成员步骤")
    def test_update_member(self):
        # 修改成员
        r = self.contact.update_member()
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "updated"
