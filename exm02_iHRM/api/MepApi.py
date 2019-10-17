import logging

from day07.exm02_iHRM import app


class MepAUGD:
    """case 员工增删改查操作请求实现"""
    logging.info("执行员工增删改查操作")

    def add_api(self, session, username, mobile, timeOfEntry,
                formOfEmployment, workNumber, departmentName, departmentId, correctionTime):
        """增加员工操作请求实现"""
        add_json = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry": timeOfEntry,
                    "formOfEmployment": formOfEmployment,
                    "workNumber": workNumber,
                    "departmentName": departmentName,
                    "departmentId": departmentId,
                    "correctionTime": correctionTime
                    }

        return session.post(app.iHRM_url + "user", json=add_json,
                            headers={"Authorization": "Bearer " + app.Data_token})

    def updata_api(self, session, updata_json):
        """修改员工操作请求实现"""
        return session.put(app.iHRM_url + "user/" + app.Staff_id, json=updata_json,
                           headers={"Authorization": "Bearer " + app.Data_token})

    def get_api(self, session):
        """查看员工操作请求实现"""

        return session.get(app.iHRM_url + "user/" + app.Staff_id,
                           headers={"Authorization": "Bearer " + app.Data_token})

    def delete_api(self, session):
        """删除员工操作请求实现"""

        return session.delete(app.iHRM_url + "user/" + app.Staff_id,
                              headers={"Authorization": "Bearer " + app.Data_token})
