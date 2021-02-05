# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(456, 154)
        self.gridLayout_2 = QtWidgets.QGridLayout(Setting)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Setting)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(Setting)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Setting)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quality_original = QtWidgets.QRadioButton(Setting)
        self.quality_original.setObjectName("quality_original")
        self.buttonGroup = QtWidgets.QButtonGroup(Setting)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.quality_original)
        self.horizontalLayout.addWidget(self.quality_original)
        self.quality_high = QtWidgets.QRadioButton(Setting)
        self.quality_high.setObjectName("quality_high")
        self.buttonGroup.addButton(self.quality_high)
        self.horizontalLayout.addWidget(self.quality_high)
        self.quality_medium = QtWidgets.QRadioButton(Setting)
        self.quality_medium.setObjectName("quality_medium")
        self.buttonGroup.addButton(self.quality_medium)
        self.horizontalLayout.addWidget(self.quality_medium)
        self.quality_low = QtWidgets.QRadioButton(Setting)
        self.quality_low.setObjectName("quality_low")
        self.buttonGroup.addButton(self.quality_low)
        self.horizontalLayout.addWidget(self.quality_low)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Setting)
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Setting)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Setting)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.httpEdit = QtWidgets.QLineEdit(Setting)
        self.httpEdit.setObjectName("httpEdit")
        self.gridLayout_3.addWidget(self.httpEdit, 1, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveEdit = QtWidgets.QLineEdit(Setting)
        self.saveEdit.setObjectName("saveEdit")
        self.horizontalLayout_4.addWidget(self.saveEdit)
        self.pushButton = QtWidgets.QPushButton(Setting)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Setting)
        self.buttonBox.accepted.connect(Setting.SaveSetting)
        self.buttonBox.rejected.connect(Setting.close)
        self.pushButton.clicked.connect(Setting.SelectSavePath)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.label_5.setText(_translate("Setting", "保存路径"))
        self.label_2.setText(_translate("Setting", "http代理"))
        self.quality_original.setText(_translate("Setting", "原画"))
        self.quality_high.setText(_translate("Setting", "高"))
        self.quality_medium.setText(_translate("Setting", "中"))
        self.quality_low.setText(_translate("Setting", "低"))
        self.comboBox.setItemText(0, _translate("Setting", "2"))
        self.comboBox.setItemText(1, _translate("Setting", "3"))
        self.comboBox.setItemText(2, _translate("Setting", "4"))
        self.comboBox.setItemText(3, _translate("Setting", "5"))
        self.comboBox.setItemText(4, _translate("Setting", "6"))
        self.label.setText(_translate("Setting", "下载线程数"))
        self.label_4.setText(_translate("Setting", "画质选择"))
        self.httpEdit.setPlaceholderText(_translate("Setting", "http://127.0.0.1:10809"))
        self.pushButton.setText(_translate("Setting", "..."))
