from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton, QLineEdit, QComboBox, QRadioButton, QListWidget
from PySide2.QtCore import Qt, QSize, QEvent
from PySide2.QtGui import QIcon, QFontDatabase, QFont, QIntValidator
from time import strftime


class MainUI(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()

    def mainUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(414, 695)
        self.setWindowTitle("The_King_of_Macro")
        self.setWindowIcon(QIcon("KOM.ico"))
        QFontDatabase.addApplicationFont("./NanumGothicBold.otf")

        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(4, 3, 406, 666)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #202020;\n"
                                        "border-radius : 10px;\n"
                                    "}")
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(18)
        self.shadow.setOffset(0, 0)
        self.body_frm.setGraphicsEffect(self.shadow)

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
        self.title_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/title_main.png);\n"
                                    "}")

        title_bt_styleSheet = ("QPushButton{\n"
                                    "background-color : #aaaaaa;\n"
                                    "border-radius : 10px;\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                    "background-color : #666666;\n"
                                "}")

        self.keep_bt = QPushButton(self.title_frm)
        self.keep_bt.setGeometry(346, 10, 22, 22)
        self.keep_bt.setStyleSheet(title_bt_styleSheet)
        icon = QIcon()
        icon.addPixmap(":/img/keep.png")
        self.keep_bt.setIcon(icon)
        self.keep_bt.setIconSize(QSize(12, 12))

        self.exit_bt = QPushButton(self.title_frm)
        self.exit_bt.setGeometry(377, 10, 22, 22)
        self.exit_bt.setStyleSheet(title_bt_styleSheet)
        icon.addPixmap(":/img/exit.png")
        self.exit_bt.setIcon(icon)
        self.exit_bt.setIconSize(QSize(22, 11))

        self.setting_bt = QPushButton(self.body_frm)
        self.setting_bt.setGeometry(374, 48, 24, 24)
        self.setting_bt.setStyleSheet("QPushButton{\n"
                                            "background-color : #aaaaaa;\n"
                                            "border-radius : 5px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "background-color : #666666;\n"
                                        "}")
        icon.addPixmap(":/img/setting.png")
        self.setting_bt.setIcon(icon)
        self.setting_bt.setIconSize(QSize(30, 30))

        line_styleSheet = ("QLabel{\n"
                                "image : url(:/img/line.png);\n"
                            "}")

        self.line_1 = QLabel(self.body_frm)
        self.line_1.setGeometry(67, 160, 271, 16)
        self.line_1.setStyleSheet(line_styleSheet)

        self.line_2 = QLabel(self.body_frm)
        self.line_2.setGeometry(67, 280, 271, 16)
        self.line_2.setStyleSheet(line_styleSheet)

        self.line_3 = QLabel(self.body_frm)
        self.line_3.setGeometry(67, 407, 271, 16)
        self.line_3.setStyleSheet(line_styleSheet)


        # addNewMacro_part
        lb_styleSheet = ("QLabel{\n"
                            "color : #b1b1b1;\n"
                        "}")

        self.addNewMacro_lb = QLabel(self.body_frm)
        self.addNewMacro_lb.setGeometry(20, 76, 151, 21)
        self.addNewMacro_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.addNewMacro_lb.setStyleSheet(lb_styleSheet)
        self.addNewMacro_lb.setText("Add Macro's Name")

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

        self.addNewMacro_le = QLineEdit(self.body_frm)
        self.addNewMacro_le.setGeometry(20, 107, 300, 24)
        self.addNewMacro_le.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.addNewMacro_le.setStyleSheet(le_styleSheet)
        
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

        self.addNewMacro_bt = QPushButton(self.body_frm)
        self.addNewMacro_bt.setGeometry(328, 107, 60, 24)
        self.addNewMacro_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.addNewMacro_bt.setStyleSheet(bt_styleSheet)
        self.addNewMacro_bt.setText("추가")


        # edit_part
        self.edit_lb = QLabel(self.body_frm)
        self.edit_lb.setGeometry(20, 193, 81, 21)
        self.edit_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.edit_lb.setStyleSheet(lb_styleSheet)
        self.edit_lb.setText("Edit Macro")

        self.edit_bt = QPushButton(self.body_frm)
        self.edit_bt.setGeometry(20, 227, 369, 24)
        self.edit_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.edit_bt.setStyleSheet(bt_styleSheet)
        self.edit_bt.setText("편집")


        # delete_part
        self.delete_lb = QLabel(self.body_frm)
        self.delete_lb.setGeometry(20, 313, 101, 21)
        self.delete_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.delete_lb.setStyleSheet(lb_styleSheet)
        self.delete_lb.setText("Delete Macro")

        cb_styleSheet = ("QComboBox{\n"
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

        self.delete_cb = QComboBox(self.body_frm)
        self.delete_cb.setGeometry(20, 347, 300, 24)
        self.delete_cb.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.delete_cb.setStyleSheet(cb_styleSheet)
        
        self.delete_bt = QPushButton(self.body_frm)
        self.delete_bt.setGeometry(328, 347, 60, 24)
        self.delete_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.delete_bt.setStyleSheet(bt_styleSheet)
        self.delete_bt.setText("삭제")


        # start_part
        self.start_lb = QLabel(self.body_frm)
        self.start_lb.setGeometry(20, 442, 101, 21)
        self.start_lb.setFont(QFont("나눔고딕OTF", 12, QFont.Bold))
        self.start_lb.setStyleSheet(lb_styleSheet)
        self.start_lb.setText("Start Macro")

        self.start_type_frm = QFrame(self.body_frm)
        self.start_type_frm.setGeometry(198, 443, 191, 21)
        self.start_type_frm.setStyleSheet("QFrame{\n"
                                                "background-color : #4d4d4d;\n"
                                                "border-radius : 5px;\n"
                                            "}")

        rb_styleSheet = ("QRadioButton{\n"
                            "color : #dddddd;\n"
                        "}")

        self.start_typeNum_rb = QRadioButton(self.start_type_frm)
        self.start_typeNum_rb.setGeometry(6, 0, 91, 21)
        self.start_typeNum_rb.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_typeNum_rb.setStyleSheet(rb_styleSheet)
        self.start_typeNum_rb.setText("Num_type")
        self.start_typeNum_rb.setChecked(True)
        self.start_typeNum_rb.installEventFilter(self)

        self.start_typeTime_rb = QRadioButton(self.start_type_frm)
        self.start_typeTime_rb.setGeometry(102, 0, 91, 21)
        self.start_typeTime_rb.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_typeTime_rb.setStyleSheet(rb_styleSheet)
        self.start_typeTime_rb.setText("Time_type")
        self.start_typeTime_rb.installEventFilter(self)

        self.start_cb = QComboBox(self.body_frm)
        self.start_cb.setGeometry(20, 476, 163, 24)
        self.start_cb.setStyleSheet(cb_styleSheet)

        self.start_lb_1 = QLabel(self.body_frm)
        self.start_lb_1.setGeometry(192, 478, 41, 21)
        self.start_lb_1.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_lb_1.setStyleSheet(lb_styleSheet)
        self.start_lb_1.setText("을(를)")

        self.start_le = QLineEdit(self.body_frm)
        self.start_le.setGeometry(235, 478, 60, 22)
        self.start_le.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_le.setStyleSheet(le_styleSheet)
        self.start_le.setValidator(QIntValidator())
        self.start_le.setAlignment(Qt.AlignCenter)
        self.start_le.setText("0")

        self.start_lb_2 = QLabel(self.body_frm)
        self.start_lb_2.setGeometry(304, 478, 16, 21)
        self.start_lb_2.setFont(QFont("나눔고딕OTF", 10, QFont.Bold))
        self.start_lb_2.setStyleSheet(lb_styleSheet)
        self.start_lb_2.setText("번")

        self.start_bt = QPushButton(self.body_frm)
        self.start_bt.setGeometry(328, 477, 60, 24)
        self.start_bt.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.start_bt.setStyleSheet(bt_styleSheet)
        self.start_bt.setText("실행")

        self.log_lw = QListWidget(self.body_frm)
        self.log_lw.setGeometry(18, 529, 370, 118)
        self.log_lw.setFont(QFont("나눔고딕OTF", 9, QFont.Bold))
        self.log_lw.setStyleSheet("QListWidget{\n"
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
        self.log_lw.setFocusPolicy(Qt.NoFocus)
        self.log_lw.addItem(f"[{strftime('%H:%M:%S')}] <The King of Macro v2.2> - Made by. Yoonmen")
        self.log_lw.addItem(f"[{strftime('%H:%M:%S')}] 환영합니다. data.dat 파일을 불러와주세요.")
        self.log_lw.setCurrentRow(self.log_lw.count()-1)



    def setCenterPoint(self, event) : 
        self.centerPoint = event.globalPos()
    
    def moveWindow(self, event) : 
        if event.buttons() == Qt.LeftButton : 
            self.move(self.pos() + event.globalPos() - self.centerPoint)
            self.centerPoint = event.globalPos()
    


    def eventFilter(self, object, event) : 
        if object == self.start_typeNum_rb : 
            if event.type() == QEvent.MouseButtonPress : 
                self.start_cb.setGeometry(20, 476, 163, 24)
                self.start_lb_1.setGeometry(192, 478, 41, 21)
                self.start_le.setGeometry(235, 478, 60, 22)
                self.start_lb_2.setGeometry(304, 478, 16, 21)
                self.start_lb_2.setText("번")

        elif object == self.start_typeTime_rb : 
            if event.type() == QEvent.MouseButtonPress : 
                self.start_cb.setGeometry(20, 476, 137, 24)
                self.start_lb_1.setGeometry(166, 478, 41, 21)
                self.start_le.setGeometry(210, 478, 60, 22)
                self.start_lb_2.setGeometry(280, 478, 41, 21)
                self.start_lb_2.setText("초 동안")

        return False





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    mainUI = MainUI()
    mainUI.show()
    sys.exit(app.exec_())
