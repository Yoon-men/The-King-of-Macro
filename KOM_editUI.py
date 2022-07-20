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
        self.addDelay_bt.setGeometry(326, 241, 100, 24)
        self.addDelay_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.addDelay_bt_inactive()
        self.addDelay_bt.setText("딜레이 추가")

        self.addColorChecker_bt = QPushButton(self.body_frm)
        self.addColorChecker_bt.setGeometry(326, 282, 100, 24)
        self.addColorChecker_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.addColorChecker_bt_inactive()
        self.addColorChecker_bt.setText("컬러체커 추가")

        self.line_1 = QFrame(self)
        self.line_1.setGeometry(343, 329, 71, 20)
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setStyleSheet("QFrame{\n"
                                        "color : #585858;\n"
                                    "}")

        self.delete_bt = QPushButton(self.body_frm)
        self.delete_bt.setGeometry(326, 367, 100, 24)
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
        self.line_2.setGeometry(343, 414, 71, 20)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setStyleSheet("QFrame{\n"
                                        "color : #585858;\n"
                                    "}")

        self.up_bt = QPushButton(self.body_frm)
        self.up_bt.setGeometry(362, 461, 28, 24)
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
        self.down_bt.setGeometry(362, 496, 28, 24)
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
    ## << addClick_bt (1/4) >> --------------------
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


    ## << addKeyboard_bt (2/4) >> --------------------
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


    ## << addDelay_bt (3/4) >> --------------------
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


    ## << addColorChecker_bt (4/4) >> --------------------
    def addColorChecker_bt_inactive(self) : 
        self.addColorChecker_bt.setStyleSheet("QPushButton{\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "color : #cccccc;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "color : #222222;\n"
                                                "background-color : #aaaaaa;\n"
                                            "}")
    
    def addColorChecker_bt_active(self) : 
        self.addColorChecker_bt.setStyleSheet("QPushButton{\n"
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
        self.addDelay_lb.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
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




class AddColorCheckerUI(QDialog) : 
    def __init__(self) : 
        super().__init__()

        self.addColorCheckerUI()



    def addColorCheckerUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(369, 608)
        self.setWindowTitle("Add ColorChecker")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(10, 5, 351, 601)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")

        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 351, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #464646;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.title_frm)
        self.title_lb.setGeometry(93, 13, 181, 16)
        self.title_lb.setPixmap(":/img/Logo_addColorChecker.png")
        self.title_lb.setScaledContents(True)

        self.exit_bt = QPushButton(self.title_frm)
        self.exit_bt.setGeometry(320, 10, 22, 22)
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


        # setCoordinate_part
        self.setCoordinate_bt = QPushButton(self.body_frm)
        self.setCoordinate_bt.setGeometry(20, 63, 311, 24)
        self.setCoordinate_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.setCoordinate_bt_inactive()
        self.setCoordinate_bt.setText("좌표 설정")

        self.X_lb = QLabel(self.body_frm)
        self.X_lb.setGeometry(75, 122, 14, 21)
        self.X_lb.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.X_lb.setStyleSheet("QLabel{\n"
                                    "color : #b1b1b1;\n"
                                "}")
        self.X_lb.setText("X")

        self.X_le = QLineEdit(self.body_frm)
        self.X_le.setGeometry(95, 120, 67, 24)
        self.X_le.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.X_le.setStyleSheet("QLineEdit{\n"
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
        self.X_le.setValidator(QIntValidator())
        self.X_le.setAlignment(Qt.AlignCenter)

        self.Y_lb = QLabel(self.body_frm)
        self.Y_lb.setGeometry(191, 120, 15, 21)
        self.Y_lb.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.Y_lb.setStyleSheet("QLabel{\n"
                                    "color : #b1b1b1;\n"
                                "}")
        self.Y_lb.setText("Y")

        self.Y_le = QLineEdit(self.body_frm)
        self.Y_le.setGeometry(211, 120, 67, 24)
        self.Y_le.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.Y_le.setStyleSheet("QLineEdit{\n"
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
        self.Y_le.setValidator(QIntValidator())
        self.Y_le.setAlignment(Qt.AlignCenter)
        
        self.line_1 = QLabel(self.body_frm)
        self.line_1.setGeometry(53, 170, 241, 16)
        self.line_1.setPixmap(":/img/Line.png")
        self.line_1.setScaledContents(True)


        # palette_part
        self.palette_rb_1 = QRadioButton(self.body_frm)
        self.palette_rb_1.setGeometry(61, 216, 46, 21)
        self.palette_rb_1.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_1.setChecked(True)

        self.palette_rb_2 = QRadioButton(self.body_frm)
        self.palette_rb_2.setGeometry(120, 216, 46, 21)
        self.palette_rb_2.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_2.hide()

        self.palette_rb_3 = QRadioButton(self.body_frm)
        self.palette_rb_3.setGeometry(179, 216, 46, 21)
        self.palette_rb_3.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_3.hide()

        self.palette_rb_4 = QRadioButton(self.body_frm)
        self.palette_rb_4.setGeometry(238, 216, 46, 21)
        self.palette_rb_4.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_4.hide()

        self.palette_rb_5 = QRadioButton(self.body_frm)
        self.palette_rb_5.setGeometry(61, 250, 46, 21)
        self.palette_rb_5.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_5.hide()

        self.palette_rb_6 = QRadioButton(self.body_frm)
        self.palette_rb_6.setGeometry(120, 250, 46, 21)
        self.palette_rb_6.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_6.hide()

        self.palette_rb_7 = QRadioButton(self.body_frm)
        self.palette_rb_7.setGeometry(179, 250, 46, 21)
        self.palette_rb_7.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_7.hide()

        self.palette_rb_8 = QRadioButton(self.body_frm)
        self.palette_rb_8.setGeometry(238, 250, 46, 21)
        self.palette_rb_8.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_8.hide()

        self.palette_rb_9 = QRadioButton(self.body_frm)
        self.palette_rb_9.setGeometry(61, 284, 46, 21)
        self.palette_rb_9.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_9.hide()

        self.palette_rb_10 = QRadioButton(self.body_frm)
        self.palette_rb_10.setGeometry(120, 284, 46, 21)
        self.palette_rb_10.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_10.hide()

        self.palette_rb_11 = QRadioButton(self.body_frm)
        self.palette_rb_11.setGeometry(179, 284, 46, 21)
        self.palette_rb_11.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_11.hide()

        self.palette_rb_12 = QRadioButton(self.body_frm)
        self.palette_rb_12.setGeometry(238, 284, 46, 21)
        self.palette_rb_12.setStyleSheet("QRadioButton{\n"
                                            "background-color : #ff00ff;\n"
                                            "border-radius : 6px;\n"
                                        "}\n"
                                        "QRadioButton::indicator{\n"
                                            "width : 1px;\n"
                                        "}\n"
                                        "QRadioButton::checked{\n"
                                            "border : 2px solid #ffffff;\n"
                                        "}")
        self.palette_rb_12.hide()

        self.addPalette_bt = QPushButton(self.body_frm)
        self.addPalette_bt.setGeometry(133, 216, 21, 21)
        self.addPalette_bt.setStyleSheet("QPushButton{\n"
                                            "image : url(:/img/bt_plus_normal.png);\n"
                                            "border-radius : 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "image : url(:/img/bt_plus_hover.png);\n"
                                        "}")

        self.R_lb = QLabel(self.body_frm)
        self.R_lb.setGeometry(72, 341, 13, 21)
        self.R_lb.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.R_lb.setStyleSheet("QLabel{\n"
                                    "color : #b1b1b1;\n"
                                "}")
        self.R_lb.setText("R")

        self.R_le = QLineEdit(self.body_frm)
        self.R_le.setGeometry(92, 339, 50, 24)
        self.R_le.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.R_le.setStyleSheet("QLineEdit{\n"
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
        self.R_le.setValidator(QIntValidator(0, 255))
        self.R_le.setAlignment(Qt.AlignCenter)
        self.R_le.setText("255")

        self.G_lb = QLabel(self.body_frm)
        self.G_lb.setGeometry(70, 374, 20, 21)
        self.G_lb.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.G_lb.setStyleSheet("QLabel{\n"
                                    "color : #b1b1b1;\n"
                                "}")
        self.G_lb.setText("G")

        self.G_le = QLineEdit(self.body_frm)
        self.G_le.setGeometry(92, 372, 50, 24)
        self.G_le.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.G_le.setStyleSheet("QLineEdit{\n"
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
        self.G_le.setValidator(QIntValidator(0, 255))
        self.G_le.setAlignment(Qt.AlignCenter)
        self.G_le.setText("0")

        self.B_lb = QLabel(self.body_frm)
        self.B_lb.setGeometry(72, 407, 20, 21)
        self.B_lb.setFont(QFont("나눔고딕", 12, QFont.ExtraBold))
        self.B_lb.setStyleSheet("QLabel{\n"
                                    "color : #b1b1b1;\n"
                                "}")
        self.B_lb.setText("B")

        self.B_le = QLineEdit(self.body_frm)
        self.B_le.setGeometry(92, 405, 50, 24)
        self.B_le.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.B_le.setStyleSheet("QLineEdit{\n"
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
        self.B_le.setValidator(QIntValidator(0, 255))
        self.B_le.setAlignment(Qt.AlignCenter)
        self.B_le.setText("255")

        self.copyColor_bt = QPushButton(self.body_frm)
        self.copyColor_bt.setGeometry(162, 339, 111, 91)
        self.copyColor_bt.setFont(QFont("나눔고딕", 9, QFont.ExtraBold))
        self.copyColor_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "color : #222222;\n"
                                            "background-color : #aaaaaa;\n"
                                        "}")
        self.copyColor_bt.setText("좌표 컬러 복사")

        self.line_2 = QLabel(self.body_frm)
        self.line_2.setGeometry(53, 457, 241, 16)
        self.line_2.setPixmap(":/img/Line.png")
        self.line_2.setScaledContents(True)


        # colorCheckProcess_part
        self.checkingDelay_le = QLineEdit(self.body_frm)
        self.checkingDelay_le.setGeometry(80, 504, 60, 22)
        self.checkingDelay_le.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.checkingDelay_le.setStyleSheet("QLineEdit{\n"
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
        self.checkingDelay_le.setValidator(QIntValidator())
        self.checkingDelay_le.setAlignment(Qt.AlignCenter)
        self.checkingDelay_le.setText("0")

        self.checkingDelay_lb = QLabel(self.body_frm)
        self.checkingDelay_lb.setGeometry(149, 505, 121, 21)
        self.checkingDelay_lb.setFont(QFont("나눔고딕", 10, QFont.ExtraBold))
        self.checkingDelay_lb.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.checkingDelay_lb.setText("초마다 컬러체크 진행")

        self.add_bt = QPushButton(self.body_frm)
        self.add_bt.setGeometry(130, 560, 91, 24)
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
    ## << setCoordinate_bt (1/1) >> --------------------
    def setCoordinate_bt_inactive(self) : 
        self.setCoordinate_bt.setStyleSheet("QPushButton{\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "color : #cccccc;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "color : #222222;\n"
                                                "background-color : #aaaaaa;\n"
                                            "}")
        

    def setCoordinate_bt_active(self) : 
        self.setCoordinate_bt.setStyleSheet("QPushButton{\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "background-color : #aaaaaa;\n"
                                                "color : #222222;\n"
                                            "}")


    def eventFilter(self, object, event) : 
        if event.type() == QtCore.QEvent.HoverEnter : 
            pass                # Test code / please delete the contents of this line.





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    global edit
    edit = EditUI()
    edit.exec_()