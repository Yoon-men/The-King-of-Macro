from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QDialog, QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton, QCheckBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QFontDatabase, QFont
from enum import Enum


class StyleSheets(Enum) : 
    body_frame = ("QFrame{\n"
                        "background-color : #202020;\n"
                        "border-radius : 10px;\n"
                    "}")
    
    title_frame = ("QFrame{\n"
                        "background-color : #484848;\n"
                        "border-radius : 10px;\n"
                    "}")
    
    exit_button = ("QPushButton{\n"
                        "background-color : #aaaaaa;\n"
                        "border-radius : 10px;\n"
                    "}\n"
                    "QPushButton:hover{\n"
                        "background-color : #666666;\n"
                    "}")

    push_button = ("QPushButton{\n"
                        "background-color : #202020;\n"
                        "border : 2px solid #aaaaaa;\n"
                        "border-radius : 6px;\n"
                        "color : #cccccc;\n"
                    "}\n"
                    "QPushButton:hover{\n"
                        "background-color : #aaaaaa;\n"
                        "color : #222222;\n"
                    "}")
    
    label = ("QLabel{\n"
                "color : #b1b1b1;\n"
            "}")
    
    line = ("QLabel{\n"
                "image : url(:/img/line.png);\n"
            "}")
    
    check_box = ("QCheckBox::indicator::unchecked{\n"
                    "image : url(:/img/ckb_unchecked_normal.png);\n"
                    "width : 21;\n"
                    "height : 21px;\n"
                "}\n"
                "QCheckBox::indicator::unchecked::hover{\n"
                    "image : url(:/img/ckb_unchecked_hover.png);\n"
                "}\n"
                
                "QCheckBox::indicator::checked{\n"
                    "image : url(:/img/ckb_checked_normal.png);\n"
                    "width : 21px;\n"
                    "height : 21px;\n"
                "}\n"
                "QCheckBox::indicator::checked::hover{\n"
                    "image : url(:/img/ckb_checked_hover.png);\n"
                "}")


class SettingUI(QDialog) : 
    def __init__(self) : 
        super().__init__()

        self.settingUI()

    def settingUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(370, 310)
        self.setWindowTitle("Setting")
        self.setWindowIcon(QIcon("KOM.ico"))
        QFontDatabase.addApplicationFont("./NanumGothicBold.otf")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(10, 10, 351, 280)
        self.body_frm.setStyleSheet(StyleSheets.body_frame.value)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_frm.setGraphicsEffect(self.shadow)
        
        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 351, 41)
        self.title_frm.setStyleSheet(StyleSheets.title_frame.value)
        
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(137, 13, 81, 21)
        self.title_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/title_setting.png);\n"
                                    "}")
        
        self.exit_bt = QPushButton(self.body_frm)
        self.exit_bt.setGeometry(321, 10, 22, 22)
        self.exit_bt.setStyleSheet(StyleSheets.exit_button.value)
        icon = QIcon()
        icon.addPixmap(":/img/exit.png")
        self.exit_bt.setIcon(icon)
        self.exit_bt.setIconSize(QSize(22, 11))

        self.line = QLabel(self.body_frm)
        self.line.setGeometry(52, 105, 241, 16)
        self.line.setStyleSheet(StyleSheets.line.value)
        

        # load_part
        self.load_bt = QPushButton(self.body_frm)
        self.load_bt.setGeometry(20, 63, 311, 24)
        self.load_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.load_bt.setStyleSheet(StyleSheets.push_button.value)
        self.load_bt.setText("불러오기")


        # setStopKey_part
        self.setStopKey_lb = QLabel(self.body_frm)
        self.setStopKey_lb.setGeometry(70, 145, 111, 21)
        self.setStopKey_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.setStopKey_lb.setStyleSheet(StyleSheets.label.value)
        self.setStopKey_lb.setText("매크로 중단 키 : ")

        self.setStopKey_bt = QPushButton(self.body_frm)
        self.setStopKey_bt.setGeometry(190, 146, 91, 21)
        self.setStopKey_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.setStopKey_bt.setStyleSheet(StyleSheets.push_button.value)
        self.setStopKey_bt.setText("esc")


        # winToTop_part
        self.winToTop_lb = QLabel(self.body_frm)
        self.winToTop_lb.setGeometry(110, 192, 81, 21)
        self.winToTop_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.winToTop_lb.setStyleSheet(StyleSheets.label.value)
        self.winToTop_lb.setText("가장 위로 : ")

        self.winToTop_ckb = QCheckBox(self.body_frm)
        self.winToTop_ckb.setGeometry(200, 192, 21, 21)
        self.winToTop_ckb.setStyleSheet(StyleSheets.check_box.value)
        

        # github_part
        self.github_bt = QPushButton(self.body_frm)
        self.github_bt.setGeometry(163, 234, 30, 30)
        self.github_bt.setStyleSheet("QPushButton{\n"
                                        "border-radius : 10px;\n"
                                        "image : url(:/img/github_bt_normal.png);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "image : url(:/img/github_bt_hover.png);\n"
                                    "}")



    def setCenterPoint(self, event) : 
        self.centerPoint = event.globalPos()

    def moveWindow(self, event) : 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()



    def keyPressEvent(self, event) : 
        if event.key() == Qt.Key_Escape : pass





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    settingUI = SettingUI()
    settingUI.show()
    sys.exit(app.exec_())
