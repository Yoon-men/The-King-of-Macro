import sys
from PySide2 import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import csv
import keyboard
import mouse
import pyautogui
import time


class Task(QObject) : 
    # addSignal = Signal(bool)
    addSignal = Signal()
    # notloadSignal = Signal(bool)
    notloadSignal =Signal()
    # emptySignal = Signal(bool)
    emptySignal = Signal()

    def addName(self) : 
        if Load_status == True : 
            # macroName = [self.addName_le.text()]
            # self.addName_le.setText('')
            
            if macroName[0] == '' : 
                emptySign = True
                # self.emptySignal.emit(emptySign)
                self.emptySignal.emit()
            else : 
                # Add macro's name in List to all of comboBox
                addSign = True
                # self.addSignal.emit(addSign)
                self.addSignal.emit()

                # self.noticeBoard.addItem('[system] 매크로를 추가했습니다.')
        else : 
            notloadSign = True
            # self.notloadSignal.emit(notloadSign)
            self.notloadSignal.emit()

    def addClick(self) : 
        self.power = True
        
        timeUP = time.time() + 10
        while time.time() <= timeUP and self.power == True : 
            print("[무한의 정령 케인인] 얘! 클릭 추가 버튼을 눌렀니?!")
            time.sleep(1)
        print("[무한의 정령 케인인] 얘! 무한한 순환의 굴레에서 벗어난걸 축하한단다!")
        self.power = False
    

    def addKeyboard(self) : 
        self.power = True
        while self.power == True : 
            timeUP = time.time() + 10
            while time.time() <= timeUP : 
                print("[무한의 정령 케인인] 얘! 키보드 추가 버튼을 눌렀니?!")
                time.sleep(1)
            print("[무한의 정령 케인인] 얘! 무한한 순환의 굴레에서 벗어난걸 축하한단다!")
            self.power = False

    
    def startMacro(self) : 
        self.power = True
        while self.power == True : 
            timeUP = time.time() + 10
            while time.time() <= timeUP : 
                print("[무한의 정령 케인인] 얘! 매크로 시작 버튼을 눌렀니?!")
                time.sleep(1)
            print("[무한의 정령 케인인] 얘! 무한한 순환의 굴레에서 벗어난걸 축하한단다!")
            self.power = False
    

    def stop(self) : 
        self.power = False
        print("[귀찮음의 정령 케인인] 꺼져!")
        
 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.thread = QThread()
        self.thread.start()
        global task
        task = Task()
        task.moveToThread(self.thread)

        self.initUI()


    def initUI(self) : 
        
        # Default Setting
        self.setFixedSize(351, 664)
        self.setWindowTitle("The_King_of_Macro_v1.6")

        self.title = QLabel(self)
        self.title.setGeometry(60, 10, 241, 71)
        font = QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setText("The King of Macro")

        self.version = QLabel(self)
        self.version.setGeometry(10, 10, 64, 15)
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.version.setFont(font)
        self.version.setText("v1.6")

        self.loadButton = QToolButton(self)
        self.loadButton.setGeometry(280, 10, 61, 20)
        self.loadButton.setText("불러오기")

        self.noticeBoard = QListWidget(self)
        self.noticeBoard.setGeometry(20, 550, 311, 81)

        self.dev = QLabel(self)
        self.dev.setGeometry(130, 640, 101, 16)
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.dev.setFont(font)
        self.dev.setText("by. Yoonmen")


        # addName_group
        self.addName_group = QLabel(self)
        self.addName_group.setGeometry(20, 70, 131, 20)
        self.addName_group.setText("<Add Macro's Name>")

        self.addName_le = QLineEdit(self)
        self.addName_le.setGeometry(20, 100, 251, 20)
        self.addName_le.setPlaceholderText("ex) 자동사냥")
        self.addName_le.setClearButtonEnabled(True)

        self.addName_bt = QPushButton(self)
        self.addName_bt.setGeometry(280, 100, 51, 21)
        self.addName_bt.setText("추가")


        # addClick_group
        self.addClick_group = QLabel(self)
        self.addClick_group.setGeometry(20, 140, 101, 20)
        self.addClick_group.setText("<Add Click>")

        self.addClick_cb = QComboBox(self)
        self.addClick_cb.setGeometry(20, 170, 101, 21)

        self.addClick_lb_1 = QLabel(self)
        self.addClick_lb_1.setGeometry(130, 170, 16, 20)
        self.addClick_lb_1.setText("에")

        self.addClick_lb_2 = QLabel(self)
        self.addClick_lb_2.setGeometry(210, 170, 71, 20)
        self.addClick_lb_2.setText("초 간격으로")

        self.addClick_ds = QDoubleSpinBox(self)
        self.addClick_ds.setGeometry(150, 170, 51, 21)
        
        self.addClick_bt = QPushButton(self)
        self.addClick_bt.setGeometry(280, 170, 51, 21)
        self.addClick_bt.setText("클릭")

        self.addClick_lb_3 = QLabel(self)
        self.addClick_lb_3.setGeometry(80, 200, 191, 20)
        self.addClick_lb_3.setText("(순서에 맞게 클릭을 진행하세요.)")

        self.addClick_cc = QPushButton(self)
        self.addClick_cc.setGeometry(20, 170, 311, 21)
        self.addClick_cc.setText("취소")
        self.addClick_cc.hide()
        
        # addKeyboard_group
        self.addKeyboard_group = QLabel(self)
        self.addKeyboard_group.setGeometry(20, 240, 101, 20)
        self.addKeyboard_group.setText("<Add Keyboard>")

        self.addKeyboard_cb = QComboBox(self)
        self.addKeyboard_cb.setGeometry(20, 270, 101, 22)

        self.addKeyboard_lb_1 = QLabel(self)
        self.addKeyboard_lb_1.setGeometry(130, 270, 16, 20)
        self.addKeyboard_lb_1.setText("에")

        self.addKeyboard_ds = QDoubleSpinBox(self)
        self.addKeyboard_ds.setGeometry(150, 270, 51, 22)

        self.addKeyboard_lb_2 = QLabel(self)
        self.addKeyboard_lb_2.setGeometry(210, 270, 71, 20)
        self.addKeyboard_lb_2.setText("초 간격으로")

        self.addKeyboard_bt = QPushButton(self)
        self.addKeyboard_bt.setGeometry(280, 270, 51, 21)
        self.addKeyboard_bt.setText("입력")

        self.addKeyboard_lb_3 = QLabel(self)
        self.addKeyboard_lb_3.setGeometry(80, 300, 191, 20)
        self.addKeyboard_lb_3.setText("(순서에 맞게 클릭을 진행하세요.)")

        self.addKeyboard_cc = QPushButton(self)
        self.addKeyboard_cc.setGeometry(20, 270, 311, 21)
        self.addKeyboard_cc.setText("취소")
        self.addKeyboard_cc.hide()

        self.addLine = QFrame(self)
        self.addLine.setGeometry(110, 350, 118, 3)
        self.addLine.setFrameShape(QFrame.HLine)
        self.addLine.setFrameShadow(QFrame.Sunken)
        

        # delete_group
        self.delete_group = QLabel(self)
        self.delete_group.setGeometry(20, 370, 101, 20)
        self.delete_group.setText("<Delete Macro>")

        self.delete_cb = QComboBox(self)
        self.delete_cb.setGeometry(20, 400, 211, 22)

        self.delete_lb_1 = QLabel(self)
        self.delete_lb_1.setGeometry(240, 400, 41, 20)
        self.delete_lb_1.setText("을(를)")

        self.delete_bt = QPushButton(self)
        self.delete_bt.setGeometry(280, 400, 51, 21)
        self.delete_bt.setText("삭제")

        self.deleteLine = QFrame(self)
        self.deleteLine.setGeometry(110, 460, 118, 3)
        self.deleteLine.setFrameShape(QFrame.HLine)
        self.deleteLine.setFrameShadow(QFrame.Sunken)


        # start_group
        self.start_group = QLabel(self)
        self.start_group.setGeometry(20, 480, 101, 20)
        self.start_group.setText("<Start Macro>")

        self.start_cb = QComboBox(self)
        self.start_cb.setGeometry(20, 510, 141, 22)

        self.start_lb_1 = QLabel(self)
        self.start_lb_1.setGeometry(170, 510, 41, 20)
        self.start_lb_1.setText("을(를)")

        self.start_sb = QSpinBox(self)
        self.start_sb.setGeometry(210, 510, 42, 22)
        self.start_sb.setMaximum(99999999)

        self.start_lb_2 = QLabel(self)
        self.start_lb_2.setGeometry(260, 510, 16, 20)
        self.start_lb_2.setText("번")

        self.start_bt = QPushButton(self)
        self.start_bt.setGeometry(280, 510, 51, 21)
        self.start_bt.setText("실행")

        self.start_cc = QPushButton(self)
        self.start_cc.setGeometry(20, 510, 311, 21)
        self.start_cc.setText("중지")
        self.start_cc.hide()

        self.start_lb_type = QLabel(self)
        self.start_lb_type.setGeometry(110, 480, 211, 20)
        self.start_lb_type.setText("-   [ Type :                               ]")

        self.start_rb_num = QRadioButton(self)
        self.start_rb_num.setGeometry(190, 480, 51, 16)
        self.start_rb_num.setText("횟수")

        self.start_rb_min = QRadioButton(self)
        self.start_rb_min.setGeometry(260, 480, 51, 16)
        self.start_rb_min.setText("분")

        # If Signal is coming
        self.loadButton.clicked.connect(self.loadCSV)
        self.addName_bt.clicked.connect(self.SEMI_addName_1)
        self.addName_bt.clicked.connect(task.addName)
        self.addName_le.returnPressed.connect(self.SEMI_addName_1)
        self.addName_le.returnPressed.connect(task.addName)
        self.addClick_bt.clicked.connect(self.SEMI_addClick)
        self.addClick_bt.clicked.connect(task.addClick)
        self.addClick_cc.clicked.connect(self.stopThread)
        # self.addKeyboard_bt.clicked.connect(self.SEMI_addKeyboard)
        # self.addKeyboard_bt.clicked.conenct(self.function.addKeyboard)
        self.delete_bt.clicked.connect(self.deleteMacro)
        self.start_bt.clicked.connect(self.SEMI_startMacro)
        self.addClick_cc.clicked.connect(self.stopThread)
        self.addKeyboard_cc.clicked.connect(self.stopThread)
        self.start_cc.clicked.connect(self.stopThread)
        task.addSignal.connect(self.SEMI_addName_2)
        task.emptySignal.connect(self.emptyName)
        task.notloadSignal.connect(self.notloadMessage)

        # When program is started
        global Load_status
        Load_status = True
        self.noticeBoard.addItem("[system] 환영합니다. DATA.csv를 불러와주세요.")
    

    def loadCSV(self) : 
        timeUP = time.time() + 10
        while time.time() <= timeUP :
            print("[무한의 정령 케인인] 얘! 불러오기 버튼을 눌렀니?!")
            time.sleep(1)
        print("[무한의 정령 케인인] 얘! 무한한 순환의 굴레에서 벗어난걸 축하한단다!")
        

    def SEMI_addName_1(self) : 
        global macroName
        macroName = [self.addName_le.text()]
        self.addName_le.setText("")


    def SEMI_addName_2(self) : 
        # if addSign == True : 
            self.addClick_cb.addItem(macroName[0])
            self.addKeyboard_cb.addItem(macroName[0])
            self.delete_cb.addItem(macroName[0])
            self.start_cb.addItem(macroName[0])

            self.noticeBoard.addItem('[system] 매크로를 추가했습니다.')
    
    def emptyName(self) : 
        # if emptySign == True : 
            self.noticeBoard.addItem('[system] 공백을 이름으로 사용할 수 없습니다.')
    
    def notloadMessage(self) : 
        # if notloadSign == True : 
            self.noticeBoard.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')


    def SEMI_addClick(self) : 
        self.addClick_cb.hide()
        self.addClick_lb_1.hide()
        self.addClick_lb_2.hide()
        self.addClick_ds.hide()
        self.addClick_bt.hide()
        self.addClick_cc.show()


    def SEMI_addKeyboard(self) : 
        self.addKeyboard_cb.hide()
        self.addKeyboard_lb_1.hide()
        self.addKeyboard_ds.hide()
        self.addKeyboard_lb_2.hide()
        self.addKeyboard_bt.hide()
        self.addKeyboard_cc.show()
        


    def deleteMacro(self) : 
        timeUP = time.time() + 10
        while time.time() <= timeUP : 
            print("[무한의 정령 케인인] 얘! 삭제 버튼을 눌렀니?!")
            time.sleep(1)
        print("[무한의 정령 케인인] 얘! 무한한 순환의 굴레에서 벗어난걸 축하한단다!")

    
    def SEMI_startMacro(self) : 
        self.start_cb.hide()
        self.start_lb_1.hide()
        self.start_sb.hide()
        self.start_lb_2.hide()
        self.start_bt.hide()
        self.start_cc.show()
        self.function.startMacro

    def stopThread(self) : 
        self.addClick_cb.show()
        self.addClick_lb_1.show()
        self.addClick_lb_2.show()
        self.addClick_ds.show()
        self.addClick_bt.show()
        self.addClick_cc.hide()
        self.function.stop()

        

if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()