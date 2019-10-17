# 封装url
import logging
import os
import time
from logging import handlers

iHRM_url = "http://182.92.81.159/api/sys/"

# 动态获取绝对路径
PRO_PAIH = os.path.dirname(os.path.abspath(__file__))

Data_token = None
Staff_id = None


def my_bog_config():
    """设置日志方法"""
    # 获取日志对象
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 设置日志处理器（控制输出目标）

    to1 = logging.StreamHandler()
    filename = PRO_PAIH + "/log/iHRM日志{}".format(time.strftime("%H%M%S")) + ".log"
    to2 = logging.handlers.TimedRotatingFileHandler(filename=filename, when="h", interval=24, backupCount=5,
                                                    encoding="utf-8")
    # 设置格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 组织上述对象
    to1.setFormatter(formatter)
    to2.setFormatter(formatter)
    logger.addHandler(to1)
    logger.addHandler(to2)
