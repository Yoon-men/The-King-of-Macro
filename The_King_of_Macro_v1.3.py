"""
<The_King_of_Macro_v1.3> - 21.12.23.목 ??:??
* Made by Yoonmen *

[update] 구조 단순화
"""

import sys
from urllib.request import DataHandler
from PyQt5 import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
import os
import csv

import keyboard
import mouse
import pyautogui
import time

class MyApp(object) : 


    def __init__(self) : 
        super().__init__()

        self.initUI()


    def initUI(self, Form) : 
        # Default Setting
        Form.setFixedSize(351, 664)
        Form.setWindowTitle("The_King_of_Macro_v1.3")

        _translate = QCoreApplication.translate

        self.title = QLabel()
        self.title.setGeometry(60, 10, 241, 71)
        self.title.setText(_translate("The King of Macro"))

        self.version = QLabel()
        self.version.setGeometry(10, 10, 64, 15)
        self.version.setText(_translate("v1.3"))

        self.loadButton = QToolButton()
        self.loadButton.setGeometry(280, 10, 61, 20)
        self.loadButton.setText(_translate("불러오기"))

        self.noticeBoard = QListWidget()
        self.noticeBoard.setGeometry(20, 550, 311, 81)

        self.dev = QLabel()
        self.dev.setGeometry(130, 640, 101, 16)
        self.dev.setText(_translate("by. Yoonmen"))


        # addName_group
        self.addName_group = QGroupBox("<Add Macro's Name>")

        self.addName_le = QLineEdit()
        self.addName_le.setGeometry(20, 100, 251, 20)
        self.addName_le.setPlaceholderText("ex) 자동사냥")

        self.addName_bt = QPushButton()
        self.addName_bt.setGeometry(280, 100, 51, 21)
        self.addName_bt.setText(_translate("추가"))


        # addClick_group
        self.addClick_group = QGroupBox("<Add Click>")

        self.addClick_cb = QComboBox()
        self.addClick_cb.setGeometry(20, 170, 101, 22)

        self.addClick_lb_1 = QLabel()
        self.addClick_lb_1.setGeometry(130, 170, 16, 20)
        self.addClick_lb_1.setText(_translate("에"))

        self.addClick_lb_2 = QLabel()
        self.addClick_lb_2.setGeometry(210, 170, 71, 20)
        self.addClick_lb_2.setText(_translate("초 간격으로"))
        
        self.addClick_ds = QDoubleSpinBox()
        self.addClick_ds.setGeometry(150, 170, 51, 22)

        self.addClick_bt = QPushButton()
        self.addClick_bt.setGeometry(280, 100, 51, 21)
        self.addClick_bt.setText(_translate("클릭"))

        self.addClick_lb_3 = QLabel()
        self.addClick_lb_3.setGeometry(80, 200, 191, 20)
        self.addClick_lb_3.setText(_translate("(순서에 맞게 클릭을 진행하세요.)"))


        # addKeyboard_group
        self.addKeyboard_group = QGroupBox("<Add Keyboard>")

        self.addKeyboard_cb = QComboBox()
        self.addKeyboard_cb.setGeometry(20, 270, 101, 22)

        self.addKeyboard_lb_1 = QLabel()
        self.addKeyboard_lb_1.setGeometry(130, 270, 16, 20)
        self.addKeyboard_lb_1.setText(_translate("에"))

        self.addKeyboard_ds = QDoubleSpinBox()
        self.addKeyboard_ds.setGeometry(150, 270, 51, 22)

        self.addKeyboard_lb_2 = QLabel()
        self.addKeyboard_lb_2.setGeometry(210, 270, 71, 20)
        self.addKeyboard_lb_2.setText(_translate("초 간격으로"))

        self.addKeyboard_bt = QPushButton()
        self.addKeyboard_bt.setGeometry(280, 170, 16, 20)
        self.addKeyboard_bt.setText(_translate("입력"))

        self.addKeyboard_lb_3 = QLabel()
        self.addKeyboard_lb_3.setGeometry(80, 300, 191, 20)
        self.addKeyboard_lb_3.setText("(순서에 맞게 입력을 진행하세요.)")


        # deleteMacro_group
        self.deleteMacro_group = QGroupBox("<Delete Macro>")

        self.deleteMacro_cb = QComboBox()
        self.deleteMacro_cb.setGeometry(20, 400, 211, 22)
        
        self.deleteMacro_lb_1 = QLabel()
        self.deleteMacro_lb_1.setGeometry*(240, 400, 41, 20)
        self.deleteMacro_lb_1.setText(_translate("을(를)"))

        self.deleteMacro_bt = QPushButton()
        self.deleteMacro_bt.setGeometry(280, 400, 51, 21)
        self.deleteMacro_bt.setText(_translate("삭제"))


        # startMacro_group
        self.startMacro_group = QGroupBox("<Start Macro>")

        self.startMacro_cb = QComboBox()
        self.startMacro_cb.setGeometry(20, 510, 141, 22)
        
        self.startMacro_lb_1 = QLabel()
        self.startMacro_lb_1.setGeometry(170, 510, 41, 20)
        self.startMacro_lb_1.setText(_translate("을(를)"))

        self.startMacro_sb = QSpinBox()
        self.startMacro_sb.setGeometry(210, 510, 42, 22)

        self.startMacro_lb_2 = QLabel()
        self.startMacro_lb_2.setGeometry(260, 510, 16, 20)
        self.startMacro_lb_2.setText(_translate("번"))

        self.startMacro_bt = QPushButton()
        self.startMacro_bt.setGeometry(280, 510, 51, 21)
        self.startMacro_bt.setText(_translate("실행"))


        










if __name__ == '__main__' : 
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

