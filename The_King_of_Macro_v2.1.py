"""
<The_King_of_Macro_v2.1> - 22.?.??. (???) ??:??
* Made by Yoonmen *

[update]
1. 컬러체커 기능 추가 (In editUI)
2. '매크로 프로그램을 가장 위로' 선택 기능 추가 (In settingUI)
3. 마우스 클릭 대신 키보드 입력으로 마우스 좌표를 추가하도록 변경 (좌클릭 = F9, 우클릭 = F10)
4. 매크로 데이터 저장 방식 변경
"""

import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import pickle
import keyboard
import pyautogui
import time
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

        global isEditUiOpened
        isEditUiOpened = False

        global palettePhase
        palettePhase = 1

        global palette
        palette = [(255, 0, 255)]

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
        addColorCheckerUI.setCoordinate_bt.clicked.connect(BasicFn.setCoordinate)


        ## color_part
        addColorCheckerUI.addPalette_bt.clicked.connect(BasicFn.addPalette)

        addColorCheckerUI.palette_rb_1.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_2.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_3.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_4.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_5.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_6.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_7.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_8.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_9.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_10.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_11.clicked.connect(BasicFn.setRGB)
        addColorCheckerUI.palette_rb_12.clicked.connect(BasicFn.setRGB)

        addColorCheckerUI.R_le.textChanged.connect(BasicFn.setColor)
        addColorCheckerUI.G_le.textChanged.connect(BasicFn.setColor)
        addColorCheckerUI.B_le.textChanged.connect(BasicFn.setColor)

        addColorCheckerUI.copyColor_bt.clicked.connect(BasicFn.copyColor)


        ## addColorChecker_part
        addColorCheckerUI.add_bt.clicked.connect(BasicFn.addColorChecker)
        addColorCheckerUI.add_bt.clicked.connect(self.closeAddColorChecker)



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
        addColorCheckerUI.exec_()

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
        global FILE_road
        FILE_road = str(QFileDialog.getOpenFileName()[0])
        FILE_name = os.path.basename(FILE_road)

        if FILE_name == "DATA.p" : 
            mainUI.noticeBoard.addItem("[system] 매크로 데이터를 불러오는데 성공했습니다.")
            mainUI.noticeBoard.scrollToBottom()
            # Read the file
            with open(FILE_road, "rb") as file : 
                global macroDATA
                macroDATA = list(pickle.load(file))
            # Add names of macros to comboBoxes
            for i in range(0, len(macroDATA)) : 
                mainUI.delete_cb.addItem(macroDATA[i][0])
                mainUI.start_cb.addItem(macroDATA[i][0])
                editUI.setMacro_cb.addItem(macroDATA[i][0])

            global Load_status
            Load_status = True


        else : 
            mainUI.noticeBoard.addItem("[system] 매크로 데이터를 불러오는데 실패했습니다.")
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
            macroName = [mainUI.addName_le.text()]
            mainUI.addName_le.setText("")

            if macroName[0] == "" : 
                mainUI.noticeBoard.addItem("[system] 공백을 이름으로 사용할 수 없습니다.")
                mainUI.noticeBoard.scrollToBottom()

            else : 
                # Add name of macro to comboBoxes
                mainUI.delete_cb.addItem(macroName[0])
                mainUI.start_cb.addItem(macroName[0])
                editUI.setMacro_cb.addItem(macroName[0])

                macroDATA.append(macroName)

                # Save the data of macro to file
                with open(FILE_road, "wb") as file : 
                    pickle.dump(macroDATA, file)

                mainUI.noticeBoard.addItem("[system] 새로운 매크로를 추가했습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def setMacro(self) : 
        editUI.editMacro_lw.clear()
        setObj = editUI.setMacro_cb.currentIndex()
        for i in range(int((len(macroDATA[setObj]) - 1) / 2)) : 
            if macroDATA[setObj][(i+1)*2 - 1] == "<L>" : 
                editUI.editMacro_lw.addItem(f"마우스 {macroDATA[setObj][(i+1) * 2]} 좌클릭")
            
            elif macroDATA[setObj][(i+1)*2 - 1] == "<R>" : 
                editUI.editMacro_lw.addItem(f"마우스 {macroDATA[setObj][(i+1) * 2]} 우클릭")

            elif macroDATA[setObj][(i+1)*2 - 1] == "<K>" : 
                editUI.editMacro_lw.addItem(f"키보드 < {macroDATA[setObj][(i+1) * 2]} > 입력")

            elif macroDATA[setObj][(i+1)*2 - 1] == "<D>" : 
                editUI.editMacro_lw.addItem(f"딜레이 < {macroDATA[setObj][(i+1) * 2]} 초 >")

            elif macroDATA[setObj][(i+1)*2 - 1] == "<C>" : 
                print(f"좌표 : {macroDATA[setObj][(i+1) * 2][0]} / 딜레이 : {macroDATA[setObj][(i+1) * 2][1]}")           # Test code / please delete the contents of this line.
                editUI.editMacro_lw.addItem(f"컬러체커 {macroDATA[setObj][(i+1) * 2][0]}에서 {macroDATA[setObj][(i+1) * 2][1]}초마다 실행")



    def addClick(self) : 
        if Load_status == True : 
            if len(macroDATA) != 0 : 
                editUI.addClick_bt_active()
                addObj = editUI.setMacro_cb.currentIndex()
                while True : 
                    if keyboard.is_pressed("F9") : 
                        x, y = pyautogui.position()
                        # Add the data of macro to list
                        macroDATA[addObj].append("<L>")
                        macroDATA[addObj].append((x, y))
                        # Save the data of macro to file
                        with open(FILE_road, "wb") as file : 
                            pickle.dump(macroDATA, file)
                        # Notify addClick event
                        mainUI.noticeBoard.addItem("[system] 클릭 좌표가 저장되었습니다.")
                        mainUI.noticeBoard.scrollToBottom()
                        editUI.addClick_bt_inactive()
                        # Apply the update to editMacro_lw
                        self.setMacro()
                        break

                    if keyboard.is_pressed("F10") : 
                        x, y = pyautogui.position()
                        # Add the data of macro to list
                        macroDATA[addObj].append("<R>")
                        macroDATA[addObj].append((x, y))
                        # Save the data of macro to file
                        with open(FILE_road, "wb") as file : 
                            pickle.dump(macroDATA, file)
                        # Notify addClick event
                        mainUI.noticeBoard.addItem("[system] 클릭 좌표가 저장되었습니다.")
                        mainUI.noticeBoard.scrollToBottom()
                        editUI.addClick_bt_inactive()
                        # Apply the update to editMacro_lw
                        self.setMacro()
                        break


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
        

        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def addKeyboard(self) : 
        if Load_status == True : 
            if len(macroDATA) != 0 : 
                editUI.addKeyboard_bt_active()
                addObj = editUI.setMacro_cb.currentIndex()
                key = keyboard.read_hotkey(suppress = False)
                
                keyCheck = key.split("+")
                if len(keyCheck) > 3 : 
                    mainUI.noticeBoard.addItem("[system] 키보드 입력은 삼중 동시 입력까지 지원합니다.")
                    mainUI.noticeBoard.scrollToBottom()
                else : 
                    # Add the data of macro to list
                    macroDATA[addObj].append("<K>")
                    macroDATA[addObj].append(key)
                    # Save the data of macro to file
                    with open(FILE_road, "wb") as file : 
                        pickle.dump(macroDATA, file)
                    # Notify addKeyboard event
                    mainUI.noticeBoard.addItem("[system] 키보드 입력이 저장되었습니다.")
                    mainUI.noticeBoard.scrollToBottom()
                    # Apply the update to editMacro_lw
                    self.setMacro()
                
                editUI.addKeyboard_bt_inactive()


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()
        

        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def addDelay(self) : 
        if Load_status == True : 
            if len(macroDATA) != 0 : 
                addObj = editUI.setMacro_cb.currentIndex()
                delay = addDelayUI.addDelay_ds.text()
                # Add the data of macro to list
                macroDATA[addObj].append("<D>")
                macroDATA[addObj].append(delay)
                # Save the data of macro to file
                with open(FILE_road, "wb") as file : 
                    pickle.dump(macroDATA, file)
                # Notify addDelay event
                mainUI.noticeBoard.addItem("[system] 딜레이 추가가 완료되었습니다.")
                mainUI.noticeBoard.scrollToBottom()
                editUI.addDelay_bt_inactive()
                # Apply the update to editMacro_lw
                self.setMacro()


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    # addColorChckerUI

    ## << coordinate_part (1/3) >> --------------------
    def setCoordinate(self) : 
        addColorCheckerUI.setCoordinate_bt_active()
        while True : 
            if keyboard.is_pressed("F9") or keyboard.is_pressed("F10") : 
                x, y = pyautogui.position()
                addColorCheckerUI.X_le.setText(str(x))
                addColorCheckerUI.Y_le.setText(str(y))
                addColorCheckerUI.setCoordinate_bt_inactive()
                break


    ##  << color_part (2/3) >> --------------------
    def addPalette(self) : 
        global palettePhase
        global palette
        
        if palettePhase == 11 : 
                addColorCheckerUI.addPalette_bt.hide()
                addColorCheckerUI.palette_rb_12.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 10 : 
                addColorCheckerUI.addPalette_bt.setGeometry(251, 284, 21, 21)
                addColorCheckerUI.palette_rb_11.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 9 : 
                addColorCheckerUI.addPalette_bt.setGeometry(192, 284, 21, 21)
                addColorCheckerUI.palette_rb_10.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 8 : 
                addColorCheckerUI.addPalette_bt.setGeometry(133, 284, 21, 21)
                addColorCheckerUI.palette_rb_9.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 7 : 
                addColorCheckerUI.addPalette_bt.setGeometry(74, 284, 21, 21)
                addColorCheckerUI.palette_rb_8.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 6 : 
                addColorCheckerUI.addPalette_bt.setGeometry(251, 250, 21, 21)
                addColorCheckerUI.palette_rb_7.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 5 : 
                addColorCheckerUI.addPalette_bt.setGeometry(192, 250, 21, 21)
                addColorCheckerUI.palette_rb_6.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 4 : 
                addColorCheckerUI.addPalette_bt.setGeometry(133, 250, 21, 21)
                addColorCheckerUI.palette_rb_5.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 3 : 
                addColorCheckerUI.addPalette_bt.setGeometry(74, 250, 21, 21)
                addColorCheckerUI.palette_rb_4.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 2 : 
                addColorCheckerUI.addPalette_bt.setGeometry(251, 216, 21, 21)
                addColorCheckerUI.palette_rb_3.show()
                palette.append((255, 0, 255))
                palettePhase += 1

        if palettePhase == 1 : 
                addColorCheckerUI.addPalette_bt.setGeometry(192, 216, 21, 21)
                addColorCheckerUI.palette_rb_2.show()
                palette.append((255, 0, 255))
                palettePhase += 1



    def setRGB(self) : 
        def displayRGB(RGB) : 
            addColorCheckerUI.R_le.setText(str(RGB[0]))
            addColorCheckerUI.G_le.setText(str(RGB[1]))
            addColorCheckerUI.B_le.setText(str(RGB[2]))

        if addColorCheckerUI.palette_rb_1.isChecked() : 
            displayRGB(palette[0])

        if addColorCheckerUI.palette_rb_2.isChecked() : 
            displayRGB(palette[1])
        
        if addColorCheckerUI.palette_rb_3.isChecked() : 
            displayRGB(palette[2])

        if addColorCheckerUI.palette_rb_4.isChecked() : 
            displayRGB(palette[3])
        
        if addColorCheckerUI.palette_rb_5.isChecked() : 
            displayRGB(palette[4])
        
        if addColorCheckerUI.palette_rb_6.isChecked() : 
            displayRGB(palette[5])
        
        if addColorCheckerUI.palette_rb_7.isChecked() : 
            displayRGB(palette[6])
        
        if addColorCheckerUI.palette_rb_8.isChecked() : 
            displayRGB(palette[7])

        if addColorCheckerUI.palette_rb_9.isChecked() : 
            displayRGB(palette[8])
        
        if addColorCheckerUI.palette_rb_10.isChecked() : 
            displayRGB(palette[9])

        if addColorCheckerUI.palette_rb_11.isChecked() : 
            displayRGB(palette[10])

        if addColorCheckerUI.palette_rb_12.isChecked() : 
            displayRGB(palette[11])



    def setColor(self) : 
        if addColorCheckerUI.R_le.text() == "" : 
            addColorCheckerUI.R_le.setText("0")
            addColorCheckerUI.R_le.selectAll()
        if int(addColorCheckerUI.R_le.text()) > 255 : 
            addColorCheckerUI.R_le.setText("255")
        
        if addColorCheckerUI.G_le.text() == "" : 
            addColorCheckerUI.G_le.setText("0")
            addColorCheckerUI.G_le.selectAll()
        if int(addColorCheckerUI.G_le.text()) > 255 : 
            addColorCheckerUI.G_le.setText("255")
        
        if addColorCheckerUI.B_le.text() == "" : 
            addColorCheckerUI.B_le.setText("0")
            addColorCheckerUI.B_le.selectAll()
        if int(addColorCheckerUI.B_le.text()) > 255 : 
            addColorCheckerUI.B_le.setText("255")

        global palette
        RGB = (int(addColorCheckerUI.R_le.text()), int(addColorCheckerUI.G_le.text()), int(addColorCheckerUI.B_le.text()))

        if addColorCheckerUI.palette_rb_1.isChecked() : 
            palette[0] = RGB
            addColorCheckerUI.palette_rb_1.setStyleSheet("QRadioButton{\n"
                                                                f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                                "border-radius : 6px;\n"
                                                            "}\n"
                                                            "QRadioButton::indicator{\n"
                                                                "width : 1px;\n"
                                                            "}\n"
                                                            "QRadioButton::checked{\n"
                                                                "border : 2px solid #ffffff;\n"
                                                            "}")

        if addColorCheckerUI.palette_rb_2.isChecked() : 
            palette[1] = RGB
            addColorCheckerUI.palette_rb_2.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_3.isChecked() : 
            palette[2] = RGB
            addColorCheckerUI.palette_rb_3.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_4.isChecked() : 
            palette[3] = RGB
            addColorCheckerUI.palette_rb_4.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_5.isChecked() : 
            palette[4] = RGB
            addColorCheckerUI.palette_rb_5.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_6.isChecked() : 
            palette[5] = RGB
            addColorCheckerUI.palette_rb_6.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_7.isChecked() : 
            palette[6] = RGB
            addColorCheckerUI.palette_rb_7.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_8.isChecked() : 
            palette[7] = RGB
            addColorCheckerUI.palette_rb_8.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_9.isChecked() : 
            palette[8] = RGB
            addColorCheckerUI.palette_rb_9.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_10.isChecked() : 
            palette[9] = RGB
            addColorCheckerUI.palette_rb_10.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_11.isChecked() : 
            palette[10] = RGB
            addColorCheckerUI.palette_rb_11.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")

        if addColorCheckerUI.palette_rb_12.isChecked() : 
            palette[11] = RGB
            addColorCheckerUI.palette_rb_12.setStyleSheet("QRadioButton{\n"
                                                            f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                                            "border-radius : 6px;\n"
                                                        "}\n"
                                                        "QRadioButton::indicator{\n"
                                                            "width : 1px;\n"
                                                        "}\n"
                                                        "QRadioButton::checked{\n"
                                                            "border : 2px solid #ffffff;\n"
                                                        "}")



    def copyColor(self) : 
        if addColorCheckerUI.X_le.text() == "" or addColorCheckerUI.Y_le.text() == "" : 
            mainUI.noticeBoard.addItem("[system] 좌표 설정 후 다시 시도해주십시오.")
            mainUI.noticeBoard.scrollToBottom()


        else : 
            RGB = pyautogui.screenshot().getpixel((int(addColorCheckerUI.X_le.text()), int(addColorCheckerUI.Y_le.text())))
            addColorCheckerUI.R_le.setText(str(RGB[0]))
            addColorCheckerUI.G_le.setText(str(RGB[1]))
            addColorCheckerUI.B_le.setText(str(RGB[2]))



    ## << addColorChecker_part (3/3) >> --------------------
    def addColorChecker(self) : 
        if Load_status == True : 
            if len(macroDATA) != 0 : 
                if addColorCheckerUI.X_le.text() != "" and addColorCheckerUI.Y_le.text() != "" : 
                    addObj = editUI.setMacro_cb.currentIndex()
                    # Add the data of macro to list
                    macroDATA[addObj].append("<C>")
                    coordinate = (int(addColorCheckerUI.X_le.text()), int(addColorCheckerUI.Y_le.text()))
                    box = [coordinate, int(addColorCheckerUI.checkingDelay_le.text()), palette]
                    macroDATA[addObj].append(box)
                    # Save the data of macro to file
                    with open(FILE_road, "wb") as file : 
                        pickle.dump(macroDATA, file)
                    # Notify addColorChecker event
                    mainUI.noticeBoard.addItem("[system] 컬러체커 추가가 완료되었습니다.")
                    mainUI.noticeBoard.scrollToBottom()
                    # Apply the update to editMacro_lw
                    self.setMacro()


                else : 
                    mainUI.noticeBoard.addItem("[system] 설정된 좌표가 없어 컬러체커를 추가할 수 없습니다.")
                    mainUI.noticeBoard.scrollToBottom()


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def detailDelete(self) : 
        if Load_status == True : 
            delObj = editUI.editMacro_lw.currentRow()
            if delObj != -1 : 
                mainObj = editUI.setMacro_cb.currentIndex()
                # Delete the data of detail macro in list
                del macroDATA[mainObj][(delObj+1)*2 - 1 : (delObj+1)*2 + 1]
                # Save the data of macro to file
                with open(FILE_road, "wb") as file : 
                    pickle.dump(macroDATA, file)
                # Notify detailDelete event
                mainUI.noticeBoard.addItem("[system] 선택한 매크로를 삭제했습니다.")
                mainUI.noticeBoard.scrollToBottom()
                # Apply the update to editMacro_lw
                self.setMacro()
            
            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def checkNum(self) : 
        mainObj = editUI.setMacro_cb.currentIndex()
        checkObj = editUI.editMacro_lw.currentRow()

        if checkObj == 0 : 
            editUI.up_bt.setEnabled(False)
            editUI.down_bt.setEnabled(True)

        elif checkObj == int((len(macroDATA[mainObj])-3)/2) : 
            editUI.up_bt.setEnabled(True)
            editUI.down_bt.setEnabled(False)

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
                macroDATA[mainObj][moveObj*2 + 1], macroDATA[mainObj][moveObj*2 - 1] = macroDATA[mainObj][moveObj*2 - 1], macroDATA[mainObj][moveObj*2 + 1]
                # Skill swap
                macroDATA[mainObj][moveObj*2 + 2], macroDATA[mainObj][moveObj * 2] = macroDATA[mainObj][moveObj * 2], macroDATA[mainObj][moveObj*2 + 2]
                # Save the data of macro to file
                with open(FILE_road, "wb") as file : 
                    pickle.dump(macroDATA, file)
                # Apply the update to editMacro_lw
                self.setMacro()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
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
                macroDATA[mainObj][(moveObj+1)*2 - 1], macroDATA[mainObj][(moveObj+1)*2 + 1] = macroDATA[mainObj][(moveObj+1)*2 + 1], macroDATA[mainObj][(moveObj+1)*2 - 1]
                # Skill swap
                macroDATA[mainObj][(moveObj+1) * 2], macroDATA[mainObj][(moveObj+2) * 2] = macroDATA[mainObj][(moveObj+2) * 2], macroDATA[mainObj][(moveObj+1) * 2]
                # Save the data of macro to file
                with open(FILE_road, "wb") as file : 
                    pickle.dump(macroDATA, file)
                # Apply the update to editMacro_lw
                self.setMacro()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def delete(self) : 
        if Load_status == True : 
            if len(macroDATA) != 0 : 
                delObj = mainUI.delete_cb.currentIndex()
                # Remove the data of macro in comboBoxes
                mainUI.delete_cb.removeItem(delObj)
                mainUI.start_cb.removeItem(delObj)
                editUI.setMacro_cb.removeItem(delObj)
                # Delete the data of macro in list
                del macroDATA[delObj]
                # Save the data of macro to file
                with open(FILE_road, "wb") as file : 
                    pickle.dump(macroDATA, file)

                mainUI.noticeBoard.addItem("[system] 선택한 매크로를 삭제했습니다.")
                mainUI.noticeBoard.scrollToBottom()


            else : 
                mainUI.noticeBoard.addItem("[system] 선택한 매크로가 없습니다.")
                mainUI.noticeBoard.scrollToBottom()


        else : 
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
            mainUI.noticeBoard.scrollToBottom()



    def startMacro(self) : 
        if Load_status == True : 
            from KOM_mainUI import startType

            global power
            power = True
            
            if len(macroDATA) != 0 : 
                if startType == "typeNum" : 
                    mainUI.start_bt_typeNum_active()
                elif startType == "typeTime" : 
                    mainUI.start_bt_typeTime_active()

                startObj = mainUI.start_cb.currentIndex()
                
                global runTime
                runTime = int(mainUI.start_le.text())

                macroNum = int((len(macroDATA[startObj])-1) / 2)

                while power == True and runTime != 0 : 
                    for i in range(macroNum) : 
                        if power == False : 
                            break

                        # << Left Click (1/4) >> --------------------
                        if macroDATA[startObj][(i+1)*2 - 1] == "<L>" : 
                            pyautogui.moveTo(macroDATA[startObj][(i+1) * 2])
                            time.sleep(0.05)
                            pyautogui.click(macroDATA[startObj][(i+1) * 2])
                        

                        # << Right Click (2/4) >> --------------------
                        elif macroDATA[startObj][(i+1)*2 - 1] == "<R>" : 
                            pyautogui.moveTo(macroDATA[startObj][(i+1) * 2])
                            time.sleep(0.05)
                            pyautogui.rightClick(macroDATA[startObj][(i+1) * 2])

                        
                        # << Keyboard input (3/4) >> --------------------
                        elif macroDATA[startObj][(i+1)*2 - 1] == "<K>" : 
                            key = macroDATA[startObj][(i+1) * 2].split("+")
                            if len(key) == 1 : 
                                pyautogui.hotkey(key[0])
                            elif len(key) == 2 : 
                                pyautogui.hotkey(key[0], key[1])
                            elif len(key) == 3 : 
                                pyautogui.hotkey(key[0], key[1], key[2])


                        # << Delay (4/4) >> --------------------
                        elif macroDATA[startObj][(i+1)*2 - 1] == "<D>" : 
                            delay = float(macroDATA[startObj][(i+1) * 2])
                            for _ in range(int(delay)) : 
                                if power == False : 
                                    break
                                time.sleep(1)
                            time.sleep(float(delay) - int(delay))
                                

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
            mainUI.noticeBoard.addItem("[system] 아직 매크로 데이터를 불러오지 않았습니다.")
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