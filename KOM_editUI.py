from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QDialog, QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton, QComboBox, QListWidget, QDoubleSpinBox, QLineEdit, QRadioButton
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QFontDatabase, QFont, QIntValidator


class EditUI(QDialog) : 
    def __init__(self) : 
        super().__init__()
        
        self. editUI()
    
    def editUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(448, 598)
        self.setWindowTitle("Edit")
        self.setWindowIcon(QIcon("KOM.ico"))
        QFontDatabase.addApplicationFont("./NanumGothicBold.otf")
        

        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(3, 2, 441, 591)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_frm.setGraphicsEffect(self.shadow)
        
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
        self.title_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/logo_edit.png);\n"
                                    "}")
        
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
        self.setMacro_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.setMacro_lb.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.setMacro_lb.setText("편집할 매크로 : ")

        self.setMacro_cb = QComboBox(self.body_frm)
        self.setMacro_cb.setGeometry(191, 69, 191, 24)
        self.setMacro_cb.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.setMacro_cb.setStyleSheet("QComboBox{\n"
                                            "background-color : #303030;\n"
                                            "border-radius : 5px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QComboBox QAbstractItemView{\n"
                                            "background-color : #303030;\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 0px;\n"
                                            "color : #cccccc;\n"
                                            "selection-background-color : #ffffff;\n"
                                            "selection-color : #000000;\n"
                                            "outline : 0px;\n"
                                        "}\n"
                                        "QComboBox::down-arrow{\n"
                                            "image : url(:/img/down.png);\n"
                                            "width : 18px;\n"
                                            "height : 18px;\n"
                                        "}\n"
                                        "QComboBox::drop-down{\n"
                                            "border-color : #b1b1b1;\n"
                                            "padding-right : 10px;\n"
                                        "}")
        
        self.line_1 = QLabel(self.body_frm)
        self.line_1.setGeometry(101, 114, 241, 16)
        self.line_1.setStyleSheet("QLabel{\n"
                                    "image : url(:/img/line.png);\n"
                                "}")
        

        # editMacro_part
        self.editMacro_lw = QListWidget(self.body_frm)
        self.editMacro_lw.setGeometry(16, 159, 294, 416)
        self.editMacro_lw.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.editMacro_lw.setStyleSheet("QListWidget{\n"
                                            "background-color : #4d4d4d;\n"
                                            "border-radius : 8px;\n"
                                            "color : #dddddd;\n"
                                            "padding-left : 3px;\n"
                                            "padding-top : 3px;\n"
                                        "}\n"
                                        "QListWidget QScrollBar{\n"
                                            "background-color : #aaaaaa;\n"
                                        "}\n"
                                        "QListWidget::item{\n"
                                            "margin : 1.3px;\n"
                                        "}\n"
                                        "QListWidget::item::selected{\n"
                                            "background-color : #2b2b2b;\n"
                                            "color : #dddddd;\n"
                                        "}\n"
                                        "QListWidget::item::hover{\n"
                                            "background-color : #434343;\n"
                                        "}")
        self.editMacro_lw.setFocusPolicy(Qt.NoFocus)

        normal_bt_styleSheet = ("QPushButton{\n"
                                    "background-color : #202020;\n"
                                    "border : 2px solid #aaaaaa;\n"
                                    "border-radius : 6px;\n"
                                    "color : #cccccc;\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                    "background-color : #aaaaaa;\n"
                                    "color : #222222;\n"
                                "}")

        working_bt_styleSheet = ("QPushButton{\n"
                                    "background-color : #aaaaaa;\n"
                                    "border : 2px solid #aaaaaa;\n"
                                    "border-radius : 5px;\n"
                                    "color : #222222;\n"
                                "}")
        
        self.addClick_bt = QPushButton(self.body_frm)
        self.addClick_bt.setGeometry(326, 159, 100, 24)
        self.addClick_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addClick_bt.setStyleSheet(normal_bt_styleSheet)
        self.addClick_bt.setText("클릭 추가")

        self.addKeyboard_bt = QPushButton(self.body_frm)
        self.addKeyboard_bt.setGeometry(326, 200, 100, 24)
        self.addKeyboard_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addKeyboard_bt.setStyleSheet(normal_bt_styleSheet)
        self.addKeyboard_bt.setText("키보드 추가")

        self.addDelay_bt = QPushButton(self.body_frm)
        self.addDelay_bt.setGeometry(326, 241, 100, 24)
        self.addDelay_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addDelay_bt.setStyleSheet(normal_bt_styleSheet)
        self.addDelay_bt.setText("딜레이 추가")

        self.addColorChecker_bt = QPushButton(self.body_frm)
        self.addColorChecker_bt.setGeometry(326, 282, 100, 24)
        self.addColorChecker_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addColorChecker_bt.setStyleSheet(normal_bt_styleSheet)
        self.addColorChecker_bt.setText("컬러체커 추가")

        self.frameLine = QFrame(self)
        self.frameLine.setGeometry(343, 329, 71, 20)
        self.frameLine.setFrameShape(QFrame.HLine)
        self.frameLine.setStyleSheet("QFrame{\n"
                                            "color : #585858;\n"
                                        "}")
        
        self.delete_bt = QPushButton(self.body_frm)
        self.delete_bt.setGeometry(326, 367, 100, 24)
        self.delete_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.delete_bt.setStyleSheet(normal_bt_styleSheet)
        self.delete_bt.setText("삭제")



    def setCenterPoint(self, event) : 
        self.centerPoint = event.globalPos()

    def moveWindow(self, event) : 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()



    def keyPressEvent(self, event) : 
        if event.key() == Qt.Key_Escape : pass




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
        self.setWindowIcon(QIcon("KOM.ico"))
        QFontDatabase.addApplicationFont("./NanumGothicBold.otf")
        

        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(10, 10, 290, 173)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_frm.setGraphicsEffect(self.shadow)
        
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
        self.title_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/logo_addDelay);\n"
                                    "}")
        
        self.exit_bt = QPushButton(self.body_frm)
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
        self.addDelay_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.addDelay_lb.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.addDelay_lb.setText("딜레이 : ")

        self.addDelay_ds = QDoubleSpinBox(self.body_frm)
        self.addDelay_ds.setGeometry(19, 90, 251, 22)
        self.addDelay_ds.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.addDelay_ds.setStyleSheet("QDoubleSpinBox{\n"
                                            "background-color : #303030;\n"
                                            "border : 2px solid #303030;\n"
                                            "border-radius : 5px;\n"
                                            "color : #dddddd;\n"
                                            "selection-background-color : #ffffff;\n"
                                            "selection-color : #000000;\n"
                                        "}\n"
                                        "QDoubleSpinBox::focus{\n"
                                            "border : 2px solid #aaaaaa;\n"                 # Test code / please modify the contents of this line.
                                        "}")
        self.addDelay_ds.setMaximum(999999999)

        bt_styleSheet = ("QPushButton{\n"
                            "background-color : #202020;\n"
                            "border : 2px solid #aaaaaa;\n"
                            "border-radius : 5px;\n"
                            "color : #cccccc;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                            "background-color : #aaaaaa;\n"
                            "color : #222222;\n"
                        "}")

        self.add_bt = QPushButton(self.body_frm)
        self.add_bt.setGeometry(58, 133, 81, 24)
        self.add_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.add_bt.setStyleSheet(bt_styleSheet)
        self.add_bt.setText("추가")

        self.cancel_bt = QPushButton(self.body_frm)
        self.cancel_bt.setGeometry(148, 133, 81, 24)
        self.cancel_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.cancel_bt.setStyleSheet(bt_styleSheet)
        self.cancel_bt.setText("취소")



    def setCenterPoint(self, event) : 
        self.centerPoint = event.globalPos()
    
    def moveWindow(self, event) : 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()



    def keyPressEvent(self, event) : 
        if event.key() == Qt.Key_Escape : pass




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
        self.setWindowIcon(QIcon("KOM.ico"))
        QFontDatabase.addApplicationFont("./NanumGothicBold.otf")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(10, 5, 351, 601)
        self.body_frm.setStyleSheet("QFrame{\n"
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
                                        "background-color : #464646;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.body_frm)
        self.title_lb.setGeometry(93, 13, 181, 16)
        self.title_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/logo_addColorChecker);\n"
                                    "}")
        
        self.exit_bt = QPushButton(self.body_frm)
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
        self.setCoordinate_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.setCoordinate_bt.setStyleSheet("QPushButton{\n"
                                                "background-color : #202020;\n"
                                                "border : 2px solid #aaaaaa;\n"
                                                "border-radius : 5px;\n"
                                                "color : #cccccc;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "background-color : #aaaaaa;\n"
                                                "color : #222222;\n"
                                            "}")
        self.setCoordinate_bt.setText("좌표 설정")

        lb_styleSheet = ("QLabel{\n"
                            "color : #b1b1b1;\n"
                        "}")

        self.x_coordinate_lb = QLabel(self.body_frm)
        self.x_coordinate_lb.setGeometry(75, 122, 14, 21)
        self.x_coordinate_lb.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.x_coordinate_lb.setStyleSheet(lb_styleSheet)
        self.x_coordinate_lb.setText("X")

        le_styleSheet = ("QLineEdit{\n"
                            "background-color : #303030;\n"
                            "border : 2px solid #303030;\n"
                            "border-radius : 5px;\n"
                            "color : #dddddd;\n"
                            "selection-background-color : #ffffff;\n"
                            "selection-color : #000000;\n"
                        "}\n"
                        "QLineEdit::focus{\n"
                            "border-color : #aaaaaa;\n"
                        "}")
        
        self.x_coordinate_le = QLineEdit(self.body_frm)
        self.x_coordinate_le.setGeometry(95, 120, 67, 24)
        self.x_coordinate_le.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.x_coordinate_le.setStyleSheet(le_styleSheet)
        self.x_coordinate_le.setValidator(QIntValidator())
        self.x_coordinate_le.setAlignment(Qt.AlignCenter)

        self.y_coordinate_lb = QLabel(self.body_frm)
        self.y_coordinate_lb.setGeometry(191, 120, 15, 21)
        self.y_coordinate_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.y_coordinate_lb.setStyleSheet(lb_styleSheet)
        self.y_coordinate_lb.setText("Y")

        self.y_coordinate_le = QLineEdit(self.body_frm)
        self.y_coordinate_le.setGeometry(211, 120, 67, 24)
        self.y_coordinate_le.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.y_coordinate_le.setStyleSheet(le_styleSheet)
        self.y_coordinate_le.setValidator(QIntValidator())
        self.y_coordinate_le.setAlignment(Qt.AlignCenter)

        line_styleSheet = ("QLabel{\n"
                                "image : url(:/img/line.png);\n"
                            "}")
        
        self.line_1 = QLabel(self.body_frm)
        self.line_1.setGeometry(53, 170, 241, 16)
        self.line_1.setStyleSheet(line_styleSheet)


        # palette_part
        palette_styleSheet = ("QRadioButton::indicator{\n"
                                    "width : 46px;\n"
                                    "height : 21px;\n"
                                    "background-color : #ff00ff;\n"
                                    "border-radius : 6px;\n"
                                "}\n"
                                "QRadioButton::indicator::checked{\n"
                                    "border : 2px solid #ffffff;\n"
                                "}")
        
        self.palette_rb_1 = QRadioButton(self.body_frm)
        self.palette_rb_1.setGeometry(61, 214, 50, 25)
        self.palette_rb_1.setStyleSheet(palette_styleSheet)
        self.palette_rb_1.setChecked(True)

        self.palette_rb_2 = QRadioButton(self.body_frm)
        self.palette_rb_2.setGeometry(120, 214, 50, 25)
        self.palette_rb_2.setStyleSheet(palette_styleSheet)
        self.palette_rb_2.hide()

        self.palette_rb_3 = QRadioButton(self.body_frm)
        self.palette_rb_3.setGeometry(179, 214, 50, 25)
        self.palette_rb_3.setStyleSheet(palette_styleSheet)
        self.palette_rb_3.hide()

        self.palette_rb_4 = QRadioButton(self.body_frm)
        self.palette_rb_4.setGeometry(238, 214, 50, 25)
        self.palette_rb_4.setStyleSheet(palette_styleSheet)
        self.palette_rb_4.hide()

        self.palette_rb_5 = QRadioButton(self.body_frm)
        self.palette_rb_5.setGeometry(61, 248, 50, 25)
        self.palette_rb_5.setStyleSheet(palette_styleSheet)
        self.palette_rb_5.hide()

        self.palette_rb_6 = QRadioButton(self.body_frm)
        self.palette_rb_6.setGeometry(120, 248, 50, 25)
        self.palette_rb_6.setStyleSheet(palette_styleSheet)
        self.palette_rb_6.hide()

        self.palette_rb_7 = QRadioButton(self.body_frm)
        self.palette_rb_7.setGeometry(179, 248, 50, 25)
        self.palette_rb_7.setStyleSheet(palette_styleSheet)
        self.palette_rb_7.hide()

        self.palette_rb_8 = QRadioButton(self.body_frm)
        self.palette_rb_8.setGeometry(238, 248, 50, 25)
        self.palette_rb_8.setStyleSheet(palette_styleSheet)
        self.palette_rb_8.hide()

        self.palette_rb_9 = QRadioButton(self.body_frm)
        self.palette_rb_9.setGeometry(61, 282, 50, 25)
        self.palette_rb_9.setStyleSheet(palette_styleSheet)
        self.palette_rb_9.hide()

        self.palette_rb_10 = QRadioButton(self.body_frm)
        self.palette_rb_10.setGeometry(120, 282, 50, 25)
        self.palette_rb_10.setStyleSheet(palette_styleSheet)
        self.palette_rb_10.hide()

        self.palette_rb_11 = QRadioButton(self.body_frm)
        self.palette_rb_11.setGeometry(179, 282, 50, 25)
        self.palette_rb_11.setStyleSheet(palette_styleSheet)
        self.palette_rb_11.hide()

        self.palette_rb_12 = QRadioButton(self.body_frm)
        self.palette_rb_12.setGeometry(238, 282, 50, 25)
        self.palette_rb_12.setStyleSheet(palette_styleSheet)
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
        self.R_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.R_lb.setStyleSheet(lb_styleSheet)
        self.R_lb.setText("R")

        self.R_le = QLineEdit(self.body_frm)
        self.R_le.setGeometry(92, 339, 50, 24)
        self.R_le.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.R_le.setStyleSheet(le_styleSheet)
        self.R_le.setValidator(QIntValidator())
        self.R_le.setAlignment(Qt.AlignCenter)
        self.R_le.setText("255")

        self.G_lb = QLabel(self.body_frm)
        self.G_lb.setGeometry(70, 374, 20, 21)
        self.G_lb.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.G_lb.setStyleSheet(lb_styleSheet)
        self.G_lb.setText("G")

        self.G_le = QLineEdit(self.body_frm)
        self.G_le.setGeometry(92, 372, 50, 24)
        self.G_le.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.G_le.setStyleSheet(le_styleSheet)
        self.G_le.setValidator(QIntValidator())
        self.R_le.setAlignment(Qt.AlignCenter)
        self.R_le.setText("0")

        self.B_lb = QLabel(self.body_frm)
        self.B_lb.setGeometry(72, 407, 20, 21)
        self.B_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.B_lb.setStyleSheet(lb_styleSheet)
        self.B_lb.setText("B")

        self.B_le = QLineEdit(self.body_frm)
        self.B_le.setGeometry(92, 405, 50, 24)
        self.B_le.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.B_le.setStyleSheet(le_styleSheet)
        self.B_le.setValidator(QIntValidator())
        self.B_le.setAlignment(Qt.AlignCenter)
        self.B_le.setText("255")

        bt_styleSheet = ("QPushButton{\n"
                            "background-color : #202020;\n"
                            "border : 2px solid #aaaaaa;\n"
                            "border-radius : 5px;\n"
                            "color : #cccccc;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                            "background-color : #aaaaaa;\n"
                            "color : #222222;\n"
                        "}")

        self.copyColor_bt = QPushButton(self.body_frm)
        self.copyColor_bt.setGeometry(162, 339, 111, 91)
        self.copyColor_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.copyColor_bt.setStyleSheet(bt_styleSheet)
        self.copyColor_bt.setText("좌표 컬러 복사")

        self.line_2 = QLabel(self.body_frm)
        self.line_2.setGeometry(53, 457, 241, 16)
        self.line_2.setStyleSheet(line_styleSheet)
        

        # colorCheckerProcess_part
        self.checkingDelay_le = QLineEdit(self.body_frm)
        self.checkingDelay_le.setGeometry(80, 504, 60, 22)
        self.checkingDelay_le.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.checkingDelay_le.setStyleSheet(le_styleSheet)
        self.checkingDelay_le.setValidator(QIntValidator())
        self.checkingDelay_le.setAlignment(Qt.AlignCenter)
        self.checkingDelay_le.setText("0")

        self.checkingDelay_lb = QLabel(self.body_frm)
        self.checkingDelay_lb.setGeometry(149, 505, 121, 21)
        self.checkingDelay_lb.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.checkingDelay_lb.setStyleSheet(lb_styleSheet)
        self.checkingDelay_lb.setText("초마다 컬러체크 진행")

        self.add_bt = QPushButton(self.body_frm)
        self.add_bt.setGeometry(130, 560, 91, 24)
        self.add_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.add_bt.setStyleSheet(bt_styleSheet)
        self.add_bt.setText("추가")



    def setCenterPoint(self, event) : 
        self.centerPoint = event.globalPos()
    
    def moveWindow(self, event) : 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()



    def keyPressEvent(self, event) : 
        if event.key() == Qt.Key_Escape : pass




class DeletePaletteUI(QDialog) : 
    def __init__(self) : 
        super().__init__()

        self.deletePaletteUI()
    
    def deletePaltteUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(361, 208)
        self.setWindowTitle("Delete Palette")
        self.setWindowIcon(QIcon("KOM.ico"))
        QFontDatabase.addApplicationFont("./NanumGothicBold.otf")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(10, 10, 346, 173)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_frm.setGraphicsEffect(self.shadow)
        
        self.title_frm = QFrame(self.body_frm)
        self.title_frm.setGeometry(0, 0, 346, 41)
        self.title_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #464646;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow

        self.title_lb = QLabel(self.body_frm)
        self.title_lb.setGeometry(108, 12, 140, 19)
        self.title_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/logo_deletePalette.png);\n"
                                    "}")
        
        self.exit_bt = QPushButton(self.title_frm)
        self.exit_bt.setGeometry(316, 10, 22, 22)
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


        # deletePalette_part
        lb_styleSheet = ("QLabel{\n"
                            "color : #b1b1b1;\n"
                        "}")

        self.deletePalette_lb = QLabel(self.body_frm)
        self.deletePalette_lb.setGeometry(35, 60, 277, 21)
        self.deletePalette_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.deletePalette_lb.setStyleSheet(lb_styleSheet)
        self.deletePalette_lb.setText("아래의 팔레트를 정말 삭제하시겠습니까?")

        bt_styleSheet = ("QPushButton{\n"
                            "background-color : #202020;\n"
                            "border : 2px solid #aaaaaa;\n"
                            "border-radius : 5px;\n"
                            "color : #cccccc;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                            "background-color : #aaaaaa;\n"
                            "color : #222222;\n"
                        "}")

        self.delete_bt = QPushButton(self.body_frm)
        self.delete_bt.setGeometry(91, 133, 81, 24)
        self.delete_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.delete_bt.setStyleSheet(bt_styleSheet)
        self.delete_bt.setText("삭제")

        self.cancel_bt = QPushButton(self.body_frm)
        self.cancel_bt.setGeometry(181, 133, 81, 24)
        self.cancel_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.cancel_bt.setStyleSheet(bt_styleSheet)
        self.cancel_bt.setText("취소")


    
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
    editUI = EditUI()
    editUI.show()
    sys.exit(app.exec_())
