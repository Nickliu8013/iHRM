import json
import logging
import unittest
import requests
from parameterized import parameterized

from day07.exm02_iHRM import app
from day07.exm02_iHRM.api.User_API import UserAPI
from day07.exm02_iHRM.app import PRO_PAIH


def login_json():
    """解析json文件"""
    json_login = []
    with open(PRO_PAIH + "/data/iHRM_login_data.json"
            , encoding="utf-8") as data_json:
        json01 = json.load(data_json)
        for value in json01.values():
            json_login.append((value.get("mobile"),
                               value.get("password"),
                               value.get("success"),
                               value.get("code"),
                               value.get("message")))
        # print(json_login)
        return json_login


class TestIhrm(unittest.TestCase):
    """定义登录接口测试类"""

    def setUp(self):
        """初始化url"""
        self.session = requests.Session()
        self.user_api = UserAPI()

    def tearDown(self):
        """销毁资源"""
        self.session.close()

    @parameterized.expand(login_json)
    def test_login(self, mobile, password, success, code, message):
        """登录接口测试方法"""
        js = self.user_api.login(self.session, mobile, password)

        # 断言
        self.assertEqual(success, js.json().get("success"))
        self.assertEqual(code, js.json().get("code"))
        self.assertIn(message, js.json().get("message"))

    def test_login_correct(self):
        """登录成功接口"""
        print("*" * 100)
        login_correct = self.user_api.login(self.session, "13800000002", "123456")
        logging.info("执行登录操作")

        print(login_correct.json())

        # 断言

        self.assertEqual(True, login_correct.json().get("success"))
        self.assertEqual(10000, login_correct.json().get("code"))
        self.assertIn("操作成功", login_correct.json().get("message"))
        login_data = login_correct.json().get("data")
        print(login_data)
        app.Data_token = login_data
