'''
The King of Macro (UI_Main)

"From now on, all the bothersome tasks will disappear."

ver 2.2.0

~ Tue, Jan 2, 2024 ~

'''

#* ------------------------------------------------------------ *#

## Python Modules
import sys
from time import strftime as time_strftime
from enum import Enum
from os import path as os_path


## PySide2 Moduels
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton, QLineEdit, QComboBox, QRadioButton, QListWidget
from PySide2.QtCore import Qt, QSize, QEvent
from PySide2.QtGui import QIcon, QFontDatabase, QFont, QIntValidator


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
    
    title_button = ("QPushButton{\n"
                        "background-color : #aaaaaa;\n"
                        "border-radius : 10px;\n"
                    "}\n"
                    "QPushButton:hover{\n"
                        "background-color : #666666;\n"
                    "}")
    
    line = ("QLabel{\n"
                "image : url(:/img/line.png);\n"
            "}")
    
    label = ("QLabel{\n"
                "color : #b1b1b1;\n"
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
                        "border-radius : 6px;\n"
                        "color : #cccccc;\n"
                    "}\n"
                    "QPushButton:hover{\n"
                        "background-color : #aaaaaa;\n"
                        "color : #222222;\n"
                    "}")
    
    active_push_button = ("QPushButton{\n"
                                "border : 2px solid #aaaaaa;\n"
                                "border-radius : 6px;\n"
                                "background-color : #aaaaaa;\n"
                                "color : #222222;\n"
                            "}")
    
    combo_box = ("QComboBox{\n"
                    "background-color : #303030;\n"
                    "border-radius : 5px;\n"
                    "color : #cccccc;\n"
                    "font-family : 나눔고딕OTF;\n"
                    "font-weight : bold;\n"
                    "font-size : 10pt;\n"
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
                    "}\n"
                    "QListWidget QScrollBar{\n"
                        "background-color : #aaaaaa;\n"
                    "}\n"
                    "QListWidget::item{\n"
                        "margin : 1.3px;\n"
                    "}")


class MainUI(QMainWindow) : 
    def __init__(self) -> None: 
        super().__init__()

        self.mainUI()

        self.signal()

        ### ----- init() end ----- ###


    def mainUI(self) -> None: 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(426, 686)
        self.setWindowTitle("The_King_of_Macro")
        icon_path = os_path.join(os_path.dirname(__file__), "KOM.ico")
        if os_path.isfile(icon_path) : 
            self.setWindowIcon(QIcon(icon_path))
        font_path = os_path.join(os_path.dirname(__file__), "NanumGothicBold.otf")
        if os_path.isfile(font_path) : 
            QFontDatabase.addApplicationFont(font_path)


        # body_part
        self.body_FRM = QFrame(self)
        self.body_FRM.setGeometry(10, 10, 406, 666)
        self.body_FRM.setStyleSheet(StyleSheets.body_frame.value)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_FRM.setGraphicsEffect(self.shadow)

        self.title_FRM = QFrame(self.body_FRM)
        self.title_FRM.setGeometry(0, 0, 406, 41)
        self.title_FRM.setStyleSheet(StyleSheets.title_frame.value)
        self.title_FRM.mousePressEvent = self.setCenterPoint
        self.title_FRM.mouseMoveEvent = self.moveWindow

        self.title_LB = QLabel(self.title_FRM)
        self.title_LB.setGeometry(126, 12, 154, 19)
        self.title_LB.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/title_main.png);\n"
                                    "}")

        self.keep_BT = QPushButton(self.title_FRM)
        self.keep_BT.setGeometry(346, 10, 22, 22)
        self.keep_BT.setStyleSheet(StyleSheets.title_button.value)
        self.keep_BT.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addPixmap(":/img/keep.png")
        self.keep_BT.setIcon(icon)
        self.keep_BT.setIconSize(QSize(12, 12))

        self.exit_BT = QPushButton(self.title_FRM)
        self.exit_BT.setGeometry(377, 10, 22, 22)
        self.exit_BT.setStyleSheet(StyleSheets.title_button.value)
        self.exit_BT.setFocusPolicy(Qt.NoFocus)
        icon.addPixmap(":/img/exit.png")
        self.exit_BT.setIcon(icon)
        self.exit_BT.setIconSize(QSize(22, 11))

        self.setting_BT = QPushButton(self.body_FRM)
        self.setting_BT.setGeometry(374, 48, 24, 24)
        self.setting_BT.setStyleSheet("QPushButton{\n"
                                            "background-color : #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "background-color : #666666;\n"
                                        "}")
        self.setting_BT.setFocusPolicy(Qt.NoFocus)
        icon.addPixmap(":/img/setting.png")
        self.setting_BT.setIcon(icon)
        self.setting_BT.setIconSize(QSize(30, 30))

        self.line_1 = QLabel(self.body_FRM)
        self.line_1.setGeometry(67, 160, 271, 16)
        self.line_1.setStyleSheet(StyleSheets.line.value)

        self.line_2 = QLabel(self.body_FRM)
        self.line_2.setGeometry(67, 280, 271, 16)
        self.line_2.setStyleSheet(StyleSheets.line.value)

        self.line_3 = QLabel(self.body_FRM)
        self.line_3.setGeometry(67, 407, 271, 16)
        self.line_3.setStyleSheet(StyleSheets.line.value)


        # addNewMacro_part
        self.addNewMacro_LB = QLabel(self.body_FRM)
        self.addNewMacro_LB.setGeometry(20, 76, 151, 21)
        self.addNewMacro_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.addNewMacro_LB.setStyleSheet(StyleSheets.label.value)
        self.addNewMacro_LB.setText("Add Macro's Name")

        self.addNewMacro_LE = QLineEdit(self.body_FRM)
        self.addNewMacro_LE.setGeometry(20, 107, 300, 24)
        self.addNewMacro_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.addNewMacro_LE.setStyleSheet(StyleSheets.line_edit.value)

        self.addNewMacro_BT = QPushButton(self.body_FRM)
        self.addNewMacro_BT.setGeometry(328, 107, 60, 24)
        self.addNewMacro_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addNewMacro_BT.setStyleSheet(StyleSheets.push_button.value)
        self.addNewMacro_BT.setFocusPolicy(Qt.NoFocus)
        self.addNewMacro_BT.setText("추가")


        # edit_part
        self.edit_LB = QLabel(self.body_FRM)
        self.edit_LB.setGeometry(20, 193, 81, 21)
        self.edit_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.edit_LB.setStyleSheet(StyleSheets.label.value)
        self.edit_LB.setText("Edit Macro")

        self.edit_BT = QPushButton(self.body_FRM)
        self.edit_BT.setGeometry(20, 227, 369, 24)
        self.edit_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.edit_BT.setStyleSheet(StyleSheets.push_button.value)
        self.edit_BT.setFocusPolicy(Qt.NoFocus)
        self.edit_BT.setText("편집")


        # delete_part
        self.delete_LB = QLabel(self.body_FRM)
        self.delete_LB.setGeometry(20, 313, 101, 21)
        self.delete_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.delete_LB.setStyleSheet(StyleSheets.label.value)
        self.delete_LB.setText("Delete Macro")

        self.delete_CB = QComboBox(self.body_FRM)
        self.delete_CB.setGeometry(20, 347, 300, 24)
        self.delete_CB.setStyleSheet(StyleSheets.combo_box.value)
        
        self.delete_BT = QPushButton(self.body_FRM)
        self.delete_BT.setGeometry(328, 347, 60, 24)
        self.delete_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.delete_BT.setStyleSheet(StyleSheets.push_button.value)
        self.delete_BT.setFocusPolicy(Qt.NoFocus)
        self.delete_BT.setText("삭제")


        # start_part
        self.start_LB = QLabel(self.body_FRM)
        self.start_LB.setGeometry(20, 442, 101, 21)
        self.start_LB.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.start_LB.setStyleSheet(StyleSheets.label.value)
        self.start_LB.setText("Start Macro")

        self.start_type_frm = QFrame(self.body_FRM)
        self.start_type_frm.setGeometry(198, 443, 191, 21)
        self.start_type_frm.setStyleSheet("QFrame{\n"
                                                "background-color : #4d4d4d;\n"
                                                "border-radius : 5px;\n"
                                            "}")

        rb_styleSheet = ("QRadioButton{\n"
                            "color : #dddddd;\n"
                        "}")

        self.start_typeNum_RB = QRadioButton(self.start_type_frm)
        self.start_typeNum_RB.setGeometry(6, 0, 91, 21)
        self.start_typeNum_RB.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_typeNum_RB.setStyleSheet(rb_styleSheet)
        self.start_typeNum_RB.setFocusPolicy(Qt.NoFocus)
        self.start_typeNum_RB.setText("Num_type")
        self.start_typeNum_RB.setChecked(True)
        self.start_typeNum_RB.installEventFilter(self)

        self.start_typeTime_RB = QRadioButton(self.start_type_frm)
        self.start_typeTime_RB.setGeometry(102, 0, 91, 21)
        self.start_typeTime_RB.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_typeTime_RB.setStyleSheet(rb_styleSheet)
        self.start_typeTime_RB.setFocusPolicy(Qt.NoFocus)
        self.start_typeTime_RB.setText("Time_type")
        self.start_typeTime_RB.installEventFilter(self)

        self.start_CB = QComboBox(self.body_FRM)
        self.start_CB.setGeometry(20, 476, 163, 24)
        self.start_CB.setStyleSheet(StyleSheets.combo_box.value)

        self.start_1_LB = QLabel(self.body_FRM)
        self.start_1_LB.setGeometry(192, 478, 41, 21)
        self.start_1_LB.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_1_LB.setStyleSheet(StyleSheets.label.value)
        self.start_1_LB.setText("을(를)")

        self.start_LE = QLineEdit(self.body_FRM)
        self.start_LE.setGeometry(235, 478, 60, 22)
        self.start_LE.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_LE.setStyleSheet(StyleSheets.line_edit.value)
        self.start_LE.setValidator(QIntValidator())
        self.start_LE.setAlignment(Qt.AlignCenter)
        self.start_LE.setText("0")

        self.start_2_LB = QLabel(self.body_FRM)
        self.start_2_LB.setGeometry(304, 478, 16, 21)
        self.start_2_LB.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_2_LB.setStyleSheet(StyleSheets.label.value)
        self.start_2_LB.setText("번")

        self.start_BT = QPushButton(self.body_FRM)
        self.start_BT.setGeometry(328, 477, 60, 24)
        self.start_BT.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.start_BT.setStyleSheet(StyleSheets.push_button.value)
        self.start_BT.setFocusPolicy(Qt.NoFocus)
        self.start_BT.setText("실행")

        self.log_LW = QListWidget(self.body_FRM)
        self.log_LW.setGeometry(18, 529, 370, 118)
        self.log_LW.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.log_LW.setStyleSheet(StyleSheets.list_widget.value)
        self.log_LW.setFocusPolicy(Qt.NoFocus)
        self.log_LW.setWordWrap(True)
        self.log_LW.addItem(f"[{time_strftime('%H:%M:%S')}] <The King of Macro v2.2> - Made by. Yoonmen")
        self.log_LW.addItem(f"[{time_strftime('%H:%M:%S')}] 환영합니다. data.dat 파일을 불러와주세요.")
        self.log_LW.setCurrentRow(self.log_LW.count()-1)

        ### ----- mainUI() end ----- ###



    def setCenterPoint(self, event) -> None: 
        self.centerPoint = event.globalPos()

        ### ----- setCenterPoint() end ----- ###


    def moveWindow(self, event) -> None: 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()
        
        ### ----- moveWindow() end ----- ###
    


    def eventFilter(self, object, event) -> bool: 
        if object == self.start_typeNum_RB : 
            if event.type() == QEvent.MouseButtonPress : 
                self.start_CB.setGeometry(20, 476, 163, 24)
                self.start_1_LB.setGeometry(192, 478, 41, 21)
                self.start_LE.setGeometry(235, 478, 60, 22)
                self.start_2_LB.setGeometry(304, 478, 16, 21)
                self.start_2_LB.setText("번")

        elif object == self.start_typeTime_RB : 
            if event.type() == QEvent.MouseButtonPress : 
                self.start_CB.setGeometry(20, 476, 137, 24)
                self.start_1_LB.setGeometry(166, 478, 41, 21)
                self.start_LE.setGeometry(210, 478, 60, 22)
                self.start_2_LB.setGeometry(280, 478, 41, 21)
                self.start_2_LB.setText("초 동안")

        return False
    
        ### ----- eventFilter() end ----- ###



    def signal(self) -> None: 
        self.start_LE.textChanged.connect(self.adjustInputNumber)

        ### ----- signal() end ----- ###



    def adjustInputNumber(self) -> None: 
        if self.start_LE.text() == '' : 
            self.start_LE.setText('0')
            self.start_LE.selectAll()
        elif int(self.start_LE.text()) > 0 : 
            self.start_LE.setText(str(int(self.start_LE.text())))
        
        ### ----- adjustInputNumber() end ----- ###





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    mainUI = MainUI()
    mainUI.show()
    sys.exit(app.exec_())
