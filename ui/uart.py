# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uart.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_uartform(object):
    def setupUi(self, uartform):
        uartform.setObjectName("uartform")
        uartform.resize(387, 303)
        self.txt_show = QtWidgets.QTextEdit(uartform)
        self.txt_show.setGeometry(QtCore.QRect(20, 130, 361, 131))
        self.txt_show.setObjectName("txt_show")
        self.layoutWidget = QtWidgets.QWidget(uartform)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 30, 314, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_comname = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_comname.setObjectName("cb_comname")
        self.horizontalLayout.addWidget(self.cb_comname)
        self.btn_search = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.btn_open = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        self.btn_setcom = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_setcom.setObjectName("btn_setcom")
        self.horizontalLayout.addWidget(self.btn_setcom)
        self.txt_send = QtWidgets.QLineEdit(uartform)
        self.txt_send.setGeometry(QtCore.QRect(20, 70, 361, 20))
        self.txt_send.setObjectName("txt_send")
        self.widget = QtWidgets.QWidget(uartform)
        self.widget.setGeometry(QtCore.QRect(20, 100, 207, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_send = QtWidgets.QCheckBox(self.widget)
        self.cb_send.setObjectName("cb_send")
        self.horizontalLayout_2.addWidget(self.cb_send)
        self.btn_send = QtWidgets.QPushButton(self.widget)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout_2.addWidget(self.btn_send)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.btn_receive = QtWidgets.QPushButton(self.widget)
        self.btn_receive.setObjectName("btn_receive")
        self.horizontalLayout_3.addWidget(self.btn_receive)
        self.widget1 = QtWidgets.QWidget(uartform)
        self.widget1.setGeometry(QtCore.QRect(21, 271, 229, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cb_receive = QtWidgets.QCheckBox(self.widget1)
        self.cb_receive.setObjectName("cb_receive")
        self.horizontalLayout_4.addWidget(self.cb_receive)
        self.btn_clear = QtWidgets.QPushButton(self.widget1)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_4.addWidget(self.btn_clear)
        self.btn_save = QtWidgets.QPushButton(self.widget1)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_4.addWidget(self.btn_save)

        self.retranslateUi(uartform)
        QtCore.QMetaObject.connectSlotsByName(uartform)

    def retranslateUi(self, uartform):
        _translate = QtCore.QCoreApplication.translate
        uartform.setWindowTitle(_translate("uartform", "串口接收发送界面"))
        self.btn_search.setText(_translate("uartform", "搜索"))
        self.btn_open.setText(_translate("uartform", "打开"))
        self.btn_setcom.setText(_translate("uartform", "设置串口"))
        self.cb_send.setText(_translate("uartform", "hex"))
        self.btn_send.setText(_translate("uartform", "发送"))
        self.btn_receive.setText(_translate("uartform", "接收"))
        self.cb_receive.setText(_translate("uartform", "hex显示"))
        self.btn_clear.setText(_translate("uartform", "清除"))
        self.btn_save.setText(_translate("uartform", "保存"))

