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

from KOM_mainUI import MainUI
from KOM_settingUI import SettingUI
from KOM_editUI import EditUI

class Main(QMainWindow) : 
    def __init__(self) : 
        super().__init__()
        
        global mainUI
        mainUI = MainUI()
        global settingUI
        settingUI = SettingUI()
        global editUI
        editUI = EditUI()
        global Load_status
        Load_status = False

        mainUI.show()
        
        # If Signal is coming
        mainUI.keep_bt.clicked.connect(mainUI.showMinimized)
        mainUI.exit_bt.clicked.connect(quit)

        mainUI.setting_bt.clicked.connect(Main.openSetting)
        settingUI.exit_bt.clicked.connect(settingUI.close)
        settingUI.load_bt.clicked.connect(Main.load)
        settingUI.stopKey_bt.clicked.connect(Main.setStopKey)

        mainUI.addName_bt.clicked.connect(Main.addName)
        mainUI.addName_le.returnPressed.connect(Main.addName)

        mainUI.edit_bt.clicked.connect(Main.openEdit)
        editUI.exit_bt.clicked.connect(editUI.close)

        mainUI.delete_bt.clicked.connect(Main.delete)
        
        mainUI.start_rb_typeNum.clicked.connect(mainUI.typeNum)
        mainUI.start_rb_typeTime.clicked.connect(mainUI.typeTime)

        # mainUI.start_bt.clicked.connect()                           # ing code / When tasking is over, delete this comment.


    # settingUI_group
    def openSetting(self) : 
        settingUI.exec_()
    
    def setStopKey(self) : 
        print("[system] stopKey_bt의 클릭이 감지되었습니다.")       # Test code / please delete this line.



    # editUI_group
    def openEdit(self) : 
        editUI.exec_()



    # mainUi_group
    def load(self) : 
        global Load_status
        global CSV_road
        CSV_road = str(QFileDialog.getOpenFileName()[0])
        CSV_name = os.path.basename(CSV_road)

        if CSV_name == "DATA.csv" : 
            mainUI.noticeBoard.addItem("[system] DATA.csv를 불러오는데 성공했습니다.")
            mainUI.noticeBoard.scrollToBottom()

            # Read CSV
            global CSV_data
            CSV_file = open(CSV_road, "r", encoding = "utf-8", newline = "")
            CSV_read = csv.reader(CSV_file)
            CSV_data = []

            # Data(DATA.csv) -> List(CSV_data)
            for row in CSV_read : 
                CSV_data.append(row)
            
            # Add macro's name in CSV to All of comboBox
            for i in range(1, len(CSV_data)) : 
                mainUI.delete_cb.addItem(CSV_data[i][0])
                mainUI.start_cb.addItem(CSV_data[i][0])
            
            Load_status = True
        
        else : 
            mainUI.noticeBoard.addItem("[system] DATA.csv를 불러오는데 실패했습니다.")
            mainUI.noticeBoard.scrollToBottom()
    


    def addName(self) : 
        if Load_status == True : 
            global macroName
            macroName = [mainUI.addName_le.text()]
            mainUI.addName_le.setText("")

            if macroName[0] == "" : 
                mainUI.noticeBoard.addItem("[system] 공백을 이름으로 사용할 수 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
            else : 
                # Add macro's name in List to All of comboBox
                mainUI.delete_cb.addItem(macroName[0])
                mainUI.start_cb.addItem(macroName[0])

                CSV_data.append(macroName)

                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)

                mainUI.noticeBoard.addItem("[system] 새로운 매크로를 추가했습니다.")
                mainUI.noticeBoard.scrollToBottom()
        
        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()
    


    def delete(self) : 
        if Load_status == True : 
            delObj = mainUI.delete_cb.currentIndex()

            mainUI.delete_cb.removeItem(delObj)
            mainUI.start_cb.removeItem(delObj)
            del CSV_data[delObj + 1]

            CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
            writer = csv.writer(CSV_file)
            writer.writerows(CSV_data)

            mainUI.noticeBoard.addItem("[system] 선택한 매크로를 삭제했습니다.")
            mainUI.noticeBoard.scrollToBottom()
        
        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()


    





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()
    sys.exit(app.exec_())