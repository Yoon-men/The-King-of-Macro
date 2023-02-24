from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QDialog, QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QFontDatabase, QFont


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
        # self.setWindowIcon(QIcon("KOM.ico"))              # Test code / please unlock the contents of this line.
        QFontDatabase.addApplicationFont("./NanumGothicBold.otf")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(10, 10, 351, 280)
        self.body_frm.setStyleSheet("QFrmae{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_frm.setGraphicsEffect(self.shadow)
        
        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 351, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #484848"
                                        "border-radius : 10px;\n"
                                    "}")
        
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(137, 13, 81, 21)
        self.title_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/logo_setting.png);\n"
                                    "}")
        
        self.exit_bt = QPushButton(self.body_frm)
        self.exit_bt.setGeometry(321, 10, 22, 22)
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

        self.line = QLabel(self.body_frm)
        self.line.setGeometry(52, 105, 241, 16)
        self.line.setStyleSheet("QLabel{\n"
                                    "image : url(:/img/line.png);\n"
                                "}")
        

        # load_part
        bt_styleSheet = ("QPushButton{\n"
                            "background-color : #202020;\n"
                            "border : 2px solid #aaaaaa;\n"
                            "border-radius : 6px;\n"
                            "color : #cccccc;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                            "background-color : #aaaaaa;\n"
                            "color : #222222;\n"
                        "}")

        self.load_bt = QPushButton(self.body_frm)
        self.load_bt.setGeometry(20, 63, 311, 24)
        self.load_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.load_bt.setStyleSheet(bt_styleSheet)
        self.load_bt.setText("불러오기")


        # setStopKey_part


    


    def setCenterPoint(self, event) : 
        self.centerPoint = event.globalPos()

    def moveWindow(self, event) : 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    settingUI = SettingUI()
    settingUI.show()
    sys.exit(app.exec_())
