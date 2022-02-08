from img.img import *
import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import csv
import keyboard
import mouse
import pyautogui
import time
import copy

class Main(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()



    def mainUI(self) : 
        # basic_group
        self.setFixedSize(414, 695)
        self.setWindowTitle("The_King_of_Macro_v2.0")


        # body_group
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(4, 3, 406, 666)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")

        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 406, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #484848;\n"
                                        "border-radius : 10px;\n"
                                    "}")

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(112, 11, 185, 24)
        self.title_lb.setPixmap(":/img/Logo.png")
        self.title_lb.setScaledContents(True)

        self.exit_bt = QPushButton(self.title_frm)
        self.exit_bt.setGeometry(377, 10, 22, 22)
        self.exit_bt.setStyleSheet("QPushButton{\n"
                                        "background-color : #aaaaaa;\n"
                                        "border-radius : 10px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "background-color : #666666;\n"
                                    "}")
        icon = QIcon()
        icon.addPixmap(":/img/exit.png")
        self.exit_bt.setIcon(icon)
        self.exit_bt.setIconSize(QSize(22, 11))

        self.keep_bt = QPushButton(self.title_frm)
        self.keep_bt.setGeometry(346, 10, 22, 22)
        self.keep_bt.setStyleSheet("QPushButton{\n"
                                        "background-color : #aaaaaa;\n"
                                        "border-radius : 10px;\n"
                                    "}\n" 
                                    "QPushButton:hover{\n"
                                        "background-color : #666666;\n"
                                    "}")
        icon = QIcon()
        icon.addPixmap(":/img/keep.png")
        self.keep_bt.setIcon(icon)
        self.keep_bt.setIconSize(QSize(12, 12))

        self.setting_bt = QPushButton(self.body_frm)
        self.setting_bt.setGeometry(374, 48, 24, 24)
        self.setting_bt.setStyleSheet("QPushButton{\n"
                                        "background-color : #aaaaaa;\n"
                                        "border-radius : 5px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "background-color : #666666;\n"
                                    "}")
        icon = QIcon()
        icon.addPixmap(":/img/setting.png")
        self.setting_bt.setIcon(icon)
        self.setting_bt.setIconSize(QSize(30, 30))

        self.line_1 = QLabel(self.body_frm)
        self.line_1.setGeometry(65, 160, 271, 16)
        self.line_1.setPixmap(":/img/Line.png")
        self.line_1.setScaledContents(True)

        self.line_2 = QLabel(self.body_frm)
        self.line_2.setGeometry(65, 280, 271, 16)
        self.line_2.setPixmap(":/img/Line.png")
        self.line_2.setScaledContents(True)

        self.line_3 = QLabel(self.body_frm)
        self.line_3.setGeometry(62, 407, 271, 16)
        self.line_3.setPixmap(":/img/Line.png")
        self.line_3.setScaledContents(True)

        self.noticeBoard = QListWidget(self.body_frm)
        self.noticeBoard.setGeometry(22, 534, 370, 118)
        self.noticeBoard.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.noticeBoard.setStyleSheet("QListWidget{\n"
                                            "background-color : #4d4d4d;\n"
                                            "border-radius : 8px;\n"
                                            "color : #dddddd;\n"
                                            "padding-left : 3px;\n"
                                        "}\n"
                                        "QListWidget::item{\n"
                                            "margin : 1.5px;\n"
                                        "}\n"
                                        "QListWidget QScrollBar{\n"
                                            "background : #aaaaaa;\n"
                                        "}\n"
                                        "QListWidget::item::selected{\n"
                                            "background : #2b2b2b;\n"
                                            "color : #dddddd;\n"
                                        "}\n"
                                        "QListWidget::item::hover{\n"
                                            "background : #434343;\n"
                                        "}")
        self.noticeBoard.addItem("[system] <The King of Macro_v2.0> - Made by. Yoonmen")
        self.noticeBoard.addItem("[system] 환영합니다. DATA.csv를 불러와주세요.")

        
        #addName_group
        self.addName_lb_title = QLabel(self.body_frm)
        self.addName_lb_title.setGeometry(20, 76, 151, 21)
        self.addName_lb_title.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.addName_lb_title.setStyleSheet("QLabel{\n"
                                                "color : #b1b1b1;\n"
                                            "}")
        self.addName_lb_title.setText("Add Macro's Name")

        self.addName_le = QLineEdit(self.body_frm)
        self.addName_le.setGeometry(20, 107, 300, 24)
        self.addName_le.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.addName_le.setStyleSheet("QLineEdit{\n"
                                            "color : #dddddd;\n"
                                            "background-color : #303030;\n"
                                            "border : 2px solid #303030;\n"
                                            "border-radius : 5px;\n"
                                            "selection-color : #000000;\n"
                                            "selection-background-color : #ffffff;\n"
                                        "}\n"
                                        "QLineEdit::focus{\n"
                                            "border-color : #aaaaaa;\n"
                                        "}")

        self.addName_bt = QPushButton(self.body_frm)
        self.addName_bt.setGeometry(328, 107, 60, 24)
        self.addName_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.addName_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 8px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "color : #222222;\n"
                                            "background-color : #aaaaaa;\n"
                                        "}")
        self.addName_bt.setText("추가")
        

        

if __name__ == '__main__' : 
    app = QApplication(sys.argv)
    global main
    main = Main()
    main.show()
    sys.exit(app.exec_())