'''
======================================================================================
                              < The_King_of_Macro_v2.2 >

                         이제부터 귀찮은 일들은 모두 사라집니다.

                                 * Made by Yoonmen *

                               - 23.?.? (???) ??:?? -
======================================================================================
'''

import sys
from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtCore import QThread, QCoreApplication, QEvent, QObject, Qt, Signal

from time import sleep as timeSleep, strftime
from os import path
from pickle import load as pickleLoad, dump as pickleDump
from keyboard import read_hotkey as keyboard_read_hotkey, is_pressed as keyboard_is_pressed
from pyautogui import position as getPosition, screenshot, moveTo, click, rightClick, hotkey
from webbrowser import open as openWebBrowser
from collections import deque

from KOM_mainUI import MainUI
from KOM_settingUI import SettingUI
from KOM_editUI import EditUI, AddDelayUI, AddColorCheckerUI, DeletePaletteUI, StyleSheets

class Main(QObject) : 
    def __init__(self) : 
        super().__init__()

        global mainUI, settingUI, editUI, addDelayUI, addColorCheckerUI, deletePaletteUI
        mainUI, settingUI, editUI, addDelayUI, addColorCheckerUI, deletePaletteUI = MainUI(), SettingUI(), EditUI(), AddDelayUI(), AddColorCheckerUI(), DeletePaletteUI()

        global QMacroThread, macroThread
        QMacroThread = QThread()
        QMacroThread.start()
        macroThread = MacroThread()
        macroThread.moveToThread(QMacroThread)

        global QStopKeyListenerThread, stopKeyListenerThread
        QStopKeyListenerThread = QThread()
        QStopKeyListenerThread.start()
        stopKeyListenerThread = StopKeyListenerThread()
        stopKeyListenerThread.moveToThread(QStopKeyListenerThread)

        global QTimerThread, timerThread
        QTimerThread = QThread()
        QTimerThread.start()
        timerThread = TimerThread()
        timerThread.moveToThread(QTimerThread)

        global load_status, stop_key, is_edit_ui_opened, palette_phase, palette
        load_status = False
        stop_key = "esc"
        is_edit_ui_opened = False
        palette_phase = 1
        palette = deque([(255, 0, 255)])

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())



    def signal(self) : 
        # < MainUI (1 / 6) > --------------------
        mainUI.keep_bt.clicked.connect(mainUI.showMinimized)
        mainUI.exit_bt.clicked.connect(self.exit)

        mainUI.setting_bt.clicked.connect(settingUI.show)

        macroThread.logging_signal.connect(self.logging)

        mainUI.addNewMacro_bt.clicked.connect(self.addNewMacro)
        mainUI.addNewMacro_le.returnPressed.connect(self.addNewMacro)

        mainUI.edit_bt.clicked.connect(self.toggleEditUI)

        mainUI.delete_bt.clicked.connect(self.deleteMacro)

        mainUI.start_le.returnPressed.connect(macroThread.startMacro)
        mainUI.start_bt.clicked.connect(macroThread.startMacro)
        macroThread.start_signal.connect(self.joyGo)                 # Test code / please modify the contents of this line.
        mainUI.start_bt.clicked.connect(stopKeyListenerThread.detectStopKey)
        mainUI.start_bt.clicked.connect(timerThread.startTimer)
        timerThread.time_modify_signal.connect(self.modifyTime)


        # < SettingUI (2 / 6) > --------------------
        settingUI.exit_bt.clicked.connect(settingUI.close)

        settingUI.load_bt.clicked.connect(self.loadData)
        settingUI.setStopKey_bt.clicked.connect(self.setStopKey)
        settingUI.winToTop_ckb.stateChanged.connect(self.winToTop)


        # < EditUI (3 / 6) > --------------------
        editUI.exit_bt.clicked.connect(self.toggleEditUI)

        editUI.setMacro_cb.currentIndexChanged.connect(self.setMacro)

        editUI.addClick_bt.clicked.connect(self.addClick)
        editUI.addKeyboard_bt.clicked.connect(self.addKeyboard)
        editUI.addDelay_bt.clicked.connect(self.addDelay)
        editUI.addColorChecker_bt.clicked.connect(self.addColorChecker)

        editUI.delete_bt.clicked.connect(self.removeMacroElement)
        editUI.remove_item_signal.connect(self.removeMacroElement)


        # < addDelayUI (4 / 6) > --------------------
        addDelayUI.exit_bt.clicked.connect(addDelayUI.close)

        addDelayUI.add_bt.clicked.connect(addDelayUI.accept)
        addDelayUI.addDelay_le.returnPressed.connect(addDelayUI.accept)
        addDelayUI.cancel_bt.clicked.connect(addDelayUI.reject)


        # < addColorCheckerUI (5 / 6) --------------------
        addColorCheckerUI.exit_bt.clicked.connect(addColorCheckerUI.close)

        addColorCheckerUI.setCoordinate_bt.clicked.connect(self.setCoordinate)

        addColorCheckerUI.addPalette_bt.clicked.connect(self.addNewPalette)

        addColorCheckerUI.palette_rb_1.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_2.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_3.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_4.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_5.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_6.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_7.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_8.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_9.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_10.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_11.clicked.connect(self.setRGB)
        addColorCheckerUI.palette_rb_12.clicked.connect(self.setRGB)

        addColorCheckerUI.R_le.textChanged.connect(self.setColor)
        addColorCheckerUI.G_le.textChanged.connect(self.setColor)
        addColorCheckerUI.B_le.textChanged.connect(self.setColor)

        addColorCheckerUI.copyColor_bt.clicked.connect(self.copyColor)

        addColorCheckerUI.add_bt.clicked.connect(addColorCheckerUI.accept)



    def exit(self) -> None : 
        QMacroThread.quit()
        QStopKeyListenerThread.quit()
        QTimerThread.quit()
        QCoreApplication.instance().quit()



    def logging(self, message: str) -> None : 
        mainUI.log_lw.addItem(f"[{strftime('%H:%M:%S')}] {message}")
        mainUI.log_lw.setCurrentRow(mainUI.log_lw.count()-1)
        mainUI.log_lw.scrollToBottom()



    def loadData(self) -> None : 
        global file_path
        file_path, _ = QFileDialog.getOpenFileName()

        if not file_path : 
            self.logging("데이터 불러오기를 취소했습니다.")
            return

        file_name = path.basename(file_path)
        if file_name != "data.dat" : 
            self.logging("데이터를 불러오는데 실패했습니다.")
            return

        with open(file_path, "rb") as file : 
            global data
            data = pickleLoad(file)

        for macro_name in data.keys() : 
            mainUI.delete_cb.addItem(macro_name)
            mainUI.start_cb.addItem(macro_name)
            editUI.setMacro_cb.addItem(macro_name)

        global load_status
        load_status = True

        self.logging("데이터를 불러오는데 성공했습니다.")



    def winToTop(self) -> None : 
        flags = Qt.FramelessWindowHint
        if settingUI.winToTop_ckb.isChecked() : 
            flags |= Qt.WindowStaysOnTopHint
        
        mainUI.setWindowFlags(flags)
        settingUI.setWindowFlags(flags)
        editUI.setWindowFlags(flags)
        addDelayUI.setWindowFlags(flags)
        addColorCheckerUI.setWindowFlags(flags)
        deletePaletteUI.setWindowFlags(flags)

        mainUI.show()
        settingUI.show()
        if is_edit_ui_opened : editUI.show()



    def addNewMacro(self) -> None : 
        if not load_status : 
            self.logging("아직 매크로 데이터를 불러오지 않았습니다.")
            return
        
        macro_name = mainUI.addNewMacro_le.text()
        mainUI.addNewMacro_le.clear()
        if not macro_name : 
            self.logging("공백을 이름으로 사용할 수 없습니다.")
            return
        
        global data
        data[macro_name] = deque()

        mainUI.delete_cb.addItem(macro_name)
        mainUI.start_cb.addItem(macro_name)
        editUI.setMacro_cb.addItem(macro_name)

        with open(file_path, "wb") as file : 
            pickleDump(data, file)
        
        self.logging("새로운 매크로를 추가했습니다.")



    def toggleEditUI(self) -> None : 
        global is_edit_ui_opened
        editUI.show() if not is_edit_ui_opened else editUI.close()
        is_edit_ui_opened = not is_edit_ui_opened



    def setMacro(self) -> None : 
        editUI.editMacro_lw.clear()
        
        target_name = editUI.setMacro_cb.currentText()
        if not target_name : return

        for i in range(0, len(data[target_name]), 2) : 
            key, action = data[target_name][i], data[target_name][i+1]
            if key == "<L>" : 
                editUI.editMacro_lw.addItem(f"마우스 {action} 좌클릭")
            elif key == "<R>" : 
                editUI.editMacro_lw.addItem(f"마우스 {action} 우클릭")
            elif key == "<K>" : 
                editUI.editMacro_lw.addItem(f"키보드 < {action} > 입력")
            elif key == "<D>" : 
                editUI.editMacro_lw.addItem(f"딜레이 < {action} > 초")
            elif key == "<C>" : 
                editUI.editMacro_lw.addItem(f"컬러체커 {action[0]}에서 {action[1]}초마다 진행")



    def addClick(self) -> None : 
        if not load_status : 
            self.logging("아직 매크로 데이터를 불러오지 않았습니다.")
            return

        if not data : 
            self.logging("선택한 매크로가 없습니다.")
            return
        
        editUI.addClick_bt.setStyleSheet(StyleSheets.active_push_button.value)

        target_name = editUI.setMacro_cb.currentText()

        def save_click_position(click_type) : 
            x, y = getPosition()
            data[target_name].append(click_type)
            data[target_name].append((x, y))
            with open(file_path, "wb") as file : 
                pickleDump(data, file)

            self.logging("클릭 좌표가 저장되었습니다.")
            self.setMacro()

        while True : 
            if keyboard_is_pressed("F9") : 
                save_click_position("<L>")
                break
            elif keyboard_is_pressed("F10") : 
                save_click_position("<R>")
                break
        
        editUI.addClick_bt.setStyleSheet(StyleSheets.push_button.value)



    def addKeyboard(self) -> None : 
        if not load_status : 
            self.logging("아직 매크로 데이터를 불러오지 않았습니다.")
            return
        
        if not data : 
            self.logging("선택한 매크로가 없습니다.")
            return

        editUI.addKeyboard_bt.setStyleSheet(StyleSheets.active_push_button.value)

        target_name = editUI.setMacro_cb.currentText()

        key = keyboard_read_hotkey(suppress=False)
        data[target_name].append("<K>")
        data[target_name].append(key)
        with open(file_path, "wb") as file : 
            pickleDump(data, file)

        self.logging("키보드 입력이 저장되었습니다.")
        self.setMacro()

        editUI.addKeyboard_bt.setStyleSheet(StyleSheets.push_button.value)



    def addDelay(self) -> None : 
        if not load_status : 
            self.logging("아직 매크로 데이터를 불러오지 않았습니다.")
            return
        
        if not data : 
            self.logging("선택한 매크로가 없습니다.")
            return

        editUI.addDelay_bt.setStyleSheet(StyleSheets.active_push_button.value)
        
        if addDelayUI.exec_() == addDelayUI.Rejected : 
            editUI.addDelay_bt.setStyleSheet(StyleSheets.push_button.value)
            return
        
        target_name = editUI.setMacro_cb.currentText()

        delay = float(addDelayUI.addDelay_le.text())
        data[target_name].append("<D>")
        data[target_name].append(delay)
        with open(file_path, "wb") as file : 
            pickleDump(data, file)

        self.logging("딜레이가 저장되었습니다.")
        self.setMacro()

        editUI.addDelay_bt.setStyleSheet(StyleSheets.push_button.value)



    def removeMacroElement(self) -> None : 
        if not load_status : 
            self.logging("아직 매크로 데이터를 불러오지 않았습니다.")
            return
        
        target_index = editUI.editMacro_lw.currentRow()
        if target_index == -1 : 
            self.logging("선택한 매크로가 없습니다.")
            return
        
        macro_name = editUI.setMacro_cb.currentText()
        del data[macro_name][target_index*2 : target_index*2+2]

        self.setMacro()
        with open(file_path, "wb") as file : 
            pickleDump(data, file)

        self.logging("선택한 매크로를 삭제했습니다.")



    def setCoordinate(self) -> None : 
        addColorCheckerUI.setCoordinate_bt.setStyleSheet(StyleSheets.active_push_button.value)

        while True : 
            if keyboard_is_pressed("F9") or keyboard_is_pressed("F10") : 
                x, y = getPosition()
                addColorCheckerUI.x_coordinate_le.setText(str(x))
                addColorCheckerUI.y_coordinate_le.setText(str(y))
                break
            elif keyboard_is_pressed("ESC") : 
                break

        addColorCheckerUI.setCoordinate_bt.setStyleSheet(StyleSheets.push_button.value)



    def addColorChecker(self) -> None : 
        if not load_status : 
            self.logging("아직 매크로 데이터를 불러오지 않았습니다.")
            return
        
        if not data : 
            self.logging("선택한 매크로가 없습니다.")
            return

        editUI.addColorChecker_bt.setStyleSheet(StyleSheets.active_push_button.value)

        if addColorCheckerUI.exec_() == addColorCheckerUI.Rejected : 
            editUI.addColorChecker_bt.setStyleSheet(StyleSheets.push_button.value)
            return

        editUI.addColorChecker_bt.setStyleSheet(StyleSheets.push_button.value)



    def addNewPalette(self) -> None : 
        if palette_phase == 1 : 
            addColorCheckerUI.addPalette_bt.setGeometry(192, 216, 21, 21)
            addColorCheckerUI.palette_rb_2.show()
            palette.append((255, 0, 255))
            palette_phase += 1

        elif palette_phase == 2 : 
            addColorCheckerUI.addPalette_bt.setGeometry(251, 216, 21, 21)
            addColorCheckerUI.palette_rb_3.show()
            palette.append((255, 0, 255))
            palette_phase += 1

        elif palette_phase == 3 : 
            addColorCheckerUI.addPalette_bt.setGeometry(74, 250, 21, 21)
            addColorCheckerUI.palette_rb_4.show()
            palette.append((255, 0, 255))   
            palette_phase += 1

        elif palette_phase == 4 : 
            addColorCheckerUI.addPalette_bt.setGeometry(133, 250, 21, 21)
            addColorCheckerUI.palette_rb_5.show()
            palette.append((255, 0, 255))
            palette_phase += 1
        
        elif palette_phase == 5 : 
            addColorCheckerUI.addPalette_bt.setGeometry(192, 250, 21, 21)
            addColorCheckerUI.palette_rb_6.show()
            palette.append((255, 0, 255))
            palette_phase += 1

        elif palette_phase == 6 : 
            addColorCheckerUI.addPalette_bt.setGeometry(251, 250, 21, 21)
            addColorCheckerUI.palette_rb_7.show()
            palette.append((255, 0, 255))
            palette_phase += 1

        elif palette_phase == 7 : 
            addColorCheckerUI.addPalette_bt.setGeometry(74, 284, 21, 21)
            addColorCheckerUI.palette_rb_8.show()
            palette.append((255, 0, 255))
            palette_phase += 1

        elif palette_phase == 8 : 
            addColorCheckerUI.addPalette_bt.setGeometry(133, 284, 21, 21)
            addColorCheckerUI.palette_rb_9.show()
            palette.append((255, 0, 255))
            palette_phase += 1

        elif palette_phase == 9 : 
            addColorCheckerUI.addPalette_bt.setGeometry(192, 284, 21, 21)
            addColorCheckerUI.palette_rb_10.show()
            palette.append((255, 0, 255))
            palette_phase += 1

        elif palette_phase == 10 : 
            addColorCheckerUI.addPalette_bt.setGeometry(251, 284, 21, 21)
            addColorCheckerUI.palette_rb_11.show()
            palette.append((255, 0, 255))
            palette_phase += 1
        
        elif palette_phase == 11 : 
            addColorCheckerUI.addPalette_bt.hide()
            addColorCheckerUI.palette_rb_12.show()
            palette.append((255, 0, 255))
            palette_phase += 1



    def setRGB(self) -> None :  
        def displayRGB(RGB: tuple[int, int, int]) -> None : 
            addColorCheckerUI.R_le.setText(str(RGB[0]))
            addColorCheckerUI.G_le.setText(str(RGB[1]))
            addColorCheckerUI.B_le.setText(str(RGB[2]))

        if addColorCheckerUI.palette_rb_1.isChecked() : 
            displayRGB(palette[0])

        elif addColorCheckerUI.palette_rb_2.isChecked() : 
            displayRGB(palette[1])
        
        elif addColorCheckerUI.palette_rb_3.isChecked() : 
            displayRGB(palette[2])

        elif addColorCheckerUI.palette_rb_4.isChecked() : 
            displayRGB(palette[3])
        
        elif addColorCheckerUI.palette_rb_5.isChecked() : 
            displayRGB(palette[4])
        
        elif addColorCheckerUI.palette_rb_6.isChecked() : 
            displayRGB(palette[5])
        
        elif addColorCheckerUI.palette_rb_7.isChecked() : 
            displayRGB(palette[6])
        
        elif addColorCheckerUI.palette_rb_8.isChecked() : 
            displayRGB(palette[7])

        elif addColorCheckerUI.palette_rb_9.isChecked() : 
            displayRGB(palette[8])
        
        elif addColorCheckerUI.palette_rb_10.isChecked() : 
            displayRGB(palette[9])

        elif addColorCheckerUI.palette_rb_11.isChecked() : 
            displayRGB(palette[10])

        elif addColorCheckerUI.palette_rb_12.isChecked() : 
            displayRGB(palette[11])



    def setColor(self) -> None : 
        if addColorCheckerUI.R_le.text() == "" : 
            addColorCheckerUI.R_le.setText("0")
            addColorCheckerUI.R_le.selectAll()
        elif int(addColorCheckerUI.R_le.text()) > 255 : 
            addColorCheckerUI.R_le.setText("255")
        
        if addColorCheckerUI.G_le.text() == "" : 
            addColorCheckerUI.G_le.setText("0")
            addColorCheckerUI.G_le.selectAll()
        elif int(addColorCheckerUI.G_le.text()) > 255 : 
            addColorCheckerUI.G_le.setText("255")
        
        if addColorCheckerUI.B_le.text() == "" : 
            addColorCheckerUI.B_le.setText("0")
            addColorCheckerUI.B_le.selectAll()
        elif int(addColorCheckerUI.B_le.text()) > 255 : 
            addColorCheckerUI.B_le.setText("255")

        RGB = (int(addColorCheckerUI.R_le.text()), int(addColorCheckerUI.G_le.text()), int(addColorCheckerUI.B_le.text()))
        background_styleSheet = ("QRadioButton::indicator{\n"
                                    f"background-color: rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                                "}")

        if addColorCheckerUI.palette_rb_1.isChecked() : 
            palette[0] = RGB
            addColorCheckerUI.palette_rb_1.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_2.isChecked() : 
            palette[1] = RGB
            addColorCheckerUI.palette_rb_2.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_3.isChecked() : 
            palette[2] = RGB
            addColorCheckerUI.palette_rb_3.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_4.isChecked() : 
            palette[3] = RGB
            addColorCheckerUI.palette_rb_4.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_5.isChecked() : 
            palette[4] = RGB
            addColorCheckerUI.palette_rb_5.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_6.isChecked() : 
            palette[5] = RGB
            addColorCheckerUI.palette_rb_6.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_7.isChecked() : 
            palette[6] = RGB
            addColorCheckerUI.palette_rb_7.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_8.isChecked() : 
            palette[7] = RGB
            addColorCheckerUI.palette_rb_8.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_9.isChecked() : 
            palette[8] = RGB
            addColorCheckerUI.palette_rb_9.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_10.isChecked() : 
            palette[9] = RGB
            addColorCheckerUI.palette_rb_10.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_11.isChecked() : 
            palette[10] = RGB
            addColorCheckerUI.palette_rb_11.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)

        if addColorCheckerUI.palette_rb_12.isChecked() : 
            palette[11] = RGB
            addColorCheckerUI.palette_rb_12.setStyleSheet(StyleSheets.palette.value + 
                                                         background_styleSheet)



    def copyColor(self) -> None : 
        pass                # Test code / please delete the contents of this line.



    def deletePalette(self) -> None : 
        if addColorCheckerUI.palette_rb_1.isChecked() : del palette[0]
        elif addColorCheckerUI.palette_rb_2.isChecked() : del palette[1]
        elif addColorCheckerUI.palette_rb_3.isChecked() : del palette[2]
        elif addColorCheckerUI.palette_rb_4.isChecked() : del palette[3]
        elif addColorCheckerUI.palette_rb_5.isChecked() : del palette[4]
        elif addColorCheckerUI.palette_rb_6.isChecked() : del palette[5]
        elif addColorCheckerUI.palette_rb_7.isChecked() : del palette[6]
        elif addColorCheckerUI.palette_rb_8.isChecked() : del palette[7]
        elif addColorCheckerUI.palette_rb_9.isChecked() : del palette[8]
        elif addColorCheckerUI.palette_rb_10.isChecked() : del palette[9]
        elif addColorCheckerUI.palette_rb_11.isChecked() : del palette[10]
        elif addColorCheckerUI.palette_rb_12.isChecked() : del palette[11]

        global palette_phase
        if palette_phase == 12 : 
            addColorCheckerUI.palette_rb_12.hide()
            addColorCheckerUI.palette_rb_12.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(251, 284, 21, 21)
            addColorCheckerUI.addPalette_bt.show()
        elif palette_phase == 11 : 
            addColorCheckerUI.palette_rb_11.hide()
            addColorCheckerUI.palette_rb_11.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(192, 284, 21, 21)
        elif palette_phase == 10 : 
            addColorCheckerUI.palette_rb_10.hide()
            addColorCheckerUI.palette_rb_10.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(133, 284, 21, 21)
        elif palette_phase == 9 : 
            addColorCheckerUI.palette_rb_9.hide()
            addColorCheckerUI.palette_rb_9.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(74, 284, 21, 21)
        elif palette_phase == 8 : 
            addColorCheckerUI.palette_rb_8.hide()
            addColorCheckerUI.palette_rb_8.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(251, 250, 21, 21)
        elif palette_phase == 7 : 
            addColorCheckerUI.palette_rb_7.hide()
            addColorCheckerUI.palette_rb_7.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(192, 250, 21, 21)
        elif palette_phase == 6 : 
            addColorCheckerUI.palette_rb_6.hide()
            addColorCheckerUI.palette_rb_6.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(133, 250, 21, 21)
        elif palette_phase == 5 : 
            addColorCheckerUI.palette_rb_5.hide()
            addColorCheckerUI.palette_rb_5.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(74, 250, 21, 21)
        elif palette_phase == 4 : 
            addColorCheckerUI.palette_rb_4.hide()
            addColorCheckerUI.palette_rb_4.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(251, 216, 21, 21)
        elif palette_phase == 3 : 
            addColorCheckerUI.palette_rb_3.hide()
            addColorCheckerUI.palette_rb_3.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(192, 216, 21, 21)
        elif palette_phase == 2 : 
            addColorCheckerUI.palette_rb_2.hide()
            addColorCheckerUI.palette_rb_2.setStyleSheet(StyleSheets.palette.value)
            addColorCheckerUI.addPalette_bt.setGeometry(133, 216, 21, 21)

        palette_phase -= 1

        def makeBackgroundStyleSheet(RGB: tuple[int, int, int]) -> str : 
            return ("QRadioButton::indicator{\n"
                        f"background-color : rgb({RGB[0]}, {RGB[1]}, {RGB[2]});\n"
                    "}")
        addColorCheckerUI.palette_rb_1.setStyleSheet(StyleSheets.palette.value + 
                                                     makeBackgroundStyleSheet(palette[0]))
        if palette_phase >= 2 : 
            addColorCheckerUI.palette_rb_2.setStyleSheet(StyleSheets.palette.value + 
                                                         makeBackgroundStyleSheet(palette[1]))
        if palette_phase >= 3 : 
            addColorCheckerUI.palette_rb_3.setStyleSheet(StyleSheets.palette.value + 
                                                         makeBackgroundStyleSheet(palette[2]))
        if palette_phase >= 4 : 
            addColorCheckerUI.palette_rb_4.setStyleSheet(StyleSheets.palette.value + 
                                                         makeBackgroundStyleSheet(palette[3]))
        if palette_phase >= 5 : 
            addColorCheckerUI.palette_rb_5.setStyleSheet(StyleSheets.palette.value + 
                                                         makeBackgroundStyleSheet(palette[4]))
        if palette_phase >= 6 : 
            addColorCheckerUI.palette_rb_6.setStyleSheet(StyleSheets.palette.value + 
                                                         makeBackgroundStyleSheet(palette[5]))
        if palette_phase >= 7 : 
            addColorCheckerUI.palette_rb_7.setStyleSheet(StyleSheets.palette.value + 
                                                         makeBackgroundStyleSheet(palette[6]))
        if palette_phase >= 8 : 
            addColorCheckerUI.palette_rb_8.setStyleSheet(StyleSheets.palette.value + 
                                                         makeBackgroundStyleSheet(palette[7]))
        if palette_phase >= 9 : 
            addColorCheckerUI.palette_rb_9.setStyleSheet(StyleSheets.palette.value + 
                                                         makeBackgroundStyleSheet(palette[8]))
        if palette_phase >= 10 : 
            addColorCheckerUI.palette_rb_10.setStyleSheet(StyleSheets.palette.value + 
                                                          makeBackgroundStyleSheet(palette[9]))
        if palette_phase >= 11 : 
            addColorCheckerUI.palette_rb_11.setStyleSheet(StyleSheets.palette.value + 
                                                          makeBackgroundStyleSheet(palette[10]))
        
        self.setRGB()



    def deleteMacro(self) -> None : 
        if not load_status : 
            self.logging("아직 매크로 데이터를 불러오지 않았습니다.")
            return
        
        if not data : 
            self.logging("선택한 매크로가 없습니다.")
            return

        target_index = mainUI.delete_cb.currentIndex()
        target_name = mainUI.delete_cb.currentText()
        
        mainUI.delete_cb.removeItem(target_index)
        mainUI.start_cb.removeItem(target_index)
        editUI.setMacro_cb.removeItem(target_index)

        del data[target_name]

        with open(file_path, "wb") as file : 
            pickleDump(data, file)
        
        self.logging("선택한 매크로를 삭제했습니다.")



    def setStopKey(self) -> None : 
        global stop_key
        stop_key = keyboard_read_hotkey(suppress=False)
        settingUI.setStopKey_bt.setText(stop_key)



    def modifyTime(self, num: int) -> None : 
        mainUI.start_le.setText(str(num))



    def joyGo(self) -> None : 
        # 이 함수에는 start_bt의 styleSheet 관련 내용이 들어갈 것만 같다.               # Test code / please delete the contents of this line.
        pass                # Test code / please delete the contents of this line.




class MacroThread(QObject) : 
    logging_signal = Signal(str)
    start_signal = Signal()

    def startMacro(self) : 
        if not load_status : 
            self.logging_signal.emit("아직 매크로 데이터를 불러오지 않았습니다.")
            return
        
        if not data : 
            self.logging_signal.emit("선택한 매크로가 없습니다.")
            return

        target_name = mainUI.start_cb.currentText()

        global power, macro_run_limit
        power = True
        macro_run_limit = int(mainUI.start_le.text())

        while (power) and (macro_run_limit > 0) : 
            for i in range(0, len(data[target_name]), 2) : 
                if not power : break
                key, action = data[target_name][i], data[target_name][i+1]
                if (key == "<L>") or (key == "<R>") : 
                    moveTo(action)
                    timeSleep(0.05)
                    click(action) if key == "<L>" else rightClick(action)
                elif key == "<K>" : 
                    keys = action.split("+")
                    hotkey(*keys)
                elif key == "<D>" : 
                    for _ in range(int(action)) : 
                        if not power : break
                        timeSleep(1)
                    if power : timeSleep(action - int(action))
                elif key == "<C>" : 
                    coordinate, delay, palettes = action
                    is_found = False
                    while (power) and (not is_found) : 
                        moveTo(coordinate)
                        for palette in palettes : 
                            if screenshot().getpixel(coordinate) == palette : 
                                is_found = True
                                break
                        if not is_found : 
                            for _ in range(int(delay)) : 
                                if not power : break
                                timeSleep(1)
                            if power : timeSleep(delay - int(delay))




class StopKeyListenerThread(QObject) : 
    def detectStopKey(self) : 
        global power
        while power : 
            if keyboard_is_pressed(stop_key) : 
                power = False
                break




class TimerThread(QObject) : 
    time_modify_signal = Signal(int)

    def startTimer(self) : 
        global power, macro_run_limit
        while (power) and (macro_run_limit > 0) : 
            timeSleep(1)
            macro_run_limit -= 1
            self.time_modify_signal.emit(macro_run_limit)

        power = False





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()
