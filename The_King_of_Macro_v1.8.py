"""
<The_King_of_Macro_v1.8> - 22.2.??. (???) ??:??
* Made by Yoonmen *

[update]
1. 매크로 편집 기능('마우스 클릭, 키보드 입력' 통합 기능) 추가
2. 설정 창에서 ESC키를 눌러도 나가지지 않도록 변경
"""

import sys
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

    # 선택한 매크로가 없는 상태
    notSelectSignal = Signal()

    # 매크로가 몇 번 더 동작해야 하는지를 카운트
    # (For startMacro_typeNum)
    decreaseSignal_typeNum = Signal(int)

    # 사용자 요청 작업이 완료된 상태
    noticeClickSignal = Signal()
    noticeKeyboardSignal = Signal()
    noticeMacroSignal_typeNum = Signal()
    noticeMacroSignal_typeTime = Signal()

    def addClick(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                while True : 
                    if mouse.is_pressed("left") : 
                        x, y = pyautogui.position()
                        CSV_data[obj + 1].append("<L>")
                        CSV_data[obj + 1].append((x, y))

                        CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                        writer = csv.writer(CSV_file)
                        writer.writerows(CSV_data)

                        self.noticeClickSignal.emit()
                        break

                    if mouse.is_pressed("right") : 
                        x, y = pyautogui.position()
                        CSV_data[obj + 1].append("<R>")
                        CSV_data[obj + 1].append((x, y))

                        CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                        writer = csv.writer(CSV_file)
                        writer.writerows(CSV_data)

                        self.noticeClickSignal.emit()
                        break
            else : 
                self.notSelectSignal.emit()
        else : 
            self.notLoadSignal.emit()



    def addKeyboard(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                key = keyboard.read_hotkey(suppress = False)

                CSV_data[obj + 1].append("<K>")
                CSV_data[obj + 1].append(key)

                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)

                self.noticeKeyboardSignal.emit()
            else : 
                self.notSelectSignal.emit()

        else : 
            self.notLoadSignal.emit()



    def startMacro_typeNum(self) : 
        self.power = True

        if Load_status == True : 
            if len(CSV_data) != 1 : 
                run_num = runNum
                CSV_data_copy = copy.deepcopy(CSV_data)
                delay = float(CSV_data_copy[startObject + 1][1])
                macro_Num = len(CSV_data_copy[startObject + 1]) - 2
                while self.power == True and run_num != 0 : 
                    for j in range(macro_Num) : 
                        if self.power == False or run_num == 0 : 
                            break
                        
                        # 가공되지 않은 좌표 or 키보드 입력
                        elif str(type(CSV_data_copy[startObject + 1][j + 2])) == "<class 'str'>" : 
                            
                            # 가공되지 않은 좌표 감지
                            mouseDetector = "(" in CSV_data_copy[startObject + 1][j + 2]
                            if mouseDetector == True : 
                                # 좌표 가공
                                CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].strip('(')
                                CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].strip(')')
                                CSV_data_copy[startObject+1][j+2] = CSV_data_copy[startObject+1][j+2].split(', ')
                            
                            if str(type(CSV_data_copy[startObject+1][j+2])) == "<class 'list'>" :           # 가공된 좌표일 경우
                                pyautogui.moveTo(CSV_data_copy[startObject + 1][j + 2])
                                time.sleep(0.05)
                                pyautogui.click(CSV_data_copy[startObject + 1][j + 2])
                                time.sleep(delay)

                            else :      # 키보드 입력일 경우
                                # 동시 입력 감지
                                simultaneityDetector = "+" in CSV_data_copy[startObject + 1][j + 2]

                                # 동시 입력이 감지되면 키보딩 가공
                                if simultaneityDetector == True  :
                                    CSV_data_copy[startObject + 1][j + 2] = CSV_data_copy[startObject + 1][j + 2].split("+")

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
                self.notSelectSignal.emit()

        else : 
            self.notLoadSignal.emit()



    def startMacro_typeTime(self) : 
        self.power = True

        if Load_status == True : 
            if len(CSV_data) != 1 : 
                CSV_data_copy = copy.deepcopy(CSV_data)
                delay = float(CSV_data_copy[startObject + 1][1])
                macro_Num = len(CSV_data_copy[startObject + 1]) - 2
                while self.power == True : 
                    for j in range(macro_Num) : 
                        if self.power == False : 
                            break

                        elif str(type(CSV_data_copy[startObject + 1][j + 2])) == "<class 'str'>" :          # 가공되지 않은 좌표 or 키보드 입력
                            # 가공되지 않은 좌표 감지
                            mouseDetector = "(" in CSV_data_copy[startObject + 1][j + 2]
                            if mouseDetector == True : 
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
                                # 동시 입력 감지
                                simultaneityDetector = "+" in CSV_data_copy[startObject + 1][j + 2]
                                # 동시 입력이 감지되면 키보딩 가공
                                if simultaneityDetector == True  :
                                    CSV_data_copy[startObject + 1][j + 2] = CSV_data_copy[startObject + 1][j + 2].split("+")

                                pyautogui.press(CSV_data_copy[startObject + 1][j + 2])
                                time.sleep(delay)

                        else :      # 방금 막 저장한 마우스 매크로의 경우
                            pyautogui.moveTo(CSV_data_copy[startObject + 1][j + 2])
                            time.sleep(0.05)
                            pyautogui.click(CSV_data_copy[startObject + 1][j + 2])
                            time.sleep(delay)
                
                self.noticeMacroSignal_typeTime.emit()

                global timerPower
                timerPower = False

                global detectPower
                detectPower = False
            else : 
                self.notSelectSignal.emit()
        
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

        global timerPower
        timerPower = True
        while run_time > 0 and timerPower == True : 
            time.sleep(1)
            run_time -= 1
            self.decreaseSignal_typeTime.emit(run_time)
        task1.stop()




class Task3(QObject) : 
    def detectKey(self) : 
        global detectPower
        detectPower = True
        while detectPower == True : 
            if keyboard.is_pressed(stopKey) : 
                task1.stop()
                break




class Setting(QDialog) : 
    def __init__(self) : 
        super().__init__()

        self.settingUI()



    def settingUI(self) : 
        # Default Setting
        self.setFixedSize(255, 172)
        self.setWindowTitle("설정")

        self.title = QLabel(self)
        self.title.setGeometry(80, 0, 101, 41)
        font = QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setText("Setting")
        

        # stopKey_group
        self.stopKey_lb = QLabel(self)
        self.stopKey_lb.setGeometry(10, 70, 101, 20)
        self.stopKey_lb.setText("- 매크로 중단 키 : ")

        self.stopKey_lw = QListWidget(self)
        self.stopKey_lw.setGeometry(120, 70, 61, 21)
        item = QListWidgetItem(stopKey)
        item.setTextAlignment(Qt.AlignCenter)
        self.stopKey_lw.addItem(item)

        self.stopKey_bt = QPushButton(self)
        self.stopKey_bt.setGeometry(190, 70, 51, 21)
        self.stopKey_bt.setText("입력")
        

        # If Signal is coming
        self.stopKey_bt.clicked.connect(self.SEMI_setKey)
        self.stopKey_bt.clicked.connect(task4.setKey)

        task4.noticeSetKeySignal.connect(self.noticeSetKey)



    def SEMI_setKey(self) : 
        self.stopKey_bt.setEnabled(False)

    def noticeSetKey(self) : 
        self.stopKey_lw.clear()
        item = QListWidgetItem(stopKey)
        item.setTextAlignment(Qt.AlignCenter)
        self.stopKey_lw.addItem(item)

        self.stopKey_bt.setEnabled(True)



    def keyPressEvent(self, e) : 
        if e.key() == Qt.Key_Escape : 
            pass




class Task4(QObject) : 
    # 사용자 요청 작업이 완료된 상태
    noticeSetKeySignal = Signal()

    def setKey(self) : 
        global stopKey
        stopKey = keyboard.read_hotkey(suppress = False)
        
        self.noticeSetKeySignal.emit()




class Edit(QDialog) : 
    def __init__(self) : 
        super().__init__()
        
        self.editUI()



    def editUI(self) : 
        # Default Setting
        self.setFixedSize(381, 472)
        self.setWindowTitle("매크로 편집")

        self.title = QLabel(self)
        self.title.setGeometry(160, 10, 61, 41)
        font = QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setText("Edit")


        # setMacro_group
        self.setMacro_lb = QLabel(self)
        self.setMacro_lb.setGeometry(40, 60, 91, 20)
        self.setMacro_lb.setText("편집할 매크로 : ")

        self.setMacro_cb = QComboBox(self)
        self.setMacro_cb.setGeometry(130, 60, 211, 22)
        if Load_status == True : 
            for i in range(1, len(CSV_data)) : 
                self.setMacro_cb.addItem(CSV_data[i][0])


        # editMacro_group
        self.editMacro_lw = QListWidget(self)
        self.editMacro_lw.setGeometry(10, 110, 271, 341)
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                self.setMacro()

        self.editMacro_bt_addClick = QPushButton(self)
        self.editMacro_bt_addClick.setGeometry(290, 110, 81, 21)
        self.editMacro_bt_addClick.setText("클릭 추가")

        self.editMacro_bt_addKeyboard = QPushButton(self)
        self.editMacro_bt_addKeyboard.setGeometry(290, 150, 81, 21)
        self.editMacro_bt_addKeyboard.setText("키보드 추가")

        self.editMacro_bt_addDelay = QPushButton(self)
        self.editMacro_bt_addDelay.setGeometry(290, 190, 81, 21)
        self.editMacro_bt_addDelay.setText("딜레이 추가")

        self.editMacro_line_1 = QFrame(self)
        self.editMacro_line_1.setGeometry(300, 230, 61, 20)
        self.editMacro_line_1.setFrameShape(QFrame.HLine)
        self.editMacro_line_1.setFrameShadow(QFrame.Sunken)

        self.editMacro_bt_delete = QPushButton(self)
        self.editMacro_bt_delete.setGeometry(290, 270, 81, 21)
        self.editMacro_bt_delete.setText("삭제")

        self.editMacro_line_2 = QFrame(self)
        self.editMacro_line_2.setGeometry(300, 310, 61, 20)
        self.editMacro_line_2.setFrameShape(QFrame.HLine)
        self.editMacro_line_2.setFrameShadow(QFrame.Sunken)

        self.editMacro_bt_UP = QPushButton(self)
        self.editMacro_bt_UP.setGeometry(310, 350, 41, 21)
        self.editMacro_bt_UP.setText("▲")

        self.editMacro_bt_DOWN = QPushButton(self)
        self.editMacro_bt_DOWN.setGeometry(310, 380, 41, 21)
        self.editMacro_bt_DOWN.setText("▼")


        # If Signal is coming
        task1.notSelectSignal.connect(self.notSelect)
        self.setMacro_cb.currentIndexChanged.connect(self.setMacro)

        self.editMacro_bt_addClick.clicked.connect(self.SEMI_addClick)
        self.editMacro_bt_addClick.clicked.connect(task1.addClick)
        task1.noticeClickSignal.connect(self.noticeClick)

        self.editMacro_bt_addKeyboard.clicked.connect(self.SEMI_addKeyboard)
        self.editMacro_bt_addKeyboard.clicked.connect(task1.addKeyboard)
        task1.noticeKeyboardSignal.connect(self.noticeKeyboard)

        self.editMacro_bt_addDelay.clicked.connect(self.addDelay)

        # self.editMacro_bt_delete.clicked.connect(self.delete)

        # self.editMacro_bt_UP.clicked.connect(self.UP)
        # self.editMacro_bt_DOWN.clicked.connect(self.DOWN)



    def notSelect(self) : 
        self.editMacro_bt_addClick.setEnabled(True)
        self.editMacro_bt_addKeyboard.setEnabled(True)



    def setMacro(self) : 
        self.editMacro_lw.clear()
        obj = self.setMacro_cb.currentIndex()
        for i in range(int((len(CSV_data[obj + 1]) - 1) / 2)) : 
            if CSV_data[obj + 1][(i+1)*2 - 1] == "<L>" : 
                self.editMacro_lw.addItem(f"마우스 {CSV_data[obj + 1][(i+1) * 2]} 좌클릭")
            
            elif CSV_data[obj + 1][(i+1)*2 - 1] == "<R>" : 
                self.editMacro_lw.addItem(f"마우스 {CSV_data[obj + 1][(i+1) * 2]} 우클릭")

            elif CSV_data[obj + 1][(i+1)*2 - 1] == "<K>" : 
                self.editMacro_lw.addItem(f"키보드 < {CSV_data[obj + 1][(i+1) * 2]} > 입력")

            elif CSV_data[obj + 1][(i+1)*2 - 1] == "<D>" : 
                self.editMacro_lw.addItem(f"딜레이 < {CSV_data[obj + 1][(i+1) * 2]} 초 >")



    def SEMI_addClick(self) : 
        if Load_status == True : 
            global obj
            obj = self.setMacro_cb.currentIndex()
            self.editMacro_bt_addClick.setEnabled(False)

    def noticeClick(self) : 
        self.editMacro_bt_addClick.setEnabled(True)
        self.setMacro()



    def SEMI_addKeyboard(self) : 
        if Load_status == True : 
            global obj
            obj = self.setMacro_cb.currentIndex()
            self.editMacro_bt_addKeyboard.setEnabled(False)

    def noticeKeyboard(self) : 
        self.editMacro_bt_addKeyboard.setEnabled(True)
        self.setMacro()


    
    def addDelay(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                obj = self.setMacro_cb.currentIndex()
                self.editMacro_bt_addDelay.setEnabled(False)

                delay, add = QInputDialog.getDouble(self, '딜레이 추가', '딜레이 : ')
                if add : 
                    CSV_data[obj + 1].append("<D>")
                    CSV_data[obj + 1].append(delay)

                    CSV_file = open(CSV_road, "w", encoding = "utf-8", newline="")
                    writer = csv.writer(CSV_file)
                    writer.writerows(CSV_data)

                    self.editMacro_bt_addDelay.setEnabled(True)
                    self.setMacro()
                else : 
                    self.editMacro_bt_addDelay.setEnabled(True)
            else : 
                task1.notSelectSignal.emit()
        
        else : 
            task1.notLoadSignal.emit()



    def keyPressEvent(self, e) : 
        if e.key() == Qt.Key_Escape : 
            pass




class Main(QMainWindow) : 
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

        self.task4 = QThread()
        self.task4.start()
        global task4
        task4 = Task4()
        task4.moveToThread(self.task4)
        

        self.mainUI()



    def mainUI(self) : 
        # basic_group
        self.setFixedSize(351, 603)
        self.setWindowTitle("The_King_of_Macro_v1.8")

        self.title = QLabel(self)
        self.title.setGeometry(60, 20, 231, 71)
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
        self.version.setText("v1.8")

        self.load_bt = QToolButton(self)
        self.load_bt.setGeometry(280, 10, 61, 20)
        self.load_bt.setText("불러오기")

        self.setting_bt = QToolButton(self)
        self.setting_bt.setGeometry(210, 10, 61, 20)
        self.setting_bt.setText("설정")

        self.noticeBoard = QListWidget(self)
        self.noticeBoard.setGeometry(20, 490, 311, 81)

        self.dev = QLabel(self)
        self.dev.setGeometry(130, 580, 101, 16)
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.dev.setFont(font)
        self.dev.setText("by. Yoonmen")


        # addName_group
        self.addName_group = QLabel(self)
        self.addName_group.setGeometry(20, 80, 131, 20)
        self.addName_group.setText("<Add Macro's Name>")

        self.addName_le = QLineEdit(self)
        self.addName_le.setGeometry(20, 110, 251, 20)
        self.addName_le.setPlaceholderText("ex) 자동사냥")
        self.addName_le.setClearButtonEnabled(True)

        self.addName_bt = QPushButton(self)
        self.addName_bt.setGeometry(280, 110, 51, 21)
        self.addName_bt.setText("추가")

        self.line_1 = QFrame(self)
        self.line_1.setGeometry(110, 160, 118, 3)
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)


        # edit_group
        self.edit_lb_1 = QLabel(self)
        self.edit_lb_1.setGeometry(20, 180, 101, 20)
        self.edit_lb_1.setText("<Edit Macro>")

        self.edit_bt = QPushButton(self)
        self.edit_bt.setGeometry(20, 210, 311, 21)
        self.edit_bt.setText("편집")

        self.line_2 = QFrame(self)
        self.line_2.setGeometry(110, 270, 118, 3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)


        # delete_group
        self.delete_group = QLabel(self)
        self.delete_group.setGeometry(20, 290, 101, 20)
        self.delete_group.setText("<Delete Macro>")

        self.delete_cb = QComboBox(self)
        self.delete_cb.setGeometry(20, 320, 211, 22)

        self.delete_lb_1 = QLabel(self)
        self.delete_lb_1.setGeometry(240, 320, 41, 20)
        self.delete_lb_1.setText("을(를)")

        self.delete_bt = QPushButton(self)
        self.delete_bt.setGeometry(280, 320, 51, 21)
        self.delete_bt.setText("삭제")

        self.line_3 = QFrame(self)
        self.line_3.setGeometry(110, 380, 118, 3)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)


        # start_group
        self.start_group = QLabel(self)
        self.start_group.setGeometry(20, 410, 101, 20)
        self.start_group.setText("<Start Macro>")

        self.start_cb = QComboBox(self)
        self.start_cb.setGeometry(20, 440, 141, 22)

        self.start_lb_1 = QLabel(self)
        self.start_lb_1.setGeometry(170, 440, 41, 20)
        self.start_lb_1.setText("을(를)")

        self.start_sb_1 = QSpinBox(self)
        self.start_sb_1.setGeometry(210, 440, 42, 22)
        self.start_sb_1.setMaximum(999999999)

        self.start_sb_2 = QSpinBox(self)
        self.start_sb_2.setGeometry(180, 440, 42, 22)
        self.start_sb_2.setMaximum(999999999)
        self.start_sb_2.hide()

        self.start_lb_2 = QLabel(self)
        self.start_lb_2.setGeometry(260, 440, 16, 20)
        self.start_lb_2.setText("번")

        self.start_lb_3 = QLabel(self)
        self.start_lb_3.setGeometry(230, 440, 41, 20)
        self.start_lb_3.setText("초 동안")
        self.start_lb_3.hide()

        self.start_bt_1 = QPushButton(self)
        self.start_bt_1.setGeometry(280, 440, 51, 21)
        self.start_bt_1.setText("실행")

        self.start_bt_2 = QPushButton(self)
        self.start_bt_2.setGeometry(280, 440, 51, 21)
        self.start_bt_2.setText("실행")
        self.start_bt_2.hide()

        self.start_lb_type = QLabel(self)
        self.start_lb_type.setGeometry(110, 410, 211, 20)
        self.start_lb_type.setText("-   [ Type :                                 ]")

        self.start_rb_num = QRadioButton(self)
        self.start_rb_num.setGeometry(190, 410, 51, 16)
        self.start_rb_num.setText("횟수")
        self.start_rb_num.setChecked(True)

        self.start_rb_min = QRadioButton(self)
        self.start_rb_min.setGeometry(260, 410, 51, 16)
        self.start_rb_min.setText("시간")


        # When program is started (DEFAULT)
        global Load_status
        Load_status = False

        global stopKey
        stopKey = "esc"

        self.noticeBoard.addItem("[system] 환영합니다. DATA.csv를 불러와주세요.")


        # If Signal is coming
        self.load_bt.clicked.connect(self.loadCSV)

        self.setting_bt.clicked.connect(self.openSetting)

        self.addName_bt.clicked.connect(self.addName)
        self.addName_le.returnPressed.connect(self.addName)

        self.edit_bt.clicked.connect(self.openEdit)

        self.delete_bt.clicked.connect(self.deleteMacro)

        self.start_bt_1.clicked.connect(self.SEMI_startMacro_typeNum)
        self.start_bt_1.clicked.connect(task1.startMacro_typeNum)
        self.start_bt_1.clicked.connect(task3.detectKey)

        self.start_bt_2.clicked.connect(self.SEMI_startMacro_typeTime)
        self.start_bt_2.clicked.connect(task1.startMacro_typeTime)
        self.start_bt_2.clicked.connect(task2.timer)
        self.start_bt_2.clicked.connect(task3.detectKey)

        task1.notLoadSignal.connect(self.notLoadMessage)
        task1.notSelectSignal.connect(self.notSelectMessage)

        self.start_rb_num.clicked.connect(self.typeNum)
        self.start_rb_min.clicked.connect(self.typeTime)

        task1.decreaseSignal_typeNum.connect(self.start_sb_1.setValue)
        task2.decreaseSignal_typeTime.connect(self.start_sb_2.setValue)

        task1.noticeClickSignal.connect(self.noticeClick)
        task1.noticeKeyboardSignal.connect(self.noticeKeyboard)
        task1.noticeMacroSignal_typeNum.connect(self.noticeMacro_typeNum)
        task1.noticeMacroSignal_typeTime.connect(self.noticeMacro_typeTime)



    def loadCSV(self) : 
        global Load_status
        global CSV_road
        CSV_road = str(QFileDialog.getOpenFileName()[0])
        CSV_name = os.path.basename(CSV_road)
        
        if CSV_name == "DATA.csv" : 
            self.noticeBoard.addItem("[system] DATA.csv를 불러오는데 성공했습니다.")
            self.noticeBoard.scrollToBottom()
            
            # Read CSV
            global CSV_data
            CSV_file = open(CSV_road, "r", encoding = "utf-8", newline = "")
            CSV_read = csv.reader(CSV_file)
            CSV_data = []

            # Data(DATA.csv) -> List(CSV_DATA)
            for row in CSV_read : 
                CSV_data.append(row)

            # Add macro's name in CSV to all of comboBox
            for i in range(1, len(CSV_data)) : 
                self.delete_cb.addItem(CSV_data[i][0])
                self.start_cb.addItem(CSV_data[i][0])

            Load_status = True

        elif CSV_name != "DATA.csv" : 
            self.noticeBoard.addItem("[system] DATA.csv를 불러오는데 실패했습니다.")
            self.noticeBoard.scrollToBottom()



    def openSetting(self) : 
        global setting
        setting = Setting()
        setting.exec_()



    def openEdit(self) : 
        global edit
        edit = Edit()
        edit.exec_()



    def addName(self) : 
        if Load_status == True : 
            global macroName
            macroName = [self.addName_le.text()]
            self.addName_le.setText("")
            
            if macroName[0] == "" : 
                self.noticeBoard.addItem("[system] 공백을 이름으로 사용할 수 없습니다.")
                self.noticeBoard.scrollToBottom()
            else : 
                # Add macro's name in List to all of comboBox
                self.delete_cb.addItem(macroName[0])
                self.start_cb.addItem(macroName[0])

                CSV_data.append(macroName)

                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)

                self.noticeBoard.addItem("[system] 매크로를 추가했습니다.")
                self.noticeBoard.scrollToBottom()

        else : 
            self.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            self.noticeBoard.scrollToBottom()



    def deleteMacro(self) : 
        if Load_status == True : 
            deleteObj = self.delete_cb.currentIndex()

            self.start_cb.removeItem(deleteObj)
            self.delete_cb.removeItem(deleteObj)
            del CSV_data[deleteObj + 1]

            CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
            writer = csv.writer(CSV_file)
            writer.writerows(CSV_data)

            self.noticeBoard.addItem("[system] 매크로를 삭제했습니다.")
            self.noticeBoard.scrollToBottom()
        else : 
            self.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            self.noticeBoard.scrollToBottom()



    def typeNum(self) : 
        self.start_cb.setGeometry(20, 440, 141, 22)
        self.start_lb_1.setGeometry(170, 440, 41, 20)
        self.start_sb_2.hide()
        self.start_sb_1.show()
        self.start_lb_3.hide()
        self.start_lb_2.show()
        self.start_bt_2.hide()
        self.start_bt_1.show()

    

    def typeTime(self) : 
        self.start_cb.setGeometry(20, 440, 111, 22)
        self.start_lb_1.setGeometry(140, 440, 41, 20)
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
        self.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
        self.noticeBoard.scrollToBottom()

    def notSelectMessage(self) : 
        self.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
        self.noticeBoard.scrollToBottom()

    def noticeClick(self) : 
        self.noticeBoard.addItem("[system] 클릭한 좌표가 저장되었습니다.")
        self.noticeBoard.scrollToBottom()

    def noticeKeyboard(self) : 
        self.noticeBoard.addItem("[system] 키보드 입력이 설정되었습니다.")
        self.noticeBoard.scrollToBottom()

    def noticeMacro_typeNum(self) : 
        self.start_cb.setEnabled(True)
        self.start_lb_1.setEnabled(True)
        self.start_sb_1.setEnabled(True)
        self.start_lb_2.setEnabled(True)
        self.start_bt_1.setEnabled(True)
        self.noticeBoard.addItem("[system] 매크로 작동이 완료되었습니다.")
        self.noticeBoard.scrollToBottom()

    def noticeMacro_typeTime(self) : 
        self.start_cb.setEnabled(True)
        self.start_lb_1.setEnabled(True)
        self.start_sb_2.setEnabled(True)
        self.start_lb_3.setEnabled(True)
        self.start_bt_2.setEnabled(True)
        self.noticeBoard.addItem("[system] 매크로 작동이 완료되었습니다.")
        self.noticeBoard.scrollToBottom()



if __name__ == '__main__' : 
    app = QApplication(sys.argv)
    global main
    main = Main()
    main.show()
    sys.exit(app.exec_())