"""
<The_King_of_Macro_v1.3> - 21.12.23.목 ??:??
* Made by Yoonmen *

[update] 구조 단순화
"""

import sys
from urllib.request import DataHandler
from PyQt5 import *
from PyQt5.QtWidgets import *
import os
import csv

import keyboard
import mouse
import pyautogui
import time

class MyApp() : 


    def __init__(self) : 
        super().__init__()

        self.initUI()


    def initUI(self, Form) : 
        # Default Setting
        Form.setFixedSize(351, 664)
        Form.setWindowTitle("The_King_of_Macro_v1.3")

        # addName_group
        self.addName_group = QGroupBox("<Add Macro's Name>")

        self.addName_le = QLineEdit()
        self.addName_le.setGeometry(20, 100, 251, 20)
        self.addName_le.setPlaceholderText("ex) 자동사냥")


        # addClick_group
        self.addClick_group = QGroupBox("<Add Click>")

        self.addClick_cb = QComboBox()
        self.addClick_cb.setGeometry(20, 170, 101, 22)
        
        self.addClick_ds = QDoubleSpinBox()
        self.addClick_ds.setGeometry(150, 170, 51, 22)

        self.addClick_bt = QPushButton()
        self.addClick_bt.setGeometry(280, 100, 51, 21)




