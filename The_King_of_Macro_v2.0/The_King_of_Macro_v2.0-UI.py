from PyQt5 import QtCore, QtGui, QtWidgets
from img.img import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.body_frm = QtWidgets.QFrame(self.centralwidget)
        self.body_frm.setGeometry(QtCore.QRect(4, 3, 406, 666))
        self.body_frm.setStyleSheet("QFrame{\n"
"background-color: #202020;\n"
"border-radius: 10px;\n"
"}")
        self.body_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_frm.setObjectName("body_frm")
        self.title_frm = QtWidgets.QFrame(self.body_frm)
        self.title_frm.setGeometry(QtCore.QRect(0, 0, 406, 41))
        self.title_frm.setStyleSheet("QFrame{\n"
"background-color: #464646;\n"
"border-radius: 10px;\n"
"}")
        self.title_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frm.setObjectName("title_frm")
        self.exit_bt = QtWidgets.QPushButton(self.title_frm)
        self.exit_bt.setGeometry(QtCore.QRect(377, 10, 22, 22))
        self.exit_bt.setMinimumSize(QtCore.QSize(16, 16))
        self.exit_bt.setMaximumSize(QtCore.QSize(30, 30))
        self.exit_bt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_bt.setStyleSheet("QPushButton{\n"
"    background-color: #aaaaaa;\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #666666;\n"
"}")
        self.exit_bt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_bt.setIcon(icon)
        self.exit_bt.setIconSize(QtCore.QSize(22, 11))
        self.exit_bt.setAutoRepeatDelay(300)
        self.exit_bt.setObjectName("exit_bt")
        self.title_lb = QtWidgets.QLabel(self.title_frm)
        self.title_lb.setGeometry(QtCore.QRect(112, 11, 185, 24))
        self.title_lb.setText("")
        self.title_lb.setPixmap(QtGui.QPixmap(":/img/Logo.png"))
        self.title_lb.setScaledContents(True)
        self.title_lb.setObjectName("title_lb")
        self.keep_bt = QtWidgets.QPushButton(self.title_frm)
        self.keep_bt.setGeometry(QtCore.QRect(346, 10, 22, 22))
        self.keep_bt.setMinimumSize(QtCore.QSize(16, 16))
        self.keep_bt.setMaximumSize(QtCore.QSize(23, 23))
        self.keep_bt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.keep_bt.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #aaaaaa;\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #666666;\n"
"}")
        self.keep_bt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/keep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.keep_bt.setIcon(icon1)
        self.keep_bt.setIconSize(QtCore.QSize(12, 12))
        self.keep_bt.setObjectName("keep_bt")
        self.line_1 = QtWidgets.QLabel(self.body_frm)
        self.line_1.setEnabled(True)
        self.line_1.setGeometry(QtCore.QRect(65, 160, 271, 16))
        self.line_1.setText("")
        self.line_1.setPixmap(QtGui.QPixmap(":/img/Line.png"))
        self.line_1.setScaledContents(True)
        self.line_1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_1.setWordWrap(False)
        self.line_1.setOpenExternalLinks(False)
        self.line_1.setObjectName("line_1")
        self.addName_lb_title = QtWidgets.QLabel(self.body_frm)
        self.addName_lb_title.setGeometry(QtCore.QRect(20, 76, 141, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addName_lb_title.setFont(font)
        self.addName_lb_title.setStyleSheet("QLabel{\n"
"    color: #b1b1b1;\n"
"    font-family: 나눔고딕;\n"
"    font-weight : bold;\n"
"    font-size: 11pt;\n"
"}")
        self.addName_lb_title.setObjectName("addName_lb_title")
        self.setting_bt = QtWidgets.QPushButton(self.body_frm)
        self.setting_bt.setGeometry(QtCore.QRect(374, 48, 24, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_bt.sizePolicy().hasHeightForWidth())
        self.setting_bt.setSizePolicy(sizePolicy)
        self.setting_bt.setMinimumSize(QtCore.QSize(16, 16))
        self.setting_bt.setMaximumSize(QtCore.QSize(30, 30))
        self.setting_bt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setting_bt.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #aaaaaa;\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #666666;\n"
"}")
        self.setting_bt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_bt.setIcon(icon2)
        self.setting_bt.setIconSize(QtCore.QSize(30, 30))
        self.setting_bt.setObjectName("setting_bt")
        self.addName_le = QtWidgets.QLineEdit(self.body_frm)
        self.addName_le.setGeometry(QtCore.QRect(20, 107, 300, 24))
        self.addName_le.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addName_le.setStyleSheet("QLineEdit{\n"
"    color : #dddddd;\n"
"    background-color : #303030;\n"
"    border : 2px solid #303030;\n"
"    border-radius : 5px;\n"
"    selection-color : #000000;\n"
"    selection-background-color : #ffffff;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    font-size : 10pt;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"    border-color : #aaaaaa;\n"
"}")
        self.addName_le.setText("")
        self.addName_le.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.addName_le.setClearButtonEnabled(False)
        self.addName_le.setObjectName("addName_le")
        self.addName_bt = QtWidgets.QPushButton(self.body_frm)
        self.addName_bt.setGeometry(QtCore.QRect(328, 107, 60, 24))
        self.addName_bt.setStyleSheet("QPushButton{\n"
"    border : 2px solid #aaaaaa;\n"
"    border-radius : 5px;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    color : #cccccc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border : 2px solid #aaaaaa;\n"
"    color : #222222;\n"
"    background-color : #aaaaaa;\n"
"}")
        self.addName_bt.setObjectName("addName_bt")
        self.edit_bt = QtWidgets.QPushButton(self.body_frm)
        self.edit_bt.setGeometry(QtCore.QRect(20, 227, 369, 24))
        self.edit_bt.setStyleSheet("QPushButton{\n"
"    border : 2px solid #aaaaaa;\n"
"    border-radius : 5px;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    color : #cccccc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border : 2px solid #aaaaaa;\n"
"    color : #222222;\n"
"    background-color : #aaaaaa;\n"
"}")
        self.edit_bt.setObjectName("edit_bt")
        self.edit_lb_title = QtWidgets.QLabel(self.body_frm)
        self.edit_lb_title.setGeometry(QtCore.QRect(20, 193, 81, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.edit_lb_title.setFont(font)
        self.edit_lb_title.setStyleSheet("QLabel{\n"
"    color: #b1b1b1;\n"
"    font-family: 나눔고딕;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}")
        self.edit_lb_title.setObjectName("edit_lb_title")
        self.line_2 = QtWidgets.QLabel(self.body_frm)
        self.line_2.setEnabled(True)
        self.line_2.setGeometry(QtCore.QRect(65, 280, 271, 16))
        self.line_2.setText("")
        self.line_2.setPixmap(QtGui.QPixmap(":/img/Line.png"))
        self.line_2.setScaledContents(True)
        self.line_2.setAlignment(QtCore.Qt.AlignCenter)
        self.line_2.setWordWrap(False)
        self.line_2.setOpenExternalLinks(False)
        self.line_2.setObjectName("line_2")
        self.delete_bt = QtWidgets.QPushButton(self.body_frm)
        self.delete_bt.setGeometry(QtCore.QRect(328, 347, 60, 24))
        self.delete_bt.setStyleSheet("QPushButton{\n"
"    border : 2px solid #aaaaaa;\n"
"    border-radius : 5px;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    color : #cccccc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border : 2px solid #aaaaaa;\n"
"    color : #222222;\n"
"    background-color : #aaaaaa;\n"
"}")
        self.delete_bt.setObjectName("delete_bt")
        self.delete_lb_title = QtWidgets.QLabel(self.body_frm)
        self.delete_lb_title.setGeometry(QtCore.QRect(20, 313, 101, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delete_lb_title.setFont(font)
        self.delete_lb_title.setStyleSheet("QLabel{\n"
"    color: #b1b1b1;\n"
"    font-family: 나눔고딕;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}")
        self.delete_lb_title.setObjectName("delete_lb_title")
        self.line_3 = QtWidgets.QLabel(self.body_frm)
        self.line_3.setEnabled(True)
        self.line_3.setGeometry(QtCore.QRect(62, 407, 271, 16))
        self.line_3.setText("")
        self.line_3.setPixmap(QtGui.QPixmap(":/img/Line.png"))
        self.line_3.setScaledContents(True)
        self.line_3.setAlignment(QtCore.Qt.AlignCenter)
        self.line_3.setWordWrap(False)
        self.line_3.setOpenExternalLinks(False)
        self.line_3.setObjectName("line_3")
        self.delete_cb = QtWidgets.QComboBox(self.body_frm)
        self.delete_cb.setGeometry(QtCore.QRect(20, 347, 300, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_cb.sizePolicy().hasHeightForWidth())
        self.delete_cb.setSizePolicy(sizePolicy)
        self.delete_cb.setStyleSheet("QComboBox{\n"
"    border-radius : 5px;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    font-size : 10pt;\n"
"    color : #cccccc;\n"
"    background-color : #303030;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border : 2px solid #aaaaaa;\n"
"    border-radius : 0px;\n"
"    background-color : #303030;\n"
"    color : #cccccc;\n"
"    selection-background-color : #ffffff;\n"
"    selection-color : #000000;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image : url(:/img/down.png);\n"
"    width : 18px;\n"
"    Height : 18px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border-color : #b1b1b1;\n"
"    padding-right :10px;\n"
"}")
        self.delete_cb.setEditable(False)
        self.delete_cb.setMinimumContentsLength(0)
        self.delete_cb.setIconSize(QtCore.QSize(16, 16))
        self.delete_cb.setDuplicatesEnabled(False)
        self.delete_cb.setFrame(True)
        self.delete_cb.setObjectName("delete_cb")
        self.delete_cb.addItem("")
        self.delete_cb.addItem("")
        self.delete_cb.addItem("")
        self.start_bt = QtWidgets.QPushButton(self.body_frm)
        self.start_bt.setGeometry(QtCore.QRect(328, 477, 60, 24))
        self.start_bt.setStyleSheet("QPushButton{\n"
"    border : 2px solid #aaaaaa;\n"
"    border-radius : 5px;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    color : #cccccc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border : 2px solid #aaaaaa;\n"
"    color : #222222;\n"
"    background-color : #aaaaaa;\n"
"}")
        self.start_bt.setObjectName("start_bt")
        self.start_cb = QtWidgets.QComboBox(self.body_frm)
        self.start_cb.setGeometry(QtCore.QRect(20, 477, 163, 24))
        self.start_cb.setStyleSheet("QComboBox{\n"
"    border-radius : 5px;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    font-size : 10pt;\n"
"    color : #cccccc;\n"
"    background-color : #303030;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border : 2px solid #aaaaaa;\n"
"    border-radius : 0px;\n"
"    background-color : #303030;\n"
"    color : #cccccc;\n"
"    selection-background-color : #ffffff;\n"
"    selection-color : #000000;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image : url(:/img/down.png);\n"
"    width : 18px;\n"
"    Height : 18px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border-color : #b1b1b1;\n"
"    padding-right : 10px;\n"
"}")
        self.start_cb.setObjectName("start_cb")
        self.start_cb.addItem("")
        self.start_cb.addItem("")
        self.start_cb.addItem("")
        self.start_lb_title = QtWidgets.QLabel(self.body_frm)
        self.start_lb_title.setGeometry(QtCore.QRect(20, 442, 101, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.start_lb_title.setFont(font)
        self.start_lb_title.setStyleSheet("QLabel{\n"
"    color: #b1b1b1;\n"
"    font-family: 나눔고딕;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}")
        self.start_lb_title.setObjectName("start_lb_title")
        self.start_lb_1 = QtWidgets.QLabel(self.body_frm)
        self.start_lb_1.setGeometry(QtCore.QRect(192, 477, 41, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start_lb_1.setFont(font)
        self.start_lb_1.setStyleSheet("QLabel{\n"
"    color: #b1b1b1;\n"
"    font-family: 나눔고딕;\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"}")
        self.start_lb_1.setObjectName("start_lb_1")
        self.start_sb_1 = QtWidgets.QSpinBox(self.body_frm)
        self.start_sb_1.setGeometry(QtCore.QRect(235, 478, 60, 22))
        self.start_sb_1.setStyleSheet("QSpinBox{\n"
"    color : #dddddd;\n"
"    background-color : #303030;\n"
"    border : 2px solid #303030;\n"
"    border-radius : 5px;\n"
"    selection-color : #000000;\n"
"    selection-background-color : #ffffff;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    font-size : 10pt;\n"
"}\n"
"\n"
"QSpinBox::focus{\n"
"    border-color : #aaaaaa;\n"
"}")
        self.start_sb_1.setAlignment(QtCore.Qt.AlignCenter)
        self.start_sb_1.setMaximum(999999999)
        self.start_sb_1.setObjectName("start_sb_1")
        self.start_lb_2 = QtWidgets.QLabel(self.body_frm)
        self.start_lb_2.setGeometry(QtCore.QRect(304, 477, 16, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start_lb_2.setFont(font)
        self.start_lb_2.setStyleSheet("QLabel{\n"
"    color: #b1b1b1;\n"
"    font-family: 나눔고딕;\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"}")
        self.start_lb_2.setObjectName("start_lb_2")
        self.start_frm = QtWidgets.QFrame(self.body_frm)
        self.start_frm.setGeometry(QtCore.QRect(198, 443, 191, 21))
        self.start_frm.setStyleSheet("QFrame{\n"
"background-color: #4d4d4d;\n"
"border-radius: 5px;\n"
"}")
        self.start_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.start_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start_frm.setObjectName("start_frm")
        self.start_rb_num = QtWidgets.QRadioButton(self.start_frm)
        self.start_rb_num.setGeometry(QtCore.QRect(6, 0, 91, 21))
        self.start_rb_num.setStyleSheet("QRadioButton{\n"
"    color : #dddddd;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    font-size : 10pt;\n"
"}")
        self.start_rb_num.setObjectName("start_rb_num")
        self.start_rb_time = QtWidgets.QRadioButton(self.start_frm)
        self.start_rb_time.setGeometry(QtCore.QRect(102, 0, 91, 21))
        self.start_rb_time.setStyleSheet("QRadioButton{\n"
"    color : #dddddd;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    font-size : 10pt;\n"
"}")
        self.start_rb_time.setObjectName("start_rb_time")
        self.noticeBoard = QtWidgets.QListWidget(self.centralwidget)
        self.noticeBoard.setGeometry(QtCore.QRect(22, 534, 370, 118))
        self.noticeBoard.setStyleSheet("QListWidget{\n"
"    background-color : #4d4d4d;\n"
"    border-radius : 8px;\n"
"    color : #dddddd;\n"
"    font-family : 나눔고딕;\n"
"    font-weight : bold;\n"
"    font-size : 9pt;\n"
"    padding-left : 3px;\n"
"}\n"
"\n"
"QListWidget::item{\n"
"    margin : 1.5px;\n"
"}\n"
"\n"
"QListWidget QScrollBar{\n"
"    background : #aaaaaa;\n"
"}\n"
"\n"
"QListWidget::item::selected{\n"
"    background : #2b2b2b;\n"
"    color : #dddddd;\n"
"}\n"
"\n"
"QListWidget::item::hover {\n"
"    background : #434343;\n"
"}")
        self.noticeBoard.setAutoScroll(True)
        self.noticeBoard.setProperty("showDropIndicator", True)
        self.noticeBoard.setDragEnabled(False)
        self.noticeBoard.setObjectName("noticeBoard")
        item = QtWidgets.QListWidgetItem()
        self.noticeBoard.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.noticeBoard.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addName_lb_title.setText(_translate("MainWindow", "Add Macro\'s Name"))
        self.addName_bt.setText(_translate("MainWindow", "추가"))
        self.edit_bt.setText(_translate("MainWindow", "편집"))
        self.edit_lb_title.setText(_translate("MainWindow", "Edit Macro"))
        self.delete_bt.setText(_translate("MainWindow", "삭제"))
        self.delete_lb_title.setText(_translate("MainWindow", "Delete Macro"))
        self.delete_cb.setItemText(0, _translate("MainWindow", "테스트 매크로 1"))
        self.delete_cb.setItemText(1, _translate("MainWindow", "테스트 매크로 2"))
        self.delete_cb.setItemText(2, _translate("MainWindow", "테스트 매크로 3"))
        self.start_bt.setText(_translate("MainWindow", "실행"))
        self.start_cb.setItemText(0, _translate("MainWindow", "테스트 매크로 1"))
        self.start_cb.setItemText(1, _translate("MainWindow", "테스트 매크로 2"))
        self.start_cb.setItemText(2, _translate("MainWindow", "테스트 매크로 3"))
        self.start_lb_title.setText(_translate("MainWindow", "Start Macro"))
        self.start_lb_1.setText(_translate("MainWindow", "을(를)"))
        self.start_lb_2.setText(_translate("MainWindow", "번"))
        self.start_rb_num.setText(_translate("MainWindow", "Num_type"))
        self.start_rb_time.setText(_translate("MainWindow", "Time_type"))
        __sortingEnabled = self.noticeBoard.isSortingEnabled()
        self.noticeBoard.setSortingEnabled(False)
        item = self.noticeBoard.item(0)
        item.setText(_translate("MainWindow", "[system] <The King of Macro_v2.0> - Made by. Yoonmen"))
        item = self.noticeBoard.item(1)
        item.setText(_translate("MainWindow", "[system] 환영합니다. DATA.csv를 불러와주세요."))
        self.noticeBoard.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
