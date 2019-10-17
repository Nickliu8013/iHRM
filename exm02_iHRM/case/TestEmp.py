import unittest
import requests

from day07.exm02_iHRM import app
from day07.exm02_iHRM.api.MepApi import MepAUGD


class TestEmp(unittest.TestCase):
    """定义增删改查的测试类"""

    def setUp(self):
        """初始化api"""
        self.session = requests.Session()
        self.login_correct = MepAUGD()

    def tearDown(self):
        """销毁资源"""
        self.session.close()

    def test_add_01_mep(self):
        """添加员工操作"""
        add_mep = self.login_correct.add_api(self.session,
                                             "F35",
                                             "13145205351",
                                             "2019-10-07",
                                             1,
                                             "13145205201",
                                             "查水表",
                                             "1066238836272664576",
                                             "2022-10-05T16:00:00.000Z"
                                             )

        # 断言

        self.assertEqual(10000, add_mep.json().get("code"))
        self.assertEqual(True, add_mep.json().get("success"))
        self.assertIn("操作成功", add_mep.json().get("message"))
        app.Staff_id = add_mep.json().get("data").get("id")

    def test_update_02_mep(self):
        """修改员工"""
        # 请求业务
        updata = {"username": "F22"}
        updata_mep = self.login_correct.updata_api(self.session, updata)

        # 断言
        updata_json = updata_mep.json()
        self.assertEqual(True, updata_json.get("success"))
        self.assertEqual(10000, updata_json.get("code"))
        self.assertIn("操作成功", updata_json.get("message"))

    def test_get_03_mep(self):
        """查询员工"""
        get_mep = self.login_correct.get_api(self.session)

        # 断言
        get_json = get_mep.json()
        self.assertEqual(True, get_json.get("success"))
        self.assertEqual(10000, get_json.get("code"))
        self.assertIn("操作成功", get_json.get("message"))

    def test_delete_04_mep(self):
        """删除员工"""
        delete_mep=self.login_correct.delete_api(self.session)

        # 断言
        delete_json=delete_mep.json()
        self.assertEqual(True, delete_json.get("success"))
        self.assertEqual(10000, delete_json.get("code"))
        self.assertIn("操作成功", delete_json.get("message"))