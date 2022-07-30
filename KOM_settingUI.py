from img.img import *
import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

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


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(10, 10, 351, 280)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")

        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 351, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #464646;"
                                        "border-radius : 10px;\n"
                                    "}")
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(137, 13, 81, 21)
        self.title_lb.setPixmap(":/img/Logo_setting.png")
        self.title_lb.setScaledContents(True)

        self.exit_bt = QPushButton(self.title_frm)
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
        self.line.setPixmap(":/img/Line.png")
        self.line.setScaledContents(True)


        # load_part
        self.load_bt = QPushButton(self.body_frm)
        self.load_bt.setGeometry(20, 63, 311, 24)
        self.load_bt.setFont(QFont("나눔고딕OTF", 9, QFont.ExtraBold))
        self.load_bt.setStyleSheet("QPushButton{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "color : #222222;\n"
                                        "background-color : #aaaaaa;\n"
                                    "}")
        self.load_bt.setText("불러오기")

        
        # stopKey_part
        self.stopKey_lb = QLabel(self.body_frm)
        self.stopKey_lb.setGeometry(70, 145, 111, 21)
        self.stopKey_lb.setFont(QFont("나눔고딕OTF", 12, QFont.ExtraBold))
        self.stopKey_lb.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.stopKey_lb.setText("매크로 중단 키 : ")

        self.stopKey_bt = QPushButton(self.body_frm)
        self.stopKey_bt.setGeometry(190, 146, 91, 21)
        self.stopKey_bt.setFont(QFont("나눔고딕OTF", 9, QFont.ExtraBold))
        self.stopKey_bt.setStyleSheet("QPushButton{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "color : #222222;\n"
                                        "background-color : #aaaaaa;\n"
                                    "}")
        self.stopKey_bt.setText("esc")


        # winToTop_part
        self.winToTop_lb = QLabel(self.body_frm)
        self.winToTop_lb.setGeometry(110, 192, 81, 21)
        self.winToTop_lb.setFont(QFont("나눔고딕OTF", 12, QFont.ExtraBold))
        self.winToTop_lb.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.winToTop_lb.setText("가장 위로 : ")

        self.winToTop_ckb = QCheckBox(self.body_frm)
        self.winToTop_ckb.setGeometry(200, 192, 21, 21)
        self.winToTop_ckb.setStyleSheet("QCheckBox::indicator::unchecked{\n"
                                            "image : url(:/img/ckb_unchecked_normal.png);\n"
                                            "width : 20px;\n"
                                            "height : 20px;\n"
                                        "}\n"
                                        
                                        "QCheckBox::indicator::unchecked::hover{\n"
                                            "image : url(:/img/ckb_unchecked_hover.png);\n"
                                        "}\n"
                                        
                                        "QCheckBox::indicator::checked{\n"
                                            "image : url(:/img/ckb_checked_normal.png);\n"
                                            "width : 20px;\n"
                                            "height : 20px;\n"
                                        "}\n"
                                        
                                        "QCheckBox::indicator::checked::hover{\n"
                                            "image : url(:/img/ckb_checked_hover.png);\n"
                                        "}")


        # icon_part
        self.github_bt = QPushButton(self.body_frm)
        self.github_bt.setGeometry(163, 234, 30, 30)
        self.github_bt.setStyleSheet("QPushButton{\n"
                                        "border-radius : 10px;\n"
                                        "image : url(:/img/github_0.png);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "image : url(:/img/github_1.png);\n"
                                    "}")


        # dropShadow_group
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_frm.setGraphicsEffect(self.shadow)



    # move_group
    def setCenterPoint(self, event) : 
        self.centerPoint = event.globalPos()


    def moveWindow(self, event) : 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()



    # ignoreESC_group
    def keyPressEvent(self, event) : 
        if event.key() == Qt.Key_Escape : 
            pass





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    global settingUI
    settingUI = SettingUI()
    settingUI.exec_()