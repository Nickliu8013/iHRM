import logging

from day07.exm02_iHRM import app


class UserAPI:
    """case请求响应类"""

    def login(self, session, mobile, password):
        """登录请求响应 的方法"""
        logging.info("执行登录操作")

        json_login = {"mobile": mobile, "password": password}
        return session.post(app.iHRM_url + "login", json=json_login)
