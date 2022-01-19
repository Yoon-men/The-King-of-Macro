"""
<The_King_of_Macro_v1.6> - 22.1.??. (???) ??:??
* Made by Yoonmen *

[update]
1. 이전 버전에서 나타난 버그 해결
2. 매크로 실행 타입 변경 기능 추가(1. 횟수 / 2. 시간)
3. 매크로 동작 중 종료 예약 기능 추가(매크로 동작 중 ESC키 클릭)
"""

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
import copy

class Task1(QObject) : 
    # DATA.csv를 불러오지 않은 상태
    notLoadSignal = Signal()

    # X1 = 매크로 이름만 입력된 상태
    # X2 = 매크로 내용까지 입력된 상태
    addDelaySignal_C1 = Signal()
    addDelaySignal_C2 = Signal()
    addDelaySignal_K1 = Signal()
    addDelaySignal_K2 = Signal()

    # 키보드 입력 중 ESC가 입력된 상태
    ESCis_pressedSignal = Signal()

    # 매크로가 몇 번 더 동작해야 하는지를 카운트
    # (For startMacro_typeNum)
    decreaseSignal_typeNum = Signal(int)

    # 사용자 요청 작업이 완료된 상태
    noticeClickSignal = Signal()
    noticeKeyboardSignal = Signal()
    noticeMacroSignal_typeNum = Signal()
    noticeMacroSignal_typeTime = Signal()

    def addClick(self) : 
        self.power = True
        if Load_status == True : 
            while self.power == True : 
                if len(CSV_data[clickObject + 1]) == 1 : 
                    self.addDelaySignal_C1.emit()

                else : 
                    self.addDelaySignal_C2.emit()
                    
                while True : 
                    if mouse.is_pressed('left') : 
                        x, y = pyautogui.position()
                        CSV_data[clickObject + 1].append((x, y))

                        CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
                        writer = csv.writer(CSV_file)
                        writer.writerows(CSV_data)

                        self.noticeClickSignal.emit()
                        break
                    
                    elif self.power == False : 
                        break

                self.power = False

        else : 
            self.notLoadSignal.emit()



    def addKeyboard(self) : 
        self.power = True
        if Load_status == True : 
            while self.power == True : 
                if len(CSV_data[keyboardObject + 1]) == 1 : 
                    self.addDelaySignal_K1.emit()

                else : 
                    self.addDelaySignal_K2.emit()


                key = keyboard.read_hotkey(suppress=False)
                if key == "ESC" : 
                    self.ESCis_pressedSignal.emit()
                    self.power = False

                else : 
                    CSV_data[keyboardObject + 1].append(key)

                    CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
                    writer = csv.writer(CSV_file)
                    writer.writerows(CSV_data)

                    self.noticeKeyboardSignal.emit()
                    self.power = False

        else : 
            self.notLoadSignal.emit()



    def startMacro_typeNum(self) : 
        global run_num
        run_num = runNum
        self.power = True
        if Load_status == True :
            CSV_data_copy = copy.deepcopy(CSV_data)
            delay = float(CSV_data_copy[startObject + 1][1])
            macro_Num = len(CSV_data_copy[startObject + 1]) - 2
            while self.power == True and run_num != 0 : 
                for j in range(macro_Num) : 
                    if self.power == False or run_num == 0 : 
                        break

                    elif str(type(CSV_data_copy[startObject + 1][j + 2])) == "<class 'str'>" :          # 가공되지 않은 좌표 or 키보드 입력
                        # 좌표 가공
                        CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].strip('(')
                        CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].strip(')')
                        CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].split(', ')
                        
                        if str(type(CSV_data_copy[startObject+1][j+2])) == "<class 'list'>" :         # 가공된 좌표일 경우
                            pyautogui.moveTo(CSV_data_copy[startObject + 1][j + 2])
                            time.sleep(0.05)
                            pyautogui.click(CSV_data_copy[startObject + 1][j + 2])
                            time.sleep(delay)
                        else :      # 키보드 입력일 경우
                            pyautogui.press(CSV_data_copy[startObject + 1][j + 2])
                            time.sleep(delay)

                    else :      # 방금 막 저장한 마우스 매크로의 경우
                        pyautogui.moveTo(CSV_data_copy[startObject + 1][j + 2])
                        time.sleep(0.05)
                        pyautogui.click(CSV_data_copy[startObject + 1][j + 2])
                        time.sleep(delay)
                    
                run_num -= 1
                self.decreaseSignal_typeNum.emit(run_num)

            self.noticeMacroSignal_typeNum.emit()
            global detectPower
            detectPower = False

        else : 
            self.notLoadSignal.emit()



    def startMacro_typeTime(self) : 
        self.power = True
        if Load_status == True : 
            CSV_data_copy = copy.deepcopy(CSV_data)
            delay = float(CSV_data_copy[startObject + 1][1])
            macro_Num = len(CSV_data_copy[startObject + 1]) - 2
            while self.power == True : 
                for j in range(macro_Num) : 
                    if self.power == False : 
                        break

                    elif str(type(CSV_data_copy[startObject + 1][j + 2])) == "<class 'str'>" :          # 가공되지 않은 좌표 or 키보드 입력
                        # 좌표 가공
                        CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].strip('(')
                        CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].strip(')')
                        CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].split(', ')
                        
                        if str(type(CSV_data_copy[startObject+1][j+2])) == "<class 'list'>" :         # 가공된 좌표일 경우
                            pyautogui.moveTo(CSV_data_copy[startObject + 1][j + 2])
                            time.sleep(0.05)
                            pyautogui.click(CSV_data_copy[startObject + 1][j + 2])
                            time.sleep(delay)
                        else :      # 키보드 입력일 경우
                            pyautogui.press(CSV_data_copy[startObject + 1][j + 2])
                            time.sleep(delay)

                    else :      # 방금 막 저장한 마우스 매크로의 경우
                        pyautogui.moveTo(CSV_data_copy[startObject + 1][j + 2])
                        time.sleep(0.05)
                        pyautogui.click(CSV_data_copy[startObject + 1][j + 2])
                        time.sleep(delay)
            
            self.noticeMacroSignal_typeTime.emit()
            global detectPower
            detectPower = False
        
        else : 
            self.notLoadSignal.emit()



    def stop(self) : 
        self.power = False



class Task2(QObject) : 
    # For startMacro_typeTime
    decreaseSignal_typeTime = Signal(int)

    def timer(self) : 
        global run_time
        run_time = runTime
        while run_time > 0 : 
            time.sleep(1)
            run_time -= 1
            self.decreaseSignal_typeTime.emit(run_time)
        task1.stop()



class Task3(QObject) : 
    def detectKey(self) : 
        global detectPower
        detectPower = True
        while detectPower == True : 
            if keyboard.is_pressed("ESC") : 
                task1.stop()
                break



class KOM(QMainWindow) : 
    def __init__(self) :
        super().__init__()
        
        self.task1 = QThread()
        self.task1.start()
        global task1
        task1 = Task1()
        task1.moveToThread(self.task1)

        self.task2 = QThread()
        self.task2.start()
        global task2
        task2 = Task2()
        task2.moveToThread(self.task2)

        self.task3 = QThread()
        self.task3.start()
        global task3
        task3 = Task3()
        task3.moveToThread(self.task3)


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
        self.addClick_cb.setGeometry(20, 170, 101, 22)

        self.addClick_lb_1 = QLabel(self)
        self.addClick_lb_1.setGeometry(130, 170, 16, 20)
        self.addClick_lb_1.setText("에")

        self.addClick_lb_2 = QLabel(self)
        self.addClick_lb_2.setGeometry(210, 170, 71, 20)
        self.addClick_lb_2.setText("초 간격으로")

        self.addClick_ds = QDoubleSpinBox(self)
        self.addClick_ds.setGeometry(150, 170, 51, 22)
        
        self.addClick_bt = QPushButton(self)
        self.addClick_bt.setGeometry(280, 170, 51, 21)
        self.addClick_bt.setText("클릭")

        self.addClick_lb_3 = QLabel(self)
        self.addClick_lb_3.setGeometry(80, 200, 191, 20)
        self.addClick_lb_3.setText("(순서에 맞게 클릭을 진행하세요.)")

        
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
        self.addKeyboard_lb_3.setText("(순서에 맞게 입력을 진행하세요.)")

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

        self.start_sb_1 = QSpinBox(self)
        self.start_sb_1.setGeometry(210, 510, 42, 22)
        self.start_sb_1.setMaximum(999999999)

        self.start_sb_2 = QSpinBox(self)
        self.start_sb_2.setGeometry(180, 510, 42, 22)
        self.start_sb_2.setMaximum(999999999)
        self.start_sb_2.hide()

        self.start_lb_2 = QLabel(self)
        self.start_lb_2.setGeometry(260, 510, 16, 20)
        self.start_lb_2.setText("번")

        self.start_lb_3 = QLabel(self)
        self.start_lb_3.setGeometry(230, 510, 41, 20)
        self.start_lb_3.setText("초 동안")
        self.start_lb_3.hide()

        self.start_bt_1 = QPushButton(self)
        self.start_bt_1.setGeometry(280, 510, 51, 21)
        self.start_bt_1.setText("실행")

        self.start_bt_2 = QPushButton(self)
        self.start_bt_2.setGeometry(280, 510, 51, 21)
        self.start_bt_2.setText("실행")
        self.start_bt_2.hide()

        self.start_lb_type = QLabel(self)
        self.start_lb_type.setGeometry(110, 480, 211, 20)
        self.start_lb_type.setText("-   [ Type :                                 ]")

        self.start_rb_num = QRadioButton(self)
        self.start_rb_num.setGeometry(190, 480, 51, 16)
        self.start_rb_num.setText("횟수")
        self.start_rb_num.setChecked(True)

        self.start_rb_min = QRadioButton(self)
        self.start_rb_min.setGeometry(260, 480, 51, 16)
        self.start_rb_min.setText("시간")


        # If Signal is coming
        self.loadButton.clicked.connect(self.loadCSV)

        self.addName_bt.clicked.connect(self.addName)
        self.addName_le.returnPressed.connect(self.addName)

        self.addClick_bt.clicked.connect(self.SEMI_addClick)
        self.addClick_bt.clicked.connect(task1.addClick)

        self.addKeyboard_bt.clicked.connect(self.SEMI_addKeyboard)
        self.addKeyboard_bt.clicked.connect(task1.addKeyboard)

        self.delete_bt.clicked.connect(self.deleteMacro)

        self.start_bt_1.clicked.connect(self.SEMI_startMacro_typeNum)
        self.start_bt_1.clicked.connect(task1.startMacro_typeNum)
        self.start_bt_1.clicked.connect(task3.detectKey)

        self.start_bt_2.clicked.connect(self.SEMI_startMacro_typeTime)
        self.start_bt_2.clicked.connect(task1.startMacro_typeTime)
        self.start_bt_2.clicked.connect(task2.timer)
        self.start_bt_2.clicked.connect(task3.detectKey)

        task1.notLoadSignal.connect(self.notLoadMessage)

        task1.addDelaySignal_C1.connect(self.addDelay_C1)
        task1.addDelaySignal_C2.connect(self.addDelay_C2)
        task1.addDelaySignal_K1.connect(self.addDelay_K1)
        task1.addDelaySignal_K2.connect(self.addDelay_K2)

        self.start_rb_num.clicked.connect(self.typeNum)
        self.start_rb_min.clicked.connect(self.typeTime)

        task1.decreaseSignal_typeNum.connect(self.start_sb_1.setValue)
        task2.decreaseSignal_typeTime.connect(self.start_sb_2.setValue)

        task1.noticeClickSignal.connect(self.noticeClick)
        task1.noticeKeyboardSignal.connect(self.noticeKeyboard)
        task1.ESCis_pressedSignal.connect(self.noticeNotESC)
        task1.noticeMacroSignal_typeNum.connect(self.noticeMacro_typeNum)
        task1.noticeMacroSignal_typeTime.connect(self.noticeMacro_typeTime)
        

        # When program is started(DEFAULT)
        global Load_status
        Load_status = False

        self.noticeBoard.addItem("[system] 환영합니다. DATA.csv를 불러와주세요.")



    def loadCSV(self) : 
        global Load_status
        global CSV_road
        CSV_road = str(QFileDialog.getOpenFileName()[0])
        CSV_name = os.path.basename(CSV_road)
        
        if CSV_name == 'DATA.csv' : 
            self.noticeBoard.addItem('[system] DATA.csv를 불러오는데 성공했습니다.')
            
            # Read CSV
            global CSV_data
            CSV_file = open(CSV_road, 'r', encoding = 'utf-8', newline='')
            CSV_read = csv.reader(CSV_file)
            CSV_data = []

            # Data(DATA.csv) -> List(CSV_DATA)
            for row in CSV_read : 
                CSV_data.append(row)

            # Add macro's name in CSV to all of comboBox
            for i in range(1, len(CSV_data)) : 
                self.addClick_cb.addItem(CSV_data[i][0])
                self.addKeyboard_cb.addItem(CSV_data[i][0])
                self.delete_cb.addItem(CSV_data[i][0])
                self.start_cb.addItem(CSV_data[i][0])

            Load_status = True

        elif CSV_name != 'DATA.csv' : 
            self.noticeBoard.addItem('[system] DATA.csv를 불러오는데 실패했습니다.')



    def addName(self) : 
        if Load_status == True : 
            macroName = [self.addName_le.text()]
            self.addName_le.setText('')
            
            if macroName[0] == '' : 
                self.noticeBoard.addItem('[system] 공백을 이름으로 사용할 수 없습니다.')
            else : 
                # Add macro's name in List to all of comboBox
                self.addClick_cb.addItem(macroName[0])
                self.addKeyboard_cb.addItem(macroName[0])
                self.delete_cb.addItem(macroName[0])
                self.start_cb.addItem(macroName[0])

                CSV_data.append(macroName)

                CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)

                self.noticeBoard.addItem('[system] 매크로를 추가했습니다.')

        else : 
            self.noticeBoard.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')



    def SEMI_addClick(self) : 
        if Load_status == True : 
            global clickObject
            clickObject = self.addClick_cb.currentIndex()

            self.addClick_cb.setEnabled(False)
            self.addClick_lb_1.setEnabled(False)
            self.addClick_lb_2.setEnabled(False)
            self.addClick_ds.setEnabled(False)
            self.addClick_bt.setEnabled(False)



    def SEMI_addKeyboard(self) : 
        if Load_status == True : 
            global keyboardObject
            keyboardObject = self.addKeyboard_cb.currentIndex()

            self.addKeyboard_cb.setEnabled(False)
            self.addKeyboard_lb_1.setEnabled(False)
            self.addKeyboard_ds.setEnabled(False)
            self.addKeyboard_lb_2.setEnabled(False)
            self.addKeyboard_bt.setEnabled(False)



    def deleteMacro(self) : 
        if Load_status == True : 
            object = self.delete_cb.currentIndex()

            self.addClick_cb.removeItem(object)
            self.addKeyboard_cb.removeItem(object)
            self.start_cb.removeItem(object)
            self.delete_cb.removeItem(object)
            del CSV_data[object + 1]

            CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
            writer = csv.writer(CSV_file)
            writer.writerows(CSV_data)

            self.noticeBoard.addItem('[system] 매크로를 삭제했습니다.')
        else : 
            self.noticeBoard.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')



    def typeNum(self) : 
        self.start_cb.setGeometry(20, 510, 141, 22)
        self.start_lb_1.setGeometry(170, 510, 41, 20)
        self.start_sb_2.hide()
        self.start_sb_1.show()
        self.start_lb_3.hide()
        self.start_lb_2.show()
        self.start_bt_2.hide()
        self.start_bt_1.show()

    

    def typeTime(self) : 
        self.start_cb.setGeometry(20, 510, 111, 22)
        self.start_lb_1.setGeometry(140, 510, 41, 20)
        self.start_sb_1.hide()
        self.start_sb_2.show()
        self.start_lb_2.hide()
        self.start_lb_3.show()
        self.start_bt_1.hide()
        self.start_bt_2.show()



    def SEMI_startMacro_typeNum(self) : 
        if Load_status == True : 
            global startObject
            startObject = self.start_cb.currentIndex()

            global runNum
            runNum = self.start_sb_1.value()

            self.start_cb.setEnabled(False)
            self.start_lb_1.setEnabled(False)
            self.start_sb_1.setEnabled(False)
            self.start_lb_2.setEnabled(False)
            self.start_bt_1.setEnabled(False)



    
    def SEMI_startMacro_typeTime(self) : 
        if Load_status == True : 
            global startObject
            startObject = self.start_cb.currentIndex()

            global runTime
            runTime = self.start_sb_2.value()
            
            self.start_cb.setEnabled(False)
            self.start_lb_1.setEnabled(False)
            self.start_sb_2.setEnabled(False)
            self.start_lb_3.setEnabled(False)
            self.start_bt_2.setEnabled(False)



    # taskClass's Signal
    def notLoadMessage(self) : 
        self.noticeBoard.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')

    def addDelay_C1(self) : 
        CSV_data[clickObject + 1].append(self.addClick_ds.value())
    
    def addDelay_C2(self) : 
        CSV_data[clickObject + 1][1] = self.addClick_ds.value()
    
    def addDelay_K1(self) : 
        CSV_data[keyboardObject + 1].append(self.addKeyboard_ds.value())
    
    def addDelay_K2(self) : 
        CSV_data[keyboardObject + 1][1] = self.addKeyboard_ds.value()

    def noticeClick(self) : 
        self.addClick_cb.setEnabled(True)
        self.addClick_lb_1.setEnabled(True)
        self.addClick_lb_2.setEnabled(True)
        self.addClick_ds.setEnabled(True)
        self.addClick_bt.setEnabled(True)
        self.noticeBoard.addItem('[system] 클릭한 좌표가 저장되었습니다.')

    def noticeKeyboard(self) : 
        self.addKeyboard_cb.setEnabled(True)
        self.addKeyboard_lb_1.setEnabled(True)
        self.addKeyboard_ds.setEnabled(True)
        self.addKeyboard_lb_2.setEnabled(True)
        self.addKeyboard_bt.setEnabled(True)
        self.noticeBoard.addItem('[system] 키보드 입력이 설정되었습니다.')

    def noticeNotESC(self) : 
        self.noticeBoard.addItem('[system] ESC키는 매크로로 추가할 수 없습니다.')

    def noticeMacro_typeNum(self) : 
        self.start_cb.setEnabled(True)
        self.start_lb_1.setEnabled(True)
        self.start_sb_1.setEnabled(True)
        self.start_lb_2.setEnabled(True)
        self.start_bt_1.setEnabled(True)
        self.noticeBoard.addItem('[system] 매크로 작동이 완료되었습니다.')

    def noticeMacro_typeTime(self) : 
        self.start_cb.setEnabled(True)
        self.start_lb_1.setEnabled(True)
        self.start_sb_2.setEnabled(True)
        self.start_lb_3.setEnabled(True)
        self.start_bt_2.setEnabled(True)
        self.noticeBoard.addItem('[system] 매크로 작동이 완료되었습니다.')



if __name__ == '__main__' : 
    app = QApplication(sys.argv)
    kom = KOM()
    kom.show()
    sys.exit(app.exec_())