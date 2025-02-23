import weakref

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel

from conf import config
from src.qt.util.qttask import QtTask
from src.server import Server, req
from src.user.user import User
from src.util.status import Status
from ui.login import Ui_Login
from PySide2 import QtWidgets


class QtLogin(QtWidgets.QWidget, Ui_Login):
    def __init__(self, owner):
        super(self.__class__, self).__init__(owner)
        Ui_Login.__init__(self)
        self.setupUi(self)
        self.owner = weakref.ref(owner)
        self.setWindowTitle("登陆")
        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.addButton(self.selectIp1)
        self.selectIp1.setChecked(True)

        self.speedTest = []
        self.speedIndex = 0

    def Login(self):
        self.SetSelectIp()
        userId = self.userIdEdit.text()
        passwd = self.passwdEdit.text()
        User().SetUserInfo(userId, passwd)
        QtTask().AddHttpTask(lambda x: User().Login(x), self.LoginBack)

        self.owner().loadingForm.show()
        # self.close()
        # self.owner().show()

    def LoginBack(self, msg):
        self.owner().loadingForm.close()
        if msg == Status.Ok:
            # self.close()
            self.owner().stackedWidget.setCurrentIndex(1)
            self.InitUser()
            self.owner().searchForm.InitKeyWord()
            self.owner().indexForm.Init()
        else:
            # QtWidgets.QMessageBox.information(self, '登陆失败', msg, QtWidgets.QMessageBox.Yes)
            self.owner().msgForm.ShowError("登陆失败, " + msg)

    def InitUser(self):
        self.owner().qtTask.AddHttpTask(lambda x: User().UpdateUserInfo(x), self.UpdateUserBack)
        return

    def UpdateUserBack(self, msg):
        self.owner().userForm.UpdateLabel(User().name, User().level, User().exp, User().title, User().isPunched)
        if not User().avatar:
            return

        url = User().avatar.get("fileServer")
        path = User().avatar.get("path")
        if url and path and config.IsLoadingPicture:
            self.owner().qtTask.AddDownloadTask(url, path, None, self.ShowUserImg)

    def ShowUserImg(self, data, st):
        if st == Status.Ok:
            self.owner().userForm.SetPicture(data)

    def OpenRegister(self):
        self.SetSelectIp()
        self.owner().registerForm.show()
        return

    def Init(self):
        self.owner().loadingForm.show()
        QtTask().AddHttpTask(lambda x: User().Init(x), self.InitBack)
        return

    def InitBack(self, msg):
        self.owner().loadingForm.close()
        if msg == Status.Ok:
            for index, ip in enumerate(User().addresss, 2):
                selectIp = QtWidgets.QRadioButton(self)
                selectIp.setObjectName("selectIp"+str(index))
                self.buttonGroup.addButton(selectIp)
                count = self.gridLayout_4.rowCount()
                self.gridLayout_4.addWidget(selectIp, count, 0, 1, 1)
                selectIp.setText("分流" + str(index))
            self.update()
        else:
            # QtWidgets.QMessageBox.information(self, , QtWidgets.QMessageBox.Yes)
            self.owner().msgForm.ShowError("无法获取哔咔分流列表")
        pass

    def SetSelectIp(self):
        index = int(self.buttonGroup.checkedButton().objectName().replace("selectIp", "")) - 1
        if index == 0:
            User().address = ""
        else:
            User().address = User().addresss[index-1]

    def SpeedTest(self):
        self.testSpeedButton.setEnabled(False)
        self.loginButton.setEnabled(False)
        self.registerButton.setEnabled(False)
        self.speedIndex = 0
        self.speedTest = []
        self.speedTest = [("", False), ("", True)]
        for address in User().addresss:
            self.speedTest.append((address, False))
            self.speedTest.append((address, True))
        for i in range(len(self.speedTest)):
            row = i // 2 + 1
            col = i % 2 + 1
            item = self.gridLayout_4.itemAtPosition(row, col)
            if item:
                item.widget().setText("")

        self.StartSpeedTest()

    def StartSpeedTest(self):
        if len(self.speedTest) <= self.speedIndex:
            self.testSpeedButton.setEnabled(True)
            self.loginButton.setEnabled(True)
            self.registerButton.setEnabled(True)
            return

        address, httpProxy = self.speedTest[self.speedIndex]
        if httpProxy and not config.HttpProxy:
            row = self.speedIndex // 2 + 1
            col = self.speedIndex % 2 + 1
            item = self.gridLayout_4.itemAtPosition(row, col)
            if item:
                item.widget().setText("无代理")
            else:
                label = QLabel("无代理")
                label.setAlignment(Qt.AlignCenter)
                self.gridLayout_4.addWidget(label, row, col, 1, 1)
            self.speedIndex += 1
            self.StartSpeedTest()
            return

        request = req.SpeedTestReq()
        # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDEyMjg3YzYxYWFlODJmZDJjMGQzNTUiLCJlbWFpbCI6InRvbnF1ZXIyIiwicm9sZSI6Im1lbWJlciIsIm5hbWUiOiJ0b25xdWVyMiIsInZlcnNpb24iOiIyLjIuMS4zLjMuNCIsImJ1aWxkVmVyc2lvbiI6IjQ1IiwicGxhdGZvcm0iOiJhbmRyb2lkIiwiaWF0IjoxNjE0MjQxODY1LCJleHAiOjE2MTQ4NDY2NjV9.ZUmRP319zREBHk3ax_dJh-qeUDFLmOg_RQBPAMWN8II"
        testIp = address
        index = self.speedIndex
        if httpProxy:
            request.proxy = {"http": config.HttpProxy, "https": config.HttpProxy}
        else:
            request.proxy = ""
        QtTask().AddHttpTask(lambda x: Server().TestSpeed(request, x, testIp), self.SpeedTestBack, index)
        return

    def SpeedTestBack(self, data, backParam):
        if not data:
            data = "超时"
        else:
            data = data

        row = self.speedIndex // 2 + 1
        col = self.speedIndex % 2 + 1
        item = self.gridLayout_4.itemAtPosition(row, col)
        if item:
            item.widget().setText(data)
        else:
            label = QLabel(data)
            label.setAlignment(Qt.AlignCenter)
            self.gridLayout_4.addWidget(label, row, col, 1, 1)
        self.speedIndex += 1
        self.StartSpeedTest()
        return
