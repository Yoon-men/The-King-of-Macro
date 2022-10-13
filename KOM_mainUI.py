from img.img import *
import sys
from PySide2.QtGui import QIcon, QFont, QIntValidator
from PySide2.QtWidgets import QMainWindow, QFrame, QLabel, QPushButton, QListWidget, QLineEdit, QComboBox, QRadioButton, QGraphicsDropShadowEffect, QApplication
from PySide2.QtCore import Qt, QSize

global startType
startType = "typeNum"

class MainUI(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()



    def mainUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(414, 695)
        self.setWindowTitle("The_King_of_Macro_v2.1")


        # body_part
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
        self.title_frm.mousePressEvent = self.setCenterPoint
        self.title_frm.mouseMoveEvent = self.moveWindow
        

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
        self.noticeBoard.setGeometry(18, 529, 370, 118)
        self.noticeBoard.setFocusPolicy(Qt.NoFocus)
        self.noticeBoard.setFont(QFont("나눔고딕OTF", 9, QFont.ExtraBold))
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
        self.noticeBoard.addItem("[system] <The King of Macro_v2.1> - Made by. Yoonmen")
        self.noticeBoard.addItem("[system] 환영합니다. DATA.p 파일을 불러와주세요.")


        #addName_part
        self.addName_lb_title = QLabel(self.body_frm)
        self.addName_lb_title.setGeometry(20, 76, 151, 21)
        self.addName_lb_title.setFont(QFont("나눔고딕OTF", 12, QFont.ExtraBold))
        self.addName_lb_title.setStyleSheet("QLabel{\n"
                                                "color : #b1b1b1;\n"
                                            "}")
        self.addName_lb_title.setText("Add Macro's Name")

        self.addName_le = QLineEdit(self.body_frm)
        self.addName_le.setGeometry(20, 107, 300, 24)
        self.addName_le.setFont(QFont("나눔고딕OTF", 10, QFont.ExtraBold))
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
        self.addName_bt.setFont(QFont("나눔고딕OTF", 9, QFont.ExtraBold))
        self.addName_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 8px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "background-color : #aaaaaa;\n"
                                            "color : #222222;\n"
                                        "}")
        self.addName_bt.setText("추가")


        # edit_part
        self.edit_lb_title = QLabel(self.body_frm)
        self.edit_lb_title.setGeometry(20, 193, 81, 21)
        self.edit_lb_title.setFont(QFont("나눔고딕OTF", 12, QFont.ExtraBold))
        self.edit_lb_title.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                            "}")
        self.edit_lb_title.setText("Edit Macro")

        self.edit_bt = QPushButton(self.body_frm)
        self.edit_bt.setGeometry(20, 227, 369, 24)
        self.edit_bt.setFont(QFont("나눔고딕OTF", 9, QFont.ExtraBold))
        self.edit_bt_inactive()
        self.edit_bt.setText("편집")


        # delete_part
        self.delete_lb_title = QLabel(self.body_frm)
        self.delete_lb_title.setGeometry(20, 313, 101, 21)
        self.delete_lb_title.setFont(QFont("나눔고딕OTF", 12, QFont.ExtraBold))
        self.delete_lb_title.setStyleSheet("QLabel{\n"
                                                "color : #b1b1b1;\n"
                                            "}")
        self.delete_lb_title.setText("Delete Macro")

        self.delete_cb = QComboBox(self.body_frm)
        self.delete_cb.setGeometry(20, 347, 300, 24)
        self.delete_cb.setStyleSheet("QComboBox{\n"
                                        "font-family : 나눔고딕OTF;\n"
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
                                        "height : 18px;\n"
                                    "}\n"
                                    "QComboBox::drop-down{\n"
                                        "border-color : #b1b1b1;\n"
                                        "padding-right : 10px;\n"
                                    "}")

        self.delete_bt = QPushButton(self.body_frm)
        self.delete_bt.setGeometry(328, 347, 60, 24)
        self.delete_bt.setFont(QFont("나눔고딕OTF", 9, QFont.ExtraBold))
        self.delete_bt.setStyleSheet("QPushButton{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 8px;\n"
                                        "color : #cccccc;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "background-color : #aaaaaa;\n"
                                        "color : #222222;\n"
                                    "}")
        self.delete_bt.setText("삭제")


        # start_part
        self.start_lb_title = QLabel(self.body_frm)
        self.start_lb_title.setGeometry(20, 442, 101, 21)
        self.start_lb_title.setFont(QFont("나눔고딕OTF", 12, QFont.ExtraBold))
        self.start_lb_title.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.start_lb_title.setText("Start Macro")

        self.start_frm = QFrame(self.body_frm)
        self.start_frm.setGeometry(198, 443, 191, 21)
        self.start_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #4d4d4d;\n"
                                        "border-radius : 5px;\n"
                                    "}")

        self.start_rb_typeNum = QRadioButton(self.start_frm)
        self.start_rb_typeNum.setGeometry(6, 0, 91, 21)
        self.start_rb_typeNum.setFont(QFont("나눔고딕OTF", 10, QFont.ExtraBold))
        self.start_rb_typeNum.setStyleSheet("QRadioButton{\n"
                                                "color : #dddddd;\n"
                                            "}")
        self.start_rb_typeNum.setText("Num_type")
        self.start_rb_typeNum.setChecked(True)

        self.start_rb_typeTime = QRadioButton(self.start_frm)
        self.start_rb_typeTime.setGeometry(102, 0, 91, 21)
        self.start_rb_typeTime.setFont(QFont("나눔고딕OTF", 10, QFont.ExtraBold))
        self.start_rb_typeTime.setStyleSheet("QRadioButton{\n"
                                                "color : #dddddd;\n"
                                            "}")
        self.start_rb_typeTime.setText("Time_type")

        self.start_cb = QComboBox(self.body_frm)
        self.start_cb.setGeometry(20, 477, 163, 24)
        self.start_cb.setStyleSheet("QComboBox{\n"
                                        "font-family : 나눔고딕OTF;\n"
                                        "font-weight : bold;\n"
                                        "font-size : 10pt;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                        "background-color : #303030;\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 0px;\n"
                                        "color : #cccccc;\n"
                                        "selection-background-color : #ffffff;\n"
                                        "selection-color : #000000;\n"
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

        self.start_lb_1 = QLabel(self.body_frm)
        self.start_lb_1.setGeometry(192, 477, 41, 21)
        self.start_lb_1.setFont(QFont("나눔고딕OTF", 10, QFont.ExtraBold))
        self.start_lb_1.setStyleSheet("QLabel{\n"
                                            "color : #b1b1b1;\n"
                                        "}")
        self.start_lb_1.setText("을(를)")

        self.start_le = QLineEdit(self.body_frm)
        self.start_le.setGeometry(235, 479, 60, 22)
        self.start_le.setFont(QFont("나눔고딕OTF", 10, QFont.ExtraBold))
        self.start_le.setStyleSheet("QLineEdit{\n"
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
        self.start_le.setValidator(QIntValidator())
        self.start_le.setAlignment(Qt.AlignCenter)
        self.start_le.setText("0")

        self.start_lb_2 = QLabel(self.body_frm)
        self.start_lb_2.setGeometry(304, 477, 16, 21)
        self.start_lb_2.setFont(QFont("나눔고딕OTF", 10, QFont.ExtraBold))
        self.start_lb_2.setStyleSheet("QLabel{\n"
                                    "color : #b1b1b1;\n"
                                "}")
        self.start_lb_2.setText("번")

        self.start_bt_typeNum = QPushButton(self.body_frm)
        self.start_bt_typeNum.setGeometry(328, 477, 60, 24)
        self.start_bt_typeNum.setFont(QFont("나눔고딕OTF", 9, QFont.ExtraBold))
        self.start_bt_typeNum_inactive()
        self.start_bt_typeNum.setText("실행")

        self.start_bt_typeTime = QPushButton(self.body_frm)
        self.start_bt_typeTime.setGeometry(328, 477, 60, 24)
        self.start_bt_typeTime.setFont(QFont("나눔고딕OTF", 9, QFont.ExtraBold))
        self.start_bt_typeTime_inactive()
        self.start_bt_typeTime.setText("실행")
        self.start_bt_typeTime.hide()


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



    # typeChange_group
    def typeNum(self) : 
        global startType
        startType = "typeNum"

        self.start_cb.setGeometry(20, 477, 163, 24)
        self.start_lb_1.setGeometry(192, 477, 41, 21)
        self.start_le.setGeometry(235, 479, 60, 22)
        self.start_lb_2.setGeometry(304, 477, 16, 21)
        self.start_lb_2.setText("번")
        self.start_bt_typeTime.hide()
        self.start_bt_typeNum.show()
        

    def typeTime(self) : 
        global startType
        startType = "typeTime"
        
        self.start_cb.setGeometry(20, 477, 137, 24)
        self.start_lb_1.setGeometry(166, 477, 41, 21)
        self.start_le.setGeometry(210, 479, 60, 22)
        self.start_lb_2.setGeometry(280, 477, 41, 21)
        self.start_lb_2.setText("초 동안")
        self.start_bt_typeNum.hide()
        self.start_bt_typeTime.show()



    # activatedCondition_group
    ## << edit_bt (1/3) >> --------------------
    def edit_bt_inactive(self) : 
        self.edit_bt.setStyleSheet("QPushButton{\n"
                                        "border : 2px solid #aaaaaa;\n"
                                        "border-radius : 5px;\n"
                                        "color : #cccccc;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "background-color : #aaaaaa;\n"
                                        "color : #222222;\n"
                                    "}")

    def edit_bt_active(self) : 
        self.edit_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "background-color : #aaaaaa;\n"
                                            "color : #222222;\n"
                                        "}")


    ## << start_bt_typeNum (2/3) >> --------------------
    def start_bt_typeNum_inactive(self) : 
        self.start_bt_typeNum.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "color : #222222;\n"
                                            "background-color : #aaaaaa;\n"
                                        "}")

    def start_bt_typeNum_active(self) : 
        self.start_bt_typeNum.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "background-color : #aaaaaa;\n"
                                            "color : #222222;\n"
                                        "}")


    ## << start_bt_typeTime (3/3) >> --------------------
    def start_bt_typeTime_inactive(self) : 
        self.start_bt_typeTime.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "color : #cccccc;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "color : #222222;\n"
                                            "background-color : #aaaaaa;\n"
                                        "}")

    def start_bt_typeTime_active(self) : 
        self.start_bt_typeTime.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                            "background-color : #aaaaaa;\n"
                                            "color : #222222;\n"
                                        "}")





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    global main
    main = MainUI()
    main.show()
    sys.exit(app.exec_())