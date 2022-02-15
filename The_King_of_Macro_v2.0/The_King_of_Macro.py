import sys
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

class Main() : 
    def __init__(self) : 
        super().__init__()
        
        global mainUI
        mainUI = MainUI()
        global settingUI
        settingUI = SettingUI()
        global editUI
        editUI = EditUI()

        global thread_basicFn       # For quit
        thread_basicFn = QThread()
        thread_basicFn.start()
        global basicFn
        basicFn = BasicFn()
        basicFn.moveToThread(thread_basicFn)

        global thread_additionalFn      # For quit
        thread_additionalFn = QThread()
        thread_additionalFn.start()
        global additionalFn
        additionalFn = AdditionalFn()
        additionalFn.moveToThread(thread_additionalFn)

        global Load_status
        Load_status = False

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())



    def signal(self) : 
        # << mainUI (1/3) >> --------------------

        ## title_part
        mainUI.keep_bt.clicked.connect(mainUI.showMinimized)
        mainUI.exit_bt.clicked.connect(self.quit)
        mainUI.setting_bt.clicked.connect(self.openSetting)

        ## addName_part
        mainUI.addName_bt.clicked.connect(basicFn.addName)
        mainUI.addName_le.returnPressed.connect(basicFn.addName)

        ## edit_part
        mainUI.edit_bt.clicked.connect(self.openEdit)
        
        ## delete_part
        mainUI.delete_bt.clicked.connect(BasicFn.delete)
        
        ## start_part
        mainUI.start_rb_typeNum.clicked.connect(mainUI.typeNum)
        mainUI.start_rb_typeTime.clicked.connect(mainUI.typeTime)
        mainUI.start_bt.clicked.connect(basicFn.startMacro)


        # << settingUI (2/3) >> --------------------

        ## title_part
        settingUI.exit_bt.clicked.connect(settingUI.close)

        ## load_part
        settingUI.load_bt.clicked.connect(BasicFn.load)

        ## stopKey_part
        settingUI.stopKey_bt.clicked.connect(BasicFn.setStopKey)


        # << editUI (3/3) >> --------------------

        ## functional_part
        editUI.setMacro_cb.currentIndexChanged.connect(basicFn.setMacro)

        ## title_part
        editUI.exit_bt.clicked.connect(editUI.close)

        ## editMacro_part
        editUI.addClick_bt.clicked.connect(basicFn.addClick)
        editUI.addKeyboard_bt.clicked.connect(basicFn.addKeyboard)
        # editUI.addDelay_bt.clicked.connect()
        # editUI.delete_bt.clicked.connect()
        # editUI.up_bt.clicked.connect()
        # editUI.down_bt.clicked.connect()



    def openSetting(self) : 
        settingUI.exec_()

    def openEdit(self) : 
        editUI.exec_()



    def quit(self) : 
        thread_basicFn.quit()
        thread_additionalFn.quit()
        quit()




# Basic functions for Macro working
class BasicFn(QObject) : 
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
                editUI.setMacro_cb.addItem(CSV_data[i][0])
            
            Load_status = True


        else : 
            mainUI.noticeBoard.addItem("[system] DATA.csv를 불러오는데 실패했습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def setStopKey(self) : 
        global stopKey
        stopKey = keyboard.read_hotkey(suppress = False)
        settingUI.stopKey_bt.setText(stopKey)
    


    def addName(self) : 
        if Load_status == True : 
            global macroName
            macroName = [mainUI.addName_le.text()]
            mainUI.addName_le.setText("")

            if macroName[0] == "" : 
                mainUI.noticeBoard.addItem("[system] 공백을 이름으로 사용할 수 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
            else : 
                # Add macro's name in List to ComboBoxes.
                mainUI.delete_cb.addItem(macroName[0])
                mainUI.start_cb.addItem(macroName[0])
                editUI.setMacro_cb.addItem(macroName[0])
                # Add macro's name to DATA
                CSV_data.append(macroName)
                # Write DATA to CSV
                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)

                mainUI.noticeBoard.addItem("[system] 새로운 매크로를 추가했습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def setMacro(self) : 
        editUI.editMacro_lw.clear()
        setObj = editUI.setMacro_cb.currentIndex()
        for i in range(int((len(CSV_data[setObj + 1]) - 1) / 2)) : 
            if CSV_data[setObj + 1][(i+1)*2 - 1] == "<L>" : 
                editUI.editMacro_lw.addItem(f"마우스 {CSV_data[setObj + 1][(i+1) * 2]} 좌클릭")
            
            elif CSV_data[setObj + 1][(i+1)*2 - 1] == "<R>" : 
                editUI.editMacro_lw.addItem(f"마우스 {CSV_data[setObj + 1][(i+1) * 2]} 우클릭")

            elif CSV_data[setObj + 1][(i+1)*2 - 1] == "<K>" : 
                editUI.editMacro_lw.addItem(f"키보드 < {CSV_data[setObj + 1][(i+1) * 2]} > 입력")

            elif CSV_data[setObj + 1][(i+1)*2 - 1] == "<D>" : 
                editUI.editMacro_lw.addItem(f"딜레이 < {CSV_data[setObj + 1][(i+1) * 2]} 초 >")



    def addClick(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                addObj = editUI.setMacro_cb.currentIndex()
                while True : 
                    if mouse.is_pressed("left") : 
                        x, y = pyautogui.position()
                        CSV_data[addObj + 1].append("<L>")
                        CSV_data[addObj + 1].append((x, y))
                        # Write DATA to CSV
                        CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                        writer = csv.writer(CSV_file)
                        writer.writerows(CSV_data)
                        # Notify click
                        mainUI.noticeBoard.addItem("[system] 클릭한 좌표가 저장되었습니다.")
                        mainUI.noticeBoard.scrollToBottom()
                        # Apply the update to editMacro_lw
                        self.setMacro()
                        break

                    if mouse.is_pressed("right") : 
                        x, y = pyautogui.position()
                        CSV_data[addObj + 1].append("<R>")
                        CSV_data[addObj + 1].append((x, y))
                        # Write DATA to CSV
                        CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                        writer = csv.writer(CSV_file)
                        writer.writerows(CSV_data)
                        # Notify click
                        mainUI.noticeBoard.addItem("[system] 클릭한 좌표가 저장되었습니다.")
                        mainUI.noticeBoard.scrollToBottom()
                        # Apply the update to editMacro_lw
                        self.setMacro()
                        break
            
            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
        

        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def addKeyboard(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                addObj = editUI.setMacro_cb.currentIndex()
                key = keyboard.read_hotkey(suppress = False)
                CSV_data[addObj + 1].append("<K>")
                CSV_data[addObj + 1].append(key)
                # Write DATA to CSV
                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)
                # Notify input
                mainUI.noticeBoard.addItem("[system] 키보드 입력이 저장되었습니다.")
                mainUI.noticeBoard.scrollToBottom()
                # Apply the update to editMacro_lw
                self.setMacro()
            
            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
        

        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def delete(self) : 
        if Load_status == True : 
            delObj = mainUI.delete_cb.currentIndex()
            # Remove macro in ComboBox
            mainUI.delete_cb.removeItem(delObj)
            mainUI.start_cb.removeItem(delObj)
            editUI.setMacro_cb.removeItem(delObj)
            # Delete macro in DATA
            del CSV_data[delObj + 1]
            # Write DATA to CSV
            CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
            writer = csv.writer(CSV_file)
            writer.writerows(CSV_data)

            mainUI.noticeBoard.addItem("[system] 선택한 매크로를 삭제했습니다.")
            mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def startMacro(self) : 
        if Load_status == True : 
            from KOM_mainUI import startType
            
            if startType == "typeNum" : 
                print("Igonan!")        # Test code / please delete this line.
            
            elif startType == "typeTime" : 
                print("Nanun! Jangpungul hatDA!")       # Test code / please delete this line.
        
        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



# Additional functions for Macro working.
class AdditionalFn(QObject) : 
    def timer(self) : 
        print("아이고난!")      # Test code / please delete this line.




if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()