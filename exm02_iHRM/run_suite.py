import unittest
import time
from BeautifulReport import BeautifulReport
from day07.exm02_iHRM.case.TestEmp import TestEmp
from day07.exm02_iHRM.case.TestiHRMLogin import TestIhrm

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIhrm))
suite.addTest(TestIhrm("test_login_correct"))
suite.addTest(TestEmp("test_add_01_mep"))
suite.addTest(TestEmp("test_update_02_mep"))
suite.addTest(TestEmp("test_get_03_mep"))
suite.addTest(TestEmp("test_delete_04_mep"))

repot = "黑马iHRM{}.html".format(time.strftime("%Y%m%d%H%M%S"))
BeautifulReport(suite).report(filename=repot, log_path="./report", description="人力资源登录测试")

print("11")