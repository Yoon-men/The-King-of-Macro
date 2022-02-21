from img.img import *
import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class EditUI(QDialog) : 
    def __init__(self) : 
        super().__init__()

        self.editUI()



    def editUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(448, 598)
        self.setWindowTitle("Edit")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(3, 2, 441, 591)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")

        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 441, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #464646;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(200, 14, 51, 18)
        self.title_lb.setPixmap(":/img/Logo_edit.png")
        self.title_lb.setScaledContents(True)

        self.exit_bt = QPushButton(self.title_frm)
        self.exit_bt.setGeometry(410, 10, 22, 22)
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


        # setMacro_part
        self.setMacro_lb = QLabel(self.body_frm)
        self.setMacro_lb.setGeometry(71, 70, 111, 21)
        self.setMacro_lb.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.setMacro_lb.setStyleSheet("QLabel{\n"
                                        "color : #b1b1b1;\n"
                                    "}")
        self.setMacro_lb.setText("편집할 매크로 : ")

        self.setMacro_cb = QComboBox(self.body_frm)
        self.setMacro_cb.setGeometry(191, 69, 191, 24)
        self.setMacro_cb.setStyleSheet("QComboBox{\n"
                                        "font-family : 나눔고딕;\n"
                                        "font-weight : bold;\n"
                                        "font-size : 10pt;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                        "background-color : #303030;\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 0px;\n"
                                        "background-color : #303030;\n"
                                        "color : #cccccc;\n"
                                        "selection-background-color : #ffffff;\n"
                                        "selection-color : #000000;\n"
                                    "}\n"
                                    "QComboBox::down-arrow{\n"
                                        "image : url(:/img/down.png);\n"
                                        "width : 18px;\n"
                                        "height : 10px;\n"
                                    "}\n"
                                    "QComboBox::drop-down{\n"
                                        "border-color : #b1b1b1;\n"
                                        "padding-right : 10px;\n"
                                    "}")

        self.line_0 = QLabel(self.body_frm)
        self.line_0.setGeometry(101, 114, 241, 16)
        self.line_0.setPixmap(":/img/Line.png")
        self.line_0.setScaledContents(True)


        # editMacro_part
        self.editMacro_lw = QListWidget(self.body_frm)
        self.editMacro_lw.setGeometry(16, 159, 294, 416)
        self.editMacro_lw.setFocusPolicy(Qt.NoFocus)
        self.editMacro_lw.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.editMacro_lw.setStyleSheet("QListWidget{\n"
                                            "background-color : #4d4d4d;\n"
                                            "border-radius : 8px;\n"
                                            "color : #dddddd;\n"
                                            "padding-left : 3px;\n"
                                            "padding-top : 3px;\n"
                                        "}\n"
                                        "QListWidget::item{\n"
                                            "margin : 1.3px;\n"
                                        "}\n"
                                        "QListWidget QScorllBar{\n"
                                            "background : #aaaaaa;\n"
                                        "}\n"
                                        "QListWidget::item::selected{\n"
                                            "background : #2b2b2b;\n"
                                            "color : #dddddd;\n"
                                        "}\n"
                                        "QListWidget::item::hover{\n"
                                            "background : #434343;\n"
                                        "}")

        self.addClick_bt = QPushButton(self.body_frm)
        self.addClick_bt.setGeometry(326, 159, 100, 24)
        self.addClick_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.addClick_bt_inactive()
        self.addClick_bt.setText("클릭 추가")

        self.addKeyboard_bt = QPushButton(self.body_frm)
        self.addKeyboard_bt.setGeometry(326, 200, 100, 24)
        self.addKeyboard_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.addKeyboard_bt_inactive()
        self.addKeyboard_bt.setText("키보드 추가")

        self.addDelay_bt = QPushButton(self.body_frm)
        self.addDelay_bt.setGeometry(326, 244, 100, 24)
        self.addDelay_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.addDelay_bt_inactive()
        self.addDelay_bt.setText("딜레이 추가")

        self.line_1 = QFrame(self)
        self.line_1.setGeometry(343, 291, 71, 20)
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setStyleSheet("QFrame{\n"
                                        "color : #585858;\n"
                                    "}")

        self.delete_bt = QPushButton(self.body_frm)
        self.delete_bt.setGeometry(326, 334, 100, 24)
        self.delete_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.delete_bt.setStyleSheet("QPushButton{\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "color : #cccccc;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "color : #222222;\n"
                                                "background-color : #aaaaaa;\n"
                                            "}")
        self.delete_bt.setText("삭제")

        self.line_2 = QFrame(self)
        self.line_2.setGeometry(343, 388, 71, 20)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setStyleSheet("QFrame{\n"
                                        "color : #585858;\n"
                                    "}")

        self.up_bt = QPushButton(self.body_frm)
        self.up_bt.setGeometry(362, 435, 28, 24)
        self.up_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.up_bt.setStyleSheet("QPushButton{\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "color : #cccccc;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "color : #222222;\n"
                                                "background-color : #aaaaaa;\n"
                                            "}")
        self.up_bt.setText("▲")

        self.down_bt = QPushButton(self.body_frm)
        self.down_bt.setGeometry(362, 470, 28, 24)
        self.down_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.down_bt.setStyleSheet("QPushButton{\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "color : #cccccc;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "color : #222222;\n"
                                                "background-color : #aaaaaa;\n"
                                            "}")
        self.down_bt.setText("▼")


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



    # activatedCondition_group
    ## << addClick_bt (1/3) >> --------------------
    def addClick_bt_inactive(self) : 
        self.addClick_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "color : #222222;\n"
                                            "background-color : #aaaaaa;\n"
                                        "}")

    def addClick_bt_active(self) : 
        self.addClick_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "background-color : #aaaaaa;\n"
                                            "color : #222222;\n"
                                        "}")


    ## << addKeyboard_bt (2/3) >> --------------------
    def addKeyboard_bt_inactive(self) : 
        self.addKeyboard_bt.setStyleSheet("QPushButton{\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "color : #cccccc;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "color : #222222;\n"
                                                "background-color : #aaaaaa;\n"
                                            "}")

    def addKeyboard_bt_active(self) : 
        self.addKeyboard_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "background-color : #aaaaaa;\n"
                                            "color : #222222;\n"
                                        "}")


    ## << addDelay_bt (3/3) >> --------------------
    def addDelay_bt_inactive(self) : 
        self.addDelay_bt.setStyleSheet("QPushButton{\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "color : #cccccc;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "color : #222222;\n"
                                                "background-color : #aaaaaa;\n"
                                            "}")

    def addDelay_bt_active(self) : 
        self.addDelay_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "background-color : #aaaaaa;\n"
                                            "color : #222222;\n"
                                        "}")




class AddDelayUI(QDialog) : 
    def __init__(self) : 
        super().__init__()

        self.addDelayUI()



    def addDelayUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(302, 201)
        self.setWindowTitle("Add Delay")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(10, 10, 290, 173)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")

        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 290, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #464646;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(97, 13, 101, 21)
        self.title_lb.setPixmap(":/img/Logo_addDelay.png")
        self.title_lb.setScaledContents(True)

        self.exit_bt = QPushButton(self.title_frm)
        self.exit_bt.setGeometry(260, 10, 22, 22)
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


        # addDelay_part
        self.addDelay_lb = QLabel(self.body_frm)
        self.addDelay_lb.setGeometry(18, 60, 61, 21)
        self.addDelay_lb.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.addDelay_lb.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.addDelay_lb.setText("딜레이 : ")

        self.addDelay_ds = QDoubleSpinBox(self.body_frm)
        self.addDelay_ds.setGeometry(19, 90, 251, 22)
        self.addDelay_ds.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.addDelay_ds.setStyleSheet("QDoubleSpinBox{\n"
                                            "color : #dddddd;\n"
                                            "background-color : #303030;\n"
                                            "border : 2px solid #303030;\n"
                                            "border-radius : 5px;\n"
                                            "selection-color : #000000;\n"
                                            "selection-background-color : #ffffff;\n"
                                            "}\n"
                                            "QDoubleSpinBox::focus{\n"
                                                "border-color : #aaaaaa;\n"
                                            "}")
        self.addDelay_ds.setMaximum(999999999)

        self.add_bt = QPushButton(self.body_frm)
        self.add_bt.setGeometry(58, 133, 81, 24)
        self.add_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.add_bt.setStyleSheet("QPushButton{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "color : #222222;\n"
                                        "background-color : #aaaaaa;\n"
                                    "}")
        self.add_bt.setText("추가")

        self.cancel_bt = QPushButton(self.body_frm)
        self.cancel_bt.setGeometry(148, 133, 81, 24)
        self.cancel_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.cancel_bt.setStyleSheet("QPushButton{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "color : #222222;\n"
                                        "background-color : #aaaaaa;\n"
                                    "}")
        self.cancel_bt.setText("취소")


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
    global edit
    edit = EditUI()
    edit.exec_()