"""
<The_King_of_Macro_v2.1> - 22.?.??. (???) ??:??
* Made by Yoonmen *

[update]
1. 컬러체커 기능 추가 (In editUI)
2. settingUI에 '매크로 프로그램을 가장 위로' 선택 기능 추가
3. 마우스 클릭이 아닌 키보드 입력으로 마우스 좌표를 추가할 수 있도록 함 (좌클릭 = F9, 우클릭 = F10)
"""

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
import webbrowser

from KOM_mainUI import MainUI
from KOM_settingUI import SettingUI
from KOM_editUI import EditUI
from KOM_editUI import AddDelayUI
from KOM_editUI import AddColorCheckerUI

class Main() : 
    def __init__(self) : 
        super().__init__()
        
        global mainUI
        mainUI = MainUI()
        global settingUI
        settingUI = SettingUI()
        global editUI
        editUI = EditUI()
        global addDelayUI
        addDelayUI = AddDelayUI()
        global addColorCheckerUI
        addColorCheckerUI = AddColorCheckerUI()

        global thread_basicFn       # For quit
        thread_basicFn = QThread()
        thread_basicFn.start()
        global basicFn
        basicFn = BasicFn()
        basicFn.moveToThread(thread_basicFn)

        global thread_additionalFn_1      # For quit
        thread_additionalFn_1 = QThread()
        thread_additionalFn_1.start()
        global additionalFn_1
        additionalFn_1 = AdditionalFn_1()
        additionalFn_1.moveToThread(thread_additionalFn_1)

        global thread_additionalFn_2        # For quit
        thread_additionalFn_2 = QThread()
        thread_additionalFn_2.start()
        global additionalFn_2
        additionalFn_2 = AdditionalFn_2()
        additionalFn_2.moveToThread(thread_additionalFn_2)

        global Load_status
        Load_status = False

        global stopKey
        stopKey = "esc"

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())



    def signal(self) : 
        # << mainUI (1/5) >> --------------------

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

        mainUI.start_bt_typeNum.clicked.connect(basicFn.startMacro)
        mainUI.start_bt_typeNum.clicked.connect(additionalFn_1.stopKeyDetector)

        mainUI.start_bt_typeTime.clicked.connect(basicFn.startMacro)
        mainUI.start_bt_typeTime.clicked.connect(additionalFn_1.stopKeyDetector)
        mainUI.start_bt_typeTime.clicked.connect(additionalFn_2.timer)



        # << settingUI (2/5) >> --------------------

        ## title_part
        settingUI.exit_bt.clicked.connect(settingUI.close)


        ## load_part
        settingUI.load_bt.clicked.connect(BasicFn.load)


        ## stopKey_part
        settingUI.stopKey_bt.clicked.connect(BasicFn.setStopKey)


        ## winToTop_part
        settingUI.winToTop_ckb.stateChanged.connect(BasicFn.winToTop)


        ## icon_part
        settingUI.github_bt.clicked.connect(self.openGithub)


        # << editUI (3/5) >> --------------------

        ## functional_part
        editUI.setMacro_cb.currentIndexChanged.connect(basicFn.setMacro)
        editUI.editMacro_lw.itemClicked.connect(basicFn.checkNum)


        ## title_part
        editUI.exit_bt.clicked.connect(self.closeEdit)


        ## editMacro_part
        editUI.addClick_bt.clicked.connect(basicFn.addClick)
        editUI.addKeyboard_bt.clicked.connect(basicFn.addKeyboard)
        editUI.addDelay_bt.clicked.connect(self.openAddDelay)
        editUI.addColorChecker_bt.clicked.connect(self.openAddColorChecker)

        editUI.delete_bt.clicked.connect(basicFn.detailDelete)

        editUI.up_bt.clicked.connect(basicFn.up)
        editUI.down_bt.clicked.connect(basicFn.down)



        # << addDelayUI (4/5) >> --------------------

        ## title_part
        addDelayUI.exit_bt.clicked.connect(self.closeAddDelay)


        ## addDelay_part
        addDelayUI.add_bt.clicked.connect(basicFn.addDelay)
        addDelayUI.add_bt.clicked.connect(self.closeAddDelay)

        addDelayUI.cancel_bt.clicked.connect(self.closeAddDelay)



        # << addColorCheckerUI (5/5) >> --------------------

        ## title_part
        addColorCheckerUI.exit_bt.clicked.connect(self.closeAddColorChecker)


        ## coordinate_part
        addColorCheckerUI.addCoordinate_bt.clicked.connect(basicFn.addCoordinate)


        ## color_part
        addColorCheckerUI.addPalette_bt.clicked.connect(basicFn.addPalette)
        addColorCheckerUI.copyColor_bt.clicked.connect(basicFn.copyColor)


        ## addColorChecker_part
        addColorCheckerUI.add_bt.clicked.connect(basicFn.addColorChecker)



    def openSetting(self) : 
        settingUI.show()
    
    def openGithub(self) : 
        webbrowser.open("https://github.com/Yoon-men/The_King_of_Macro")


    def openEdit(self) : 
        global isEditUiOpened
        isEditUiOpened = True
        mainUI.edit_bt_active()
        editUI.show()
    
    def closeEdit(self) : 
        global isEditUiOpened
        isEditUiOpened = False
        mainUI.edit_bt_inactive()
        editUI.close()


    def openAddDelay(self) : 
        editUI.addDelay_bt_active()
        addDelayUI.exec_()
    
    def closeAddDelay(self) : 
        editUI.addDelay_bt_inactive()
        addDelayUI.close()


    def openAddColorChecker(self) : 
        editUI.addColorChecker_bt_active()
        addColorCheckerUI.exec_()     # Test code / please unlock this line and delete this comment
        # addColorCheckerUI.show()        # Test code / please delete this line.

    def closeAddColorChecker(self) : 
        editUI.addColorChecker_bt_inactive()
        addColorCheckerUI.close()



    def quit(self) : 
        thread_basicFn.quit()
        thread_additionalFn_1.quit()
        thread_additionalFn_2.quit()
        QCoreApplication.instance().quit()




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
            # CSV(DATA.csv) -> List(CSV_data)
            for row in CSV_read : 
                CSV_data.append(row)
            # Write DATA in List to comboBoxes
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



    def winToTop(self) : 
        if settingUI.winToTop_ckb.isChecked() : 
            mainUI.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            mainUI.show()
            settingUI.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            settingUI.show()
            editUI.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            if isEditUiOpened == True : 
                editUI.show()
            addDelayUI.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            addColorCheckerUI.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)


        else : 
            mainUI.setWindowFlags(Qt.FramelessWindowHint)
            mainUI.show()
            settingUI.setWindowFlags(Qt.FramelessWindowHint)
            settingUI.show()
            editUI.setWindowFlags(Qt.FramelessWindowHint)
            if isEditUiOpened == True : 
                editUI.show()
            addDelayUI.setWindowFlags(Qt.FramelessWindowHint)
            addColorCheckerUI.setWindowFlags(Qt.FramelessWindowHint)



    def addName(self) : 
        if Load_status == True : 
            global macroName
            # Write DATA to subList
            macroName = [mainUI.addName_le.text()]
            mainUI.addName_le.setText("")

            if macroName[0] == "" : 
                mainUI.noticeBoard.addItem("[system] 공백을 이름으로 사용할 수 없습니다.")
                mainUI.noticeBoard.scrollToBottom()

            else : 
                # Write DATA in subList to comboBoxes
                mainUI.delete_cb.addItem(macroName[0])
                mainUI.start_cb.addItem(macroName[0])
                editUI.setMacro_cb.addItem(macroName[0])
                # Write DATA in subList to List
                CSV_data.append(macroName)
                # Write DATA in List to CSV
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
                editUI.addClick_bt_active()
                addObj = editUI.setMacro_cb.currentIndex()
                while True : 
                    if keyboard.is_pressed("F9") : 
                        x, y = pyautogui.position()
                        # Write DATA to List
                        CSV_data[addObj + 1].append("<L>")
                        CSV_data[addObj + 1].append((x, y))
                        # Write DATA in List to CSV
                        CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                        writer = csv.writer(CSV_file)
                        writer.writerows(CSV_data)
                        # Notify click
                        mainUI.noticeBoard.addItem("[system] 클릭한 좌표가 저장되었습니다.")
                        mainUI.noticeBoard.scrollToBottom()
                        editUI.addClick_bt_inactive()
                        # Apply the update to editMacro_lw
                        self.setMacro()
                        break

                    if keyboard.is_pressed("F10") : 
                        x, y = pyautogui.position()
                        # Write DATA to List
                        CSV_data[addObj + 1].append("<R>")
                        CSV_data[addObj + 1].append((x, y))
                        # Write DATA in List to CSV
                        CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                        writer = csv.writer(CSV_file)
                        writer.writerows(CSV_data)
                        # Notify click
                        mainUI.noticeBoard.addItem("[system] 클릭한 좌표가 저장되었습니다.")
                        mainUI.noticeBoard.scrollToBottom()
                        editUI.addClick_bt_inactive()
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
                editUI.addKeyboard_bt_active()
                addObj = editUI.setMacro_cb.currentIndex()
                key = keyboard.read_hotkey(suppress = False)
                
                keyCheck = key.split("+")
                if len(keyCheck) > 3 : 
                    mainUI.noticeBoard.addItem("[system] 키보드 입력은 삼중 동시 입력까지 가능합니다.")
                    mainUI.noticeBoard.scrollToBottom()
                
                else : 
                    # Write DATA to List
                    CSV_data[addObj + 1].append("<K>")
                    CSV_data[addObj + 1].append(key)
                    # Write DATA in List to CSV
                    CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                    writer = csv.writer(CSV_file)
                    writer.writerows(CSV_data)
                    # Notify input
                    mainUI.noticeBoard.addItem("[system] 키보드 입력이 저장되었습니다.")
                    mainUI.noticeBoard.scrollToBottom()
                    # Apply the update to editMacro_lw
                    self.setMacro()
                
                editUI.addKeyboard_bt_inactive()


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
        

        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def addDelay(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                addObj = editUI.setMacro_cb.currentIndex()
                delay = addDelayUI.addDelay_ds.text()
                # Write DATA to List
                CSV_data[addObj + 1].append("<D>")
                CSV_data[addObj + 1].append(delay)
                # Write DATA in List to CSV
                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)
                # Notify input
                mainUI.noticeBoard.addItem("[system] 딜레이 추가가 완료되었습니다.")
                mainUI.noticeBoard.scrollToBottom()
                editUI.addDelay_bt_inactive()
                # Apply the update to editMacro_lw
                self.setMacro()


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    # addColorChckerUI

    ## << coordinate_part (1/3) >> --------------------
    def addCoordinate(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                print("입력 확인 메시지 출력")      # Test code / please delete this line.
                addColorCheckerUI.addCoordinate_bt_active()       # Test code / please unlock this line and delete this comment.
                while True : 
                    if keyboard.is_pressed("F9") : 
                        x, y = pyautogui.position()
                        addColorCheckerUI.X_le.setText(str(x))
                        addColorCheckerUI.Y_le.setText(str(y))
                        addColorCheckerUI.addCoordinate_bt_inactive()
                        print("중지 버튼 입력 확인 완료")       # Test code / please delete this line.
                        break


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()

        
        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()


    ##  << color_part (2/3) >> --------------------
    def addPalette(self) : 
        print("아이고난!")      # Test code / please delete this line.


    def copyColor(self) : 
        print("있다가")     # Test code / please delete this line.


    ## << addColorChecker_part (3/3) >> --------------------
    def addColorChecker(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                print("아이고난!")      # Test code / please delete this line.
            

            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
        

        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def detailDelete(self) : 
        if Load_status == True : 
            delObj = editUI.editMacro_lw.currentRow()
            if delObj != -1 : 
                mainObj = editUI.setMacro_cb.currentIndex()
                # Delete macro and macro's keyword
                del CSV_data[mainObj + 1][(delObj+1)*2 - 1 : (delObj+1)*2 + 1]
                # Write DATA to CSV
                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)
                # Apply the update to editMacro_lw
                self.setMacro()
            
            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def checkNum(self) : 
        mainObj = editUI.setMacro_cb.currentIndex()
        checkObj = editUI.editMacro_lw.currentRow()
        if checkObj == 0 : 
            editUI.up_bt.setEnabled(False)
            editUI.down_bt.setEnabled(True)

        elif checkObj == int((len(CSV_data[mainObj + 1])-3)/2) : 
            editUI.down_bt.setEnabled(False)
            editUI.up_bt.setEnabled(True)

        else : 
            editUI.up_bt.setEnabled(True)
            editUI.down_bt.setEnabled(True)



    def up(self) : 
        if Load_status == True : 
            moveObj = editUI.editMacro_lw.currentRow()
            mainObj = editUI.setMacro_cb.currentIndex()

            if moveObj == -1 : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()

            else : 
                # Type swap
                CSV_data[mainObj + 1][moveObj*2 + 1], CSV_data[mainObj + 1][moveObj*2 - 1] = CSV_data[mainObj + 1][moveObj*2 - 1], CSV_data[mainObj + 1][moveObj*2 + 1]
                # Skill swap
                CSV_data[mainObj + 1][moveObj*2 + 2], CSV_data[mainObj + 1][moveObj * 2] = CSV_data[mainObj + 1][moveObj * 2], CSV_data[mainObj + 1][moveObj*2 + 2]
                # Write DATA to CSV
                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)
                # Apply the update to editMacro_lw
                self.setMacro()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()

    

    def down(self) : 
        if Load_status == True : 
            mainObj = editUI.setMacro_cb.currentIndex()
            moveObj = editUI.editMacro_lw.currentRow()
            
            if moveObj == -1 : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()

            else : 
                # Type swap
                CSV_data[mainObj + 1][(moveObj+1)*2 - 1], CSV_data[mainObj + 1][(moveObj+1)*2 + 1] = CSV_data[mainObj + 1][(moveObj+1)*2 + 1], CSV_data[mainObj + 1][(moveObj+1)*2 - 1]
                # Skill swap
                CSV_data[mainObj + 1][(moveObj+1) * 2], CSV_data[mainObj + 1][(moveObj+2) * 2] = CSV_data[mainObj + 1][(moveObj+2) * 2], CSV_data[mainObj + 1][(moveObj+1) * 2]
                # Write DATA in List to CSV
                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)
                # Apply the update to editMacro_lw
                self.setMacro()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def delete(self) : 
        if Load_status == True : 
            if len(CSV_data) != 1 : 
                delObj = mainUI.delete_cb.currentIndex()
                # Remove DATA in ComboBoxes
                mainUI.delete_cb.removeItem(delObj)
                mainUI.start_cb.removeItem(delObj)
                editUI.setMacro_cb.removeItem(delObj)
                # Delete DATA in List
                del CSV_data[delObj + 1]
                # Write DATA in List to CSV
                CSV_file = open(CSV_road, "w", encoding = "utf-8", newline = "")
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)

                mainUI.noticeBoard.addItem("[system] 선택한 매크로를 삭제했습니다.")
                mainUI.noticeBoard.scrollToBottom()


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def startMacro(self) : 
        if Load_status == True : 
            from KOM_mainUI import startType

            global power
            power = True
            
            if len(CSV_data) != 1 : 
                if startType == "typeNum" : 
                    mainUI.start_bt_typeNum_active()
                elif startType == "typeTime" : 
                    mainUI.start_bt_typeTime_active()

                startObj = mainUI.start_cb.currentIndex()
                global runTime
                runTime = int(mainUI.start_le.text())

                CSV_data_copy = copy.deepcopy(CSV_data)
                macroNum = int((len(CSV_data_copy[startObj + 1])-1) / 2)

                while power == True and runTime != 0 : 
                    for i in range(macroNum) : 
                        if power == False : 
                            break

                        # << Left Click (1/4) >> --------------------
                        if CSV_data_copy[startObj + 1][(i+1)*2 - 1] == "<L>" : 
                            ## Detect unprocess coordinate
                            unprocessDetector = "(" in CSV_data_copy[startObj + 1][(i+1) * 2]

                            if unprocessDetector == True : 
                                ## Process coordinate
                                CSV_data_copy[startObj + 1][(i+1) * 2] = CSV_data_copy[startObj + 1][(i+1) * 2].strip("(")
                                CSV_data_copy[startObj + 1][(i+1) * 2] = CSV_data_copy[startObj + 1][(i+1) * 2].strip(")")
                                CSV_data_copy[startObj + 1][(i+1) * 2] = CSV_data_copy[startObj + 1][(i+1) * 2].split(", ")
                            
                            pyautogui.moveTo(CSV_data_copy[startObj + 1][(i+1) * 2])
                            time.sleep(0.05)
                            pyautogui.click(CSV_data_copy[startObj + 1][(i+1) * 2])
                        

                        # << Right Click (2/4) >> --------------------
                        elif CSV_data_copy[startObj + 1][(i+1)*2 - 1] == "<R>" : 
                            ## Detect unprocess coordinate
                            unprocessDetector = "(" in CSV_data_copy[startObj + 1][(i+1) * 2]

                            if unprocessDetector == True : 
                                ## Process coordinate
                                CSV_data_copy[startObj + 1][(i+1) * 2] = CSV_data_copy[startObj + 1][(i+1) * 2].strip("(")
                                CSV_data_copy[startObj + 1][(i+1) * 2] = CSV_data_copy[startObj + 1][(i+1) * 2].strip(")")
                            
                            pyautogui.moveTo(CSV_data_copy[startObj + 1][(i+1) * 2])
                            time.sleep(0.05)
                            pyautogui.rightClick(CSV_data_copy[startObj + 1][(i+1) * 2])

                        
                        # << Keyboard input (3/4) >> --------------------
                        elif CSV_data_copy[startObj + 1][(i+1)*2 - 1] == "<K>" : 
                            key = CSV_data_copy[startObj + 1][(i+1) * 2].split("+")
                            if len(key) == 1 : 
                                pyautogui.hotkey(key[0])
                            
                            elif len(key) == 2 : 
                                pyautogui.hotkey(key[0], key[1])
                            
                            elif len(key) == 3 : 
                                pyautogui.hotkey(key[0], key[1], key[2])


                        # << Delay (4/4) >> --------------------
                        elif CSV_data_copy[startObj + 1][(i+1)*2 - 1] == "<D>" : 
                            time.sleep(float(CSV_data_copy[startObj + 1][(i+1) * 2]))


                    if startType == "typeNum" : 
                        runTime -= 1
                        mainUI.start_le.setText(str(runTime))

                mainUI.noticeBoard.addItem("[system] 매크로 작업이 완료되었습니다.")
                mainUI.noticeBoard.scrollToBottom()

                power = False

                if startType == "typeNum" : 
                    mainUI.start_bt_typeNum_inactive()
                elif startType == "typeTime" : 
                    mainUI.start_bt_typeTime_inactive()


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
        

        else : 
            mainUI.noticeBoard.addItem("[system] 아직 DATA.csv를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()


            

# Additional functions for Macro working.
class AdditionalFn_1(QObject) : 
    def stopKeyDetector(self) : 
        global power

        while power == True : 
            if keyboard.is_pressed(stopKey) : 
                power = False
                break




class AdditionalFn_2(QObject) : 
    def timer(self) : 
        global runTime
        global power

        while runTime > 0 and power == True : 
            time.sleep(1)
            runTime -= 1
            mainUI.start_le.setText(str(runTime))

        power = False





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()