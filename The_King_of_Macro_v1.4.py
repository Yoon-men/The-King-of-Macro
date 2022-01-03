"""
<The_King_of_Macro_v1.4> - 22.1.3.월 17:18
* Made by Yoonmen *

[update]
1. 설정 가능한 매크로 동작 횟수 변경 (99 → 99999999)
2. 매크로 이름 추가 시 입력해놓은 내용을 삭제하는 기능 추가
3. 매크로 이름을 추가할 때 Enter키를 눌러서도 매크로를 추가할 수 있도록 변경
"""

import sys
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import os
import csv
import keyboard
import mouse
import pyautogui
import time


class KOM(QWidget) : 
    def setupUi(self, Form) : 
        # Default Setting
        _translate = QCoreApplication.translate

        Form.setFixedSize(351, 664)
        Form.setWindowTitle(_translate("Form", "The_King_of_Macro_v1.3"))

        self.title = QLabel(Form)
        self.title.setGeometry(60, 10, 241, 71)
        font = QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setText(_translate("Form", "The King of Macro"))

        self.version = QLabel(Form)
        self.version.setGeometry(10, 10, 64, 15)
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.version.setFont(font)
        self.version.setText(_translate("Form", "v1.4"))

        self.loadButton = QToolButton(Form)
        self.loadButton.setGeometry(280, 10, 61, 20)
        self.loadButton.setText(_translate("Form", "불러오기"))

        self.noticeBoard = QListWidget(Form)
        self.noticeBoard.setGeometry(20, 550, 311, 81)

        self.dev = QLabel(Form)
        self.dev.setGeometry(130, 640, 101, 16)
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.dev.setFont(font)
        self.dev.setText(_translate("Form", "by. Yoonmen"))


        # addName_group
        self.addName_group = QLabel(Form)
        self.addName_group.setGeometry(20, 70, 131, 20)
        self.addName_group.setText(_translate("Form", "<Add Macro's Name>"))

        self.addName_le = QLineEdit(Form)
        self.addName_le.setGeometry(20, 100, 251, 20)
        self.addName_le.setPlaceholderText("ex) 자동사냥")
        self.addName_le.setClearButtonEnabled(True)

        self.addName_bt = QPushButton(Form)
        self.addName_bt.setGeometry(280, 100, 51, 21)
        self.addName_bt.setText(_translate("Form", "추가"))


        # addClick_group
        self.addClick_group = QLabel(Form)
        self.addClick_group.setGeometry(20, 140, 101, 20)
        self.addClick_group.setText(_translate("Form", "<Add Click>"))

        self.addClick_cb = QComboBox(Form)
        self.addClick_cb.setGeometry(20, 170, 101, 22)

        self.addClick_lb_1 = QLabel(Form)
        self.addClick_lb_1.setGeometry(130, 170, 16, 20)
        self.addClick_lb_1.setText(_translate("Form", "에"))

        self.addClick_lb_2 = QLabel(Form)
        self.addClick_lb_2.setGeometry(210, 170, 71, 20)
        self.addClick_lb_2.setText(_translate("Form", "초 간격으로"))

        self.addClick_ds = QDoubleSpinBox(Form)
        self.addClick_ds.setGeometry(150, 170, 51, 22)
        
        self.addClick_bt = QPushButton(Form)
        self.addClick_bt.setGeometry(280, 170, 51, 21)
        self.addClick_bt.setText(_translate("Form", "클릭"))

        self.addClick_lb_3 = QLabel(Form)
        self.addClick_lb_3.setGeometry(80, 200, 191, 20)
        self.addClick_lb_3.setText(_translate("Form", "(순서에 맞게 클릭을 진행하세요.)"))

        
        # addKeyboard_group
        self.addKeyboard_group = QLabel(Form)
        self.addKeyboard_group.setGeometry(20, 240, 101, 20)
        self.addKeyboard_group.setText(_translate("Form", "<Add Keyboard>"))

        self.addKeyboard_cb = QComboBox(Form)
        self.addKeyboard_cb.setGeometry(20, 270, 101, 22)

        self.addKeyboard_lb_1 = QLabel(Form)
        self.addKeyboard_lb_1.setGeometry(130, 270, 16, 20)
        self.addKeyboard_lb_1.setText(_translate("Form", "에"))

        self.addKeyboard_ds = QDoubleSpinBox(Form)
        self.addKeyboard_ds.setGeometry(150, 270, 51, 22)

        self.addKeyboard_lb_2 = QLabel(Form)
        self.addKeyboard_lb_2.setGeometry(210, 270, 71, 20)
        self.addKeyboard_lb_2.setText(_translate("Form", "초 간격으로"))

        self.addKeyboard_bt = QPushButton(Form)
        self.addKeyboard_bt.setGeometry(280, 270, 51, 21)
        self.addKeyboard_bt.setText(_translate("Form", "입력"))

        self.addKeyboard_lb_3 = QLabel(Form)
        self.addKeyboard_lb_3.setGeometry(80, 300, 191, 20)
        self.addKeyboard_lb_3.setText(_translate("Form", "(순서에 맞게 클릭을 진행하세요.)"))

        self.addLine = QFrame(Form)
        self.addLine.setGeometry(110, 350, 118, 3)
        self.addLine.setFrameShape(QFrame.HLine)
        self.addLine.setFrameShadow(QFrame.Sunken)
        

        # delete_group
        self.delete_group = QLabel(Form)
        self.delete_group.setGeometry(20, 370, 101, 20)
        self.delete_group.setText(_translate("Form", "<Delete Macro>"))

        self.delete_cb = QComboBox(Form)
        self.delete_cb.setGeometry(20, 400, 211, 22)

        self.delete_lb_1 = QLabel(Form)
        self.delete_lb_1.setGeometry(240, 400, 41, 20)
        self.delete_lb_1.setText(_translate("Form", "을(를)"))

        self.delete_bt = QPushButton(Form)
        self.delete_bt.setGeometry(280, 400, 51, 21)
        self.delete_bt.setText(_translate("Form", "삭제"))

        self.deleteLine = QFrame(Form)
        self.deleteLine.setGeometry(110, 460, 118, 3)
        self.deleteLine.setFrameShape(QFrame.HLine)
        self.deleteLine.setFrameShadow(QFrame.Sunken)


        # start_group
        self.start_group = QLabel(Form)
        self.start_group.setGeometry(20, 480, 101, 20)
        self.start_group.setText(_translate("Form", "<Start Macro>"))

        self.start_cb = QComboBox(Form)
        self.start_cb.setGeometry(20, 510, 141, 22)

        self.start_lb_1 = QLabel(Form)
        self.start_lb_1.setGeometry(170, 510, 41, 20)
        self.start_lb_1.setText(_translate("Form", "을(를)"))

        self.start_sb = QSpinBox(Form)
        self.start_sb.setGeometry(210, 510, 42, 22)
        self.start_sb.setMaximum(99999999)

        self.start_lb_2 = QLabel(Form)
        self.start_lb_2.setGeometry(260, 510, 16, 20)
        self.start_lb_2.setText(_translate("Form", "번"))

        self.start_bt = QPushButton(Form)
        self.start_bt.setGeometry(280, 510, 51, 21)
        self.start_bt.setText(_translate("Form", "실행"))

        QMetaObject.connectSlotsByName(Form)


        # If Button is clicked
        self.loadButton.clicked.connect(self.Load_CSV)
        self.addName_bt.clicked.connect(self.Add_NAME)
        self.addName_le.returnPressed.connect(self.Add_NAME)
        self.addClick_bt.clicked.connect(self.Add_CLICK)
        self.addKeyboard_bt.clicked.connect(self.Add_KEYBOARD)
        self.delete_bt.clicked.connect(self.Delete_MACRO)
        self.start_bt.clicked.connect(self.Start_MACRO)



        # When program is started
        global Load_status
        Load_status = False
        self.noticeBoard.addItem("[system] 환영합니다. DATA.csv를 불러와주세요.")
    


    def Load_CSV(self) : 
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



    def Add_NAME(self) : 
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



    def Add_CLICK(self) : 
        if Load_status == True : 
            object = self.addClick_cb.currentIndex()

            if len(CSV_data[object + 1]) == 1 : 
                CSV_data[object + 1].append(self.addClick_ds.value())

            else : 
                CSV_data[object + 1][1] = self.addClick_ds.value()

            while True : 
                if mouse.is_pressed('left') : 
                    x, y = pyautogui.position()
                    CSV_data[object + 1].append((x, y))

                    CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
                    writer = csv.writer(CSV_file)
                    writer.writerows(CSV_data)

                    self.noticeBoard.addItem('[system] 클릭 좌표가 설정되었습니다.')
                    break

                elif keyboard.is_pressed('ESC') : 
                    self.noticeBoard.addItem('[system] 클릭 추가가 중지되었습니다.')
                    break
        else : 
            self.noticeBoard.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')



    def Add_KEYBOARD(self) : 
        if Load_status == True : 
            object = self.addKeyboard_cb.currentIndex()

            if len(CSV_data[object + 1]) == 1 : 
                CSV_data[object + 1].append(self.addKeyboard_ds.value())

            else : 
                CSV_data[object + 1][1] = self.addKeyboard_ds.value()
            
            key = keyboard.read_hotkey(suppress=False)
            CSV_data[object + 1].append(key)

            CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
            writer = csv.writer(CSV_file)
            writer.writerows(CSV_data)

            self.noticeBoard.addItem('[system] 키보드 입력이 설정되었습니다.')

        else : 
            self.noticeBoard.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')



    def Delete_MACRO(self) : 
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



    def Start_MACRO(self) : 
        if Load_status == True :
            object = self.start_cb.currentIndex()
            delay = float(CSV_data[object + 1][1])
            macro_Num = len(CSV_data[object + 1]) - 2
            for i in range(self.start_sb.value()) : 
                for j in range(macro_Num) : 
                    if str(type(CSV_data[object + 1][j + 2])) == "<class 'str'>" :          # 가공되지 않은 좌표 or 키보드 입력

                        # 좌표 가공
                        CSV_data[object+1][j+2] = CSV_data[object+1][j+2].strip('(')
                        CSV_data[object+1][j+2] = CSV_data[object+1][j+2].strip(')')
                        CSV_data[object+1][j+2] = CSV_data[object+1][j+2].split(', ')

                        if str(type(CSV_data[object+1][j+2])) == "<class 'list'>" :         # 가공된 좌표일 경우
                            pyautogui.moveTo(CSV_data[object + 1][j + 2])
                            time.sleep(0.05)
                            pyautogui.click(CSV_data[object + 1][j + 2])
                            time.sleep(delay)
                        else :      # 키보드 입력일 경우
                            pyautogui.press(CSV_data[object + 1][j + 2])
                            time.sleep(delay)

                    else :      # 방금 막 저장한 매크로의 경우
                        pyautogui.moveTo(CSV_data[object + 1][j + 2])
                        time.sleep(0.05)
                        pyautogui.click(CSV_data[object + 1][j + 2])
                        time.sleep(delay)
            self.noticeBoard.addItem('[system] 매크로 작동이 완료되었습니다.')

        else : 
            self.noticeBoard.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')



if __name__ == '__main__' : 
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = KOM()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())