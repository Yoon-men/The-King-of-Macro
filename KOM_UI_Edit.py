'''
The King of Macro (UI_Edit)

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
from PySide2.QtWidgets import QApplication, QDialog, QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton, QComboBox, QListWidget, QLineEdit, QRadioButton, QAbstractItemView
from PySide2.QtCore import Qt, QSize, Signal
from PySide2.QtGui import QIcon, QFontDatabase, QFont, QIntValidator, QDoubleValidator


## User-defined Modules
from img.img import *
from CustomWidget import ItemListWidget

#* ------------------------------------------------------------ *#

class StyleSheets(Enum) : 
    body_frame = ("QFrame{\n"
                        "background-color : #202020;\n"
                        "border-radius : 10px;\n"
                    "}")
    
    title_frame = ("QFrame{\n"
                        "background-color : #464646;\n"
                        "border-radius : 10px;\n"
                    "}")
    
    exit_button = ("QPushButton{\n"
                        "background-color : #aaaaaa;\n"
                        "border-radius : 10px;\n"
                    "}\n"
                    "QPushButton:hover{\n"
                        "background-color : #666666;\n"
                    "}")

    line_edit = ("QLineEdit{\n"
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
    
    push_button = ("QPushButton{\n"
                        "background-color : #202020;\n"
                        "border : 2px solid #aaaaaa;\n"
                        "border-radius : 5px;\n"
                        "color : #cccccc;\n"
                    "}\n"
                    "QPushButton:hover{\n"
                        "background-color : #aaaaaa;\n"
                        "color : #222222;\n"
                    "}")
    
    active_push_button = ("QPushButton{\n"
                                "border : 2px solid #aaaaaa;\n"
                                "border-radius : 5px;\n"
                                "background-color : #aaaaaa;\n"
                                "color : #222222;\n"
                            "}")
    
    label = ("QLabel{\n"
                "color : #b1b1b1;\n"
            "}")
    
    line = ("QLabel{\n"
                "image : url(:/img/line.png);\n"
            "}")
    
    palette = ("QRadioButton::indicator{\n"
                    "width : 46px;\n"
                    "height : 21px;\n"
                    "background-color : #ff00ff;\n"
                    "border-radius : 6px;\n"
                "}\n"
                "QRadioButton::indicator::checked{\n"
                    "border : 2px solid #ffffff;\n"
                "}")
    
    combo_box = ("QComboBox{\n"
                    "font-family : 나눔고딕OTF;\n"
                    "font-weight : bold;\n"
                    "font-size : 10pt;\n"
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
    
    list_widget = ("QListWidget{\n"
                        "background-color : #4d4d4d;\n"
                        "border-radius : 8px;\n"
                        "color : #dddddd;\n"
                        "padding-left : 3px;\n"
                        "padding-top : 3px;\n"
                        "outline: none;\n"
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


class EditUI(QDialog) : 
    remove_item_signal = Signal()

    def __init__(self) -> None: 
        super().__init__()
        
        self.editUI()

        ### ----- init() end ----- ###


    def editUI(self) -> None: 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(461, 611)
        self.setWindowTitle("Edit")
        icon_path = os_path.join(os_path.dirname(__file__), "KOM.ico")
        if os_path.isfile(icon_path) : 
            self.setWindowIcon(QIcon(icon_path))
        font_path = os_path.join(os_path.dirname(__file__), "NanumGothicBold.otf")
        if os_path.isfile(font_path) : 
            QFontDatabase.addApplicationFont(font_path)
        

        # body_part
        self.body_FRM = QFrame(self)
        self.body_FRM.setGeometry(10, 10, 441, 591)
        self.body_FRM.setStyleSheet(StyleSheets.body_frame.value)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_FRM.setGraphicsEffect(self.shadow)
        
        self.title_FRM = QFrame(self.body_FRM)
        self.title_FRM.setGeometry(0, 0, 441, 41)
        self.title_FRM.setStyleSheet(StyleSheets.title_frame.value)
        
        self.title_FRM.mousePressEvent = self.setCenterPoint
        self.title_FRM.mouseMoveEvent = self.moveWindow

        self.title_LB = QLabel(self.title_FRM)
        self.title_LB.setGeometry(201, 13, 38, 16)
        self.title_LB.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/title_edit.png);\n"
                                    "}")
        
        self.exit_BT = QPushButton(self.title_FRM)
        self.exit_BT.setGeometry(410, 10, 22, 22)
        self.exit_BT.setStyleSheet(StyleSheets.exit_button.value)
        self.exit_BT.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addPixmap(":/img/exit.png")
        self.exit_BT.setIcon(icon)
        self.exit_BT.setIconSize(QSize(22, 11))


        # setMacro_part
        self.setMacro_LB = QLabel(self.body_FRM)
        self.setMacro_LB.setGeometry(71, 70, 111, 21)
        self.setMacro_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.setMacro_LB.setStyleSheet(StyleSheets.label.value)
        self.setMacro_LB.setText("편집할 매크로 : ")

        self.setMacro_CB = QComboBox(self.body_FRM)
        self.setMacro_CB.setGeometry(191, 69, 191, 24)
        self.setMacro_CB.setStyleSheet(StyleSheets.combo_box.value)
        
        self.line_1 = QLabel(self.body_FRM)
        self.line_1.setGeometry(101, 114, 241, 16)
        self.line_1.setStyleSheet(StyleSheets.line.value)
        

        # editMacro_part
        self.editMacro_LW = ItemListWidget(self.body_FRM)
        self.editMacro_LW.setGeometry(16, 159, 294, 416)
        self.editMacro_LW.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.editMacro_LW.setStyleSheet(StyleSheets.list_widget.value)
        self.editMacro_LW.setDragDropMode(QAbstractItemView.DragDrop)
        self.editMacro_LW.setDefaultDropAction(Qt.MoveAction)
        self.editMacro_LW.setWordWrap(True)
        
        self.addClick_BT = QPushButton(self.body_FRM)
        self.addClick_BT.setGeometry(326, 159, 100, 24)
        self.addClick_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addClick_BT.setStyleSheet(StyleSheets.push_button.value)
        self.addClick_BT.setFocusPolicy(Qt.NoFocus)
        self.addClick_BT.setText("클릭 추가")

        self.addKeyboard_BT = QPushButton(self.body_FRM)
        self.addKeyboard_BT.setGeometry(326, 200, 100, 24)
        self.addKeyboard_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addKeyboard_BT.setStyleSheet(StyleSheets.push_button.value)
        self.addKeyboard_BT.setFocusPolicy(Qt.NoFocus)
        self.addKeyboard_BT.setText("키보드 추가")

        self.addDelay_BT = QPushButton(self.body_FRM)
        self.addDelay_BT.setGeometry(326, 241, 100, 24)
        self.addDelay_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addDelay_BT.setStyleSheet(StyleSheets.push_button.value)
        self.addDelay_BT.setFocusPolicy(Qt.NoFocus)
        self.addDelay_BT.setText("딜레이 추가")

        self.addColorChecker_BT = QPushButton(self.body_FRM)
        self.addColorChecker_BT.setGeometry(326, 282, 100, 24)
        self.addColorChecker_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addColorChecker_BT.setStyleSheet(StyleSheets.push_button.value)
        self.addColorChecker_BT.setFocusPolicy(Qt.NoFocus)
        self.addColorChecker_BT.setText("컬러체커 추가")
        
        self.line_FRM = QFrame(self)
        self.line_FRM.setGeometry(351, 336, 71, 20)
        self.line_FRM.setFrameShape(QFrame.HLine)
        self.line_FRM.setStyleSheet("QFrame{\n"
                                        "color : #585858;\n"
                                    "}")
        
        self.delete_BT = QPushButton(self.body_FRM)
        self.delete_BT.setGeometry(325, 367, 100, 24)
        self.delete_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.delete_BT.setStyleSheet(StyleSheets.push_button.value)
        self.delete_BT.setFocusPolicy(Qt.NoFocus)
        self.delete_BT.setText("삭제")

        ### ----- editUI() end ----- ###



    def setCenterPoint(self, event) -> None: 
        self.centerPoint = event.globalPos()

        ### ----- setCenterPoint() end ----- ###


    def moveWindow(self, event) -> None: 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()
        
        ### ----- moveWindow() end ----- ###



    def keyPressEvent(self, event) -> None: 
        key = event.key()
        if key == Qt.Key_Escape : 
            pass
        elif key == Qt.Key_Down : 
            current_row = self.editMacro_LW.currentRow()
            if current_row == self.editMacro_LW.count()-1 : 
                self.editMacro_LW.setCurrentRow(0)
            else : 
                self.editMacro_LW.setCurrentRow(current_row+1)
        elif key == Qt.Key_Up : 
            current_row = self.editMacro_LW.currentRow()
            if current_row == 0 : 
                self.editMacro_LW.setCurrentRow(self.editMacro_LW.count()-1)
            else : 
                self.editMacro_LW.setCurrentRow(current_row-1)
        elif key == Qt.Key_Delete : 
            self.remove_item_signal.emit()
        
        ### ----- keyPressEvent() end ----- ###




class AddDelayUI(QDialog) : 
    def __init__(self) -> None: 
        super().__init__()

        self.addDelayUI()

        self.signal()

        ### ----- init() end ----- ###


    def addDelayUI(self) -> None: 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(310, 193)
        self.setWindowTitle("Add Delay")
        icon_path = os_path.join(os_path.dirname(__file__), "KOM.ico")
        if os_path.isfile(icon_path) : 
            self.setWindowIcon(QIcon(icon_path))
        font_path = os_path.join(os_path.dirname(__file__), "NanumGothicBold.otf")
        if os_path.isfile(font_path) : 
            QFontDatabase.addApplicationFont(font_path)
        

        # body_part
        self.body_FRM = QFrame(self)
        self.body_FRM.setGeometry(10, 10, 290, 173)
        self.body_FRM.setStyleSheet(StyleSheets.body_frame.value)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_FRM.setGraphicsEffect(self.shadow)
        
        self.title_FRM = QFrame(self.body_FRM)
        self.title_FRM.setGeometry(0, 0, 290, 41)
        self.title_FRM.setStyleSheet(StyleSheets.title_frame.value)
        self.title_FRM.mousePressEvent = self.setCenterPoint
        self.title_FRM.mouseMoveEvent = self.moveWindow

        self.title_LB = QLabel(self.title_FRM)
        self.title_LB.setGeometry(97, 13, 101, 21)
        self.title_LB.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/title_addDelay);\n"
                                    "}")
        
        self.exit_BT = QPushButton(self.body_FRM)
        self.exit_BT.setGeometry(260, 10, 22, 22)
        self.exit_BT.setStyleSheet(StyleSheets.exit_button.value)
        self.exit_BT.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addPixmap(":/img/exit.png")
        self.exit_BT.setIcon(icon)
        self.exit_BT.setIconSize(QSize(22, 11))


        # addDelay_part
        self.addDelay_LB = QLabel(self.body_FRM)
        self.addDelay_LB.setGeometry(18, 60, 61, 21)
        self.addDelay_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.addDelay_LB.setStyleSheet(StyleSheets.label.value)
        self.addDelay_LB.setText("딜레이 : ")

        self.addDelay_LE = QLineEdit(self.body_FRM)
        self.addDelay_LE.setGeometry(19, 90, 251, 22)
        self.addDelay_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.addDelay_LE.setStyleSheet(StyleSheets.line_edit.value)
        self.addDelay_LE.setValidator(QDoubleValidator())
        self.addDelay_LE.setText("0.0")
        self.addDelay_LE.selectAll()

        self.add_BT = QPushButton(self.body_FRM)
        self.add_BT.setGeometry(58, 133, 81, 24)
        self.add_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.add_BT.setStyleSheet(StyleSheets.push_button.value)
        self.add_BT.setFocusPolicy(Qt.NoFocus)
        self.add_BT.setText("추가")

        self.cancel_BT = QPushButton(self.body_FRM)
        self.cancel_BT.setGeometry(148, 133, 81, 24)
        self.cancel_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.cancel_BT.setStyleSheet(StyleSheets.push_button.value)
        self.cancel_BT.setFocusPolicy(Qt.NoFocus)
        self.cancel_BT.setText("취소")

        ### ----- addDelayUI() end ----- ###



    def setCenterPoint(self, event) -> None: 
        self.centerPoint = event.globalPos()

        ### ----- setCenterPoint() end ----- ###
    

    def moveWindow(self, event) -> None: 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()
        
        ### ----- moveWindow() end ----- ###



    def signal(self) -> None: 
        self.addDelay_LE.textChanged.connect(self.setDelay)

        ### ----- signal() end ----- ###



    def setDelay(self) -> None: 
        if self.addDelay_LE.text() == '' : 
            self.addDelay_LE.setText("0.0")
            self.addDelay_LE.selectAll()

        ### ----- setDelay() end ----- ###




class AddColorCheckerUI(QDialog) : 
    def __init__(self) : 
        super().__init__()

        self.addColorCheckerUI()

        ### ----- init() end ----- ###
    

    def addColorCheckerUI(self) -> None: 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(371, 621)
        self.setWindowTitle("Add ColorChecker")
        icon_path = os_path.join(os_path.dirname(__file__), "KOM.ico")
        if os_path.isfile(icon_path) : 
            self.setWindowIcon(QIcon(icon_path))
        font_path = os_path.join(os_path.dirname(__file__), "NanumGothicBold.otf")
        if os_path.isfile(font_path) : 
            QFontDatabase.addApplicationFont(font_path)


        # body_part
        self.body_FRM = QFrame(self)
        self.body_FRM.setGeometry(10, 10, 351, 601)
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
        self.title_LB.setGeometry(97, 13, 157, 15)
        self.title_LB.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/title_addColorChecker);\n"
                                    "}")
        
        self.exit_BT = QPushButton(self.body_FRM)
        self.exit_BT.setGeometry(320, 10, 22, 22)
        self.exit_BT.setStyleSheet(StyleSheets.exit_button.value)
        self.exit_BT.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addPixmap(":/img/exit.png")
        self.exit_BT.setIcon(icon)
        self.exit_BT.setIconSize(QSize(22, 11))


        # setCoordinate_part
        self.setCoordinate_BT = QPushButton(self.body_FRM)
        self.setCoordinate_BT.setGeometry(20, 63, 311, 24)
        self.setCoordinate_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.setCoordinate_BT.setStyleSheet(StyleSheets.push_button.value)
        self.setCoordinate_BT.setFocusPolicy(Qt.NoFocus)
        self.setCoordinate_BT.setText("좌표 설정")

        self.x_coordinate_LB = QLabel(self.body_FRM)
        self.x_coordinate_LB.setGeometry(75, 122, 14, 21)
        self.x_coordinate_LB.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.x_coordinate_LB.setStyleSheet(StyleSheets.label.value)
        self.x_coordinate_LB.setText("X")
        
        self.x_coordinate_LE = QLineEdit(self.body_FRM)
        self.x_coordinate_LE.setGeometry(95, 120, 67, 24)
        self.x_coordinate_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.x_coordinate_LE.setStyleSheet(StyleSheets.line_edit.value)
        self.x_coordinate_LE.setValidator(QIntValidator())
        self.x_coordinate_LE.setAlignment(Qt.AlignCenter)

        self.y_coordinate_LB = QLabel(self.body_FRM)
        self.y_coordinate_LB.setGeometry(191, 120, 15, 21)
        self.y_coordinate_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.y_coordinate_LB.setStyleSheet(StyleSheets.label.value)
        self.y_coordinate_LB.setText("Y")

        self.y_coordinate_LE = QLineEdit(self.body_FRM)
        self.y_coordinate_LE.setGeometry(211, 120, 67, 24)
        self.y_coordinate_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.y_coordinate_LE.setStyleSheet(StyleSheets.line_edit.value)
        self.y_coordinate_LE.setValidator(QIntValidator())
        self.y_coordinate_LE.setAlignment(Qt.AlignCenter)
        
        self.line_1 = QLabel(self.body_FRM)
        self.line_1.setGeometry(53, 170, 241, 16)
        self.line_1.setStyleSheet(StyleSheets.line.value)


        # palette_part
        self.palette_1_RB = QRadioButton(self.body_FRM)
        self.palette_1_RB.setGeometry(61, 214, 50, 25)
        self.palette_1_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_1_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_1_RB.setChecked(True)

        self.palette_2_RB = QRadioButton(self.body_FRM)
        self.palette_2_RB.setGeometry(120, 214, 50, 25)
        self.palette_2_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_2_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_2_RB.hide()

        self.palette_3_RB = QRadioButton(self.body_FRM)
        self.palette_3_RB.setGeometry(179, 214, 50, 25)
        self.palette_3_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_3_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_3_RB.hide()

        self.palette_4_RB = QRadioButton(self.body_FRM)
        self.palette_4_RB.setGeometry(238, 214, 50, 25)
        self.palette_4_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_4_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_4_RB.hide()

        self.palette_5_RB = QRadioButton(self.body_FRM)
        self.palette_5_RB.setGeometry(61, 248, 50, 25)
        self.palette_5_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_5_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_5_RB.hide()

        self.palette_6_RB = QRadioButton(self.body_FRM)
        self.palette_6_RB.setGeometry(120, 248, 50, 25)
        self.palette_6_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_6_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_6_RB.hide()

        self.palette_7_RB = QRadioButton(self.body_FRM)
        self.palette_7_RB.setGeometry(179, 248, 50, 25)
        self.palette_7_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_7_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_7_RB.hide()

        self.palette_8_RB = QRadioButton(self.body_FRM)
        self.palette_8_RB.setGeometry(238, 248, 50, 25)
        self.palette_8_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_8_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_8_RB.hide()

        self.palette_9_RB = QRadioButton(self.body_FRM)
        self.palette_9_RB.setGeometry(61, 282, 50, 25)
        self.palette_9_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_9_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_9_RB.hide()

        self.palette_10_RB = QRadioButton(self.body_FRM)
        self.palette_10_RB.setGeometry(120, 282, 50, 25)
        self.palette_10_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_10_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_10_RB.hide()

        self.palette_11_RB = QRadioButton(self.body_FRM)
        self.palette_11_RB.setGeometry(179, 282, 50, 25)
        self.palette_11_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_11_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_11_RB.hide()

        self.palette_12_RB = QRadioButton(self.body_FRM)
        self.palette_12_RB.setGeometry(238, 282, 50, 25)
        self.palette_12_RB.setStyleSheet(StyleSheets.palette.value)
        self.palette_12_RB.setFocusPolicy(Qt.NoFocus)
        self.palette_12_RB.hide()

        self.addPalette_BT = QPushButton(self.body_FRM)
        self.addPalette_BT.setGeometry(133, 216, 21, 21)
        self.addPalette_BT.setStyleSheet("QPushButton{\n"
                                            "image : url(:/img/bt_plus_normal.png);\n"
                                            "border-radius : 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "image : url(:/img/bt_plus_hover.png);\n"
                                        "}")
        self.addPalette_BT.setFocusPolicy(Qt.NoFocus)
        
        self.R_LB = QLabel(self.body_FRM)
        self.R_LB.setGeometry(72, 341, 13, 21)
        self.R_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.R_LB.setStyleSheet(StyleSheets.label.value)
        self.R_LB.setText("R")

        self.R_LE = QLineEdit(self.body_FRM)
        self.R_LE.setGeometry(92, 339, 50, 24)
        self.R_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.R_LE.setStyleSheet(StyleSheets.line_edit.value)
        self.R_LE.setValidator(QIntValidator())
        self.R_LE.setAlignment(Qt.AlignCenter)
        self.R_LE.setText("255")

        self.G_LB = QLabel(self.body_FRM)
        self.G_LB.setGeometry(70, 374, 20, 21)
        self.G_LB.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.G_LB.setStyleSheet(StyleSheets.label.value)
        self.G_LB.setText("G")

        self.G_LE = QLineEdit(self.body_FRM)
        self.G_LE.setGeometry(92, 372, 50, 24)
        self.G_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.G_LE.setStyleSheet(StyleSheets.line_edit.value)
        self.G_LE.setValidator(QIntValidator())
        self.G_LE.setAlignment(Qt.AlignCenter)
        self.G_LE.setText("0")

        self.B_LB = QLabel(self.body_FRM)
        self.B_LB.setGeometry(72, 407, 20, 21)
        self.B_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.B_LB.setStyleSheet(StyleSheets.label.value)
        self.B_LB.setText("B")

        self.B_LE = QLineEdit(self.body_FRM)
        self.B_LE.setGeometry(92, 405, 50, 24)
        self.B_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.B_LE.setStyleSheet(StyleSheets.line_edit.value)
        self.B_LE.setValidator(QIntValidator())
        self.B_LE.setAlignment(Qt.AlignCenter)
        self.B_LE.setText("255")

        self.copyColor_BT = QPushButton(self.body_FRM)
        self.copyColor_BT.setGeometry(162, 339, 111, 91)
        self.copyColor_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.copyColor_BT.setStyleSheet(StyleSheets.push_button.value)
        self.copyColor_BT.setFocusPolicy(Qt.NoFocus)
        self.copyColor_BT.setText("좌표 컬러 복사")

        self.line_2 = QLabel(self.body_FRM)
        self.line_2.setGeometry(53, 457, 241, 16)
        self.line_2.setStyleSheet(StyleSheets.line.value)
        

        # colorCheckerProcess_part
        self.checkingDelay_LE = QLineEdit(self.body_FRM)
        self.checkingDelay_LE.setGeometry(80, 504, 60, 22)
        self.checkingDelay_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.checkingDelay_LE.setStyleSheet(StyleSheets.line_edit.value)
        self.checkingDelay_LE.setValidator(QIntValidator())
        self.checkingDelay_LE.setAlignment(Qt.AlignCenter)
        self.checkingDelay_LE.setText("0")

        self.checkingDelay_LB = QLabel(self.body_FRM)
        self.checkingDelay_LB.setGeometry(149, 505, 121, 21)
        self.checkingDelay_LB.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.checkingDelay_LB.setStyleSheet(StyleSheets.label.value)
        self.checkingDelay_LB.setText("초마다 컬러체크 진행")

        self.add_BT = QPushButton(self.body_FRM)
        self.add_BT.setGeometry(130, 560, 91, 24)
        self.add_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.add_BT.setStyleSheet(StyleSheets.push_button.value)
        self.add_BT.setFocusPolicy(Qt.NoFocus)
        self.add_BT.setText("추가")

        ### ----- addColorCheckerUI() end ----- ###



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




class DeletePaletteUI(QDialog) : 
    def __init__(self) -> None: 
        super().__init__()

        self.deletePaletteUI()

        ### ----- init() end ----- ###
    

    def deletePaletteUI(self) -> None: 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(366, 193)
        self.setWindowTitle("Delete Palette")
        icon_path = os_path.join(os_path.dirname(__file__), "KOM.ico")
        if os_path.isfile(icon_path) : 
            self.setWindowIcon(QIcon(icon_path))
        font_path = os_path.join(os_path.dirname(__file__), "NanumGothicBold.otf")
        if os_path.isfile(font_path) : 
            QFontDatabase.addApplicationFont(font_path)


        # body_part
        self.body_FRM = QFrame(self)
        self.body_FRM.setGeometry(10, 10, 346, 173)
        self.body_FRM.setStyleSheet(StyleSheets.body_frame.value)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_FRM.setGraphicsEffect(self.shadow)
        
        self.title_FRM = QFrame(self.body_FRM)
        self.title_FRM.setGeometry(0, 0, 346, 41)
        self.title_FRM.setStyleSheet(StyleSheets.title_frame.value)
        self.title_FRM.mousePressEvent = self.setCenterPoint
        self.title_FRM.mouseMoveEvent = self.moveWindow

        self.title_LB = QLabel(self.title_FRM)
        self.title_LB.setGeometry(116, 13, 115, 15)
        self.title_LB.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/title_deletePalette.png);\n"
                                    "}")
        
        self.exit_BT = QPushButton(self.title_FRM)
        self.exit_BT.setGeometry(316, 10, 22, 22)
        self.exit_BT.setStyleSheet(StyleSheets.exit_button.value)
        self.exit_BT.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addPixmap(":/img/exit.png")
        self.exit_BT.setIcon(icon)
        self.exit_BT.setIconSize(QSize(22, 11))


        # deletePalette_part
        self.deletePalette_LB = QLabel(self.body_FRM)
        self.deletePalette_LB.setGeometry(35, 60, 277, 21)
        self.deletePalette_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.deletePalette_LB.setStyleSheet(StyleSheets.label.value)
        self.deletePalette_LB.setText("아래의 팔레트를 정말 삭제하시겠습니까?")

        self.deletePalette_FRM = QFrame(self.body_FRM)
        self.deletePalette_FRM.setGeometry(151, 92, 50, 25)
        self.deletePalette_FRM.setStyleSheet("QFrame{\n"
                                                "background-color : #ff00ff;\n"
                                                "border-radius : 6px;\n"
                                                "border : 2px solid #ffffff;\n"
                                            "}")

        self.delete_BT = QPushButton(self.body_FRM)
        self.delete_BT.setGeometry(91, 133, 81, 24)
        self.delete_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.delete_BT.setStyleSheet(StyleSheets.push_button.value)
        self.delete_BT.setFocusPolicy(Qt.NoFocus)
        self.delete_BT.setText("삭제")

        self.cancel_BT = QPushButton(self.body_FRM)
        self.cancel_BT.setGeometry(181, 133, 81, 24)
        self.cancel_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.cancel_BT.setStyleSheet(StyleSheets.push_button.value)
        self.cancel_BT.setFocusPolicy(Qt.NoFocus)
        self.cancel_BT.setText("취소")

        ### ----- deletePaletteUI() end ----- ###



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
    editUI = EditUI()
    editUI.show()
    sys.exit(app.exec_())
