'''
The King of Macro (UI_Setting)

"From now on, all the bothersome tasks will disappear."

ver 2.2.0

~ Tue, Jan 2, 2024 ~

'''

#* ------------------------------------------------------------ *#

## Python Modules
import sys
from enum import Enum
from os import path as os_path


## PySide2 Moduels
from PySide2.QtWidgets import QApplication, QDialog, QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton, QCheckBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QFontDatabase, QFont


## User-defined Modules
from img.img import *

#* ------------------------------------------------------------ *#

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
                    "width : 21px;\n"
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
    def __init__(self) -> None: 
        super().__init__()

        self.settingUI()

        ### ----- init() end ----- ###


    def settingUI(self) -> None: 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(371, 300)
        self.setWindowTitle("Setting")
        icon_path = os_path.join(os_path.dirname(__file__), "KOM.ico")
        if os_path.isfile(icon_path) : 
            self.setWindowIcon(QIcon(icon_path))
        font_path = os_path.join(os_path.dirname(__file__), "NanumGothicBold.otf")
        if os_path.isfile(font_path) : 
            QFontDatabase.addApplicationFont(font_path)


        # body_part
        self.body_FRM = QFrame(self)
        self.body_FRM.setGeometry(10, 10, 351, 280)
        self.body_FRM.setStyleSheet(StyleSheets.body_frame.value)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_FRM.setGraphicsEffect(self.shadow)
        
        self.title_FRM = QFrame(self.body_FRM)
        self.title_FRM.setGeometry(0, 0, 351, 41)
        self.title_FRM.setStyleSheet(StyleSheets.title_frame.value)
        
        self.title_FRM.mousePressEvent = self.setCenterPoint
        self.title_FRM.mouseMoveEvent = self.moveWindow

        self.title_LB = QLabel(self.title_FRM)
        self.title_LB.setGeometry(146, 13, 59, 18)
        self.title_LB.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/title_setting.png);\n"
                                    "}")
        
        self.exit_BT = QPushButton(self.body_FRM)
        self.exit_BT.setGeometry(321, 10, 22, 22)
        self.exit_BT.setStyleSheet(StyleSheets.exit_button.value)
        self.exit_BT.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addPixmap(":/img/exit.png")
        self.exit_BT.setIcon(icon)
        self.exit_BT.setIconSize(QSize(22, 11))

        self.line = QLabel(self.body_FRM)
        self.line.setGeometry(52, 105, 241, 16)
        self.line.setStyleSheet(StyleSheets.line.value)
        

        # load_part
        self.load_BT = QPushButton(self.body_FRM)
        self.load_BT.setGeometry(20, 63, 311, 24)
        self.load_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.load_BT.setStyleSheet(StyleSheets.push_button.value)
        self.load_BT.setFocusPolicy(Qt.NoFocus)
        self.load_BT.setText("불러오기")


        # setStopKey_part
        self.setStopKey_LB = QLabel(self.body_FRM)
        self.setStopKey_LB.setGeometry(70, 145, 111, 21)
        self.setStopKey_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.setStopKey_LB.setStyleSheet(StyleSheets.label.value)
        self.setStopKey_LB.setText("매크로 중단 키 : ")

        self.setStopKey_BT = QPushButton(self.body_FRM)
        self.setStopKey_BT.setGeometry(190, 146, 91, 21)
        self.setStopKey_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.setStopKey_BT.setStyleSheet(StyleSheets.push_button.value)
        self.setStopKey_BT.setFocusPolicy(Qt.NoFocus)
        self.setStopKey_BT.setText("esc")


        # winToTop_part
        self.winToTop_LB = QLabel(self.body_FRM)
        self.winToTop_LB.setGeometry(110, 192, 81, 21)
        self.winToTop_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.winToTop_LB.setStyleSheet(StyleSheets.label.value)
        self.winToTop_LB.setText("가장 위로 : ")

        self.winToTop_CKB = QCheckBox(self.body_FRM)
        self.winToTop_CKB.setGeometry(200, 192, 21, 21)
        self.winToTop_CKB.setStyleSheet(StyleSheets.check_box.value)
        self.winToTop_CKB.setFocusPolicy(Qt.NoFocus)
        

        # github_part
        self.github_BT = QPushButton(self.body_FRM)
        self.github_BT.setGeometry(163, 234, 30, 30)
        self.github_BT.setStyleSheet("QPushButton{\n"
                                        "border-radius : 10px;\n"
                                        "image : url(:/img/github_bt_normal.png);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "image : url(:/img/github_bt_hover.png);\n"
                                    "}")
        self.github_BT.setFocusPolicy(Qt.NoFocus)

        ### ----- settingUI() end ----- ###



    def setCenterPoint(self, event) -> None: 
        self.centerPoint = event.globalPos()

        ### ----- setCenterPoint() end ----- ###


    def moveWindow(self, event) -> None: 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()
        
        ### ----- moveWindow() end ----- ###



    def keyPressEvent(self, event) -> None: 
        if event.key() == Qt.Key_Escape : pass

        ### ----- keyPressEvent() end ----- ###





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    settingUI = SettingUI()
    settingUI.show()
    sys.exit(app.exec_())
