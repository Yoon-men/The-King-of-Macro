'''
======================================================================================
                              < The_King_of_Macro_v2.2 >

                     이제부터 귀찮은 일들은 모두 사라집니다. 3, 2, 1!

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
from KOM_editUI import EditUI, AddDelayUI, AddColorCheckerUI, DeletePaletteUI

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

        mainUI.addNewMacro_bt.clicked.connect(self.addNewMacro)
        mainUI.addNewMacro_le.returnPressed.connect(self.addNewMacro)

        mainUI.edit_bt.clicked.connect(self.toggleEditUI)

        mainUI.delete_bt.clicked.connect(self.deleteMacro)

        mainUI.start_bt.clicked.connect(macroThread.startMacro)
        macroThread.loggingSignal.connect(self.logging)
        macroThread.startSignal.connect(self.joyGo)                 # Test code / please modify the contents of this line.
        mainUI.start_bt.clicked.connect(stopKeyListenerThread.detectStopKey)
        mainUI.start_bt.clicked.connect(timerThread.startTimer)


        # < SettingUI (2 / 6) > --------------------
        settingUI.exit_bt.clicked.connect(settingUI.close)

        settingUI.load_bt.clicked.connect(self.loadData)
        settingUI.setStopKey_bt.clicked.connect(self.setStopKey)
        settingUI.winToTop_ckb.stateChanged.connect(self.winToTop)


        # < EditUI (3 / 6) > --------------------
        editUI.exit_bt.clicked.connect(self.toggleEditUI)

        editUI.setMacro_cb.currentIndexChanged.connect(self.setMacro)

        editUI.addClick_bt.clicked.connect(self.addClick)
        editUI.addClick_bt.clicked.connect(self.addKeyboard)
        editUI.addDelay_bt.clicked.connect(self.openAddDelay)
        editUI.addColorChecker_bt.clicked.connect(self.openAddColorChecker)

        editUI.delete_bt.clicked.connect(self.deleteMacro)
    


    def exit(self) -> None : 
        QMacroThread.quit()
        QTimerThread.quit()
        QCoreApplication.instance().quit()



    def logging(self, message: str) -> None : 
        mainUI.log_lw.addItem(f"[{strftime('%Y-%m-%d')}] {message}")
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
        
        for i in range(len(data)) : 
            mainUI.delete_cb.addItem(data[i]["name"])
            mainUI.start_cb.addItem(data[i]["name"])
            editUI.setMacro_cb.addItem(data[i]["name"])

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
        
        macro_name = mainUI.addMacro_le.text()
        mainUI.addMacro_le.clear()
        if not macro_name : 
            self.logging("공백을 이름으로 사용할 수 없습니다.")
            return

        mainUI.delete_cb.addItem(macro_name)
        mainUI.start_cb.addItem(macro_name)
        editUI.setMacro_cb.addItem(macro_name)

        global data
        data[macro_name] = []

        with open(file_path, "wb") as file : 
            pickleDump(data, file)
        
        self.logging("새로운 매크로를 추가했습니다.")



    def toggleEditUI(self) : 
        global is_edit_ui_opened
        editUI.show() if not is_edit_ui_opened else editUI.close()
        is_edit_ui_opened = not is_edit_ui_opened



    def setMacro(self) : 
        editUI.editMacro_lw.clear()
        
        target_name = editUI.setMacro_cb.currentText()
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



    def addClick(self) : 
        if not load_status : 
            self.logging("아직 매크로 데이터를 불러오지 않았습니다.")
            return

        if not data : 
            self.logging("선택한 매크로가 없습니다.")
            return
        
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



    def deleteMacro(self) : 
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



    def setStopKey(self) : 
        global stop_key
        stop_key = keyboard_read_hotkey(suppress=False)
        settingUI.setStopKey_bt.setText(stop_key)



    def joyGo(self) : 
        pass                # Test code / please delete the contents of this line.




class MacroThread(QObject) : 
    loggingSignal = Signal(str)
    startSignal = Signal()

    def startMacro(self) : 
        if not load_status : 
            self.loggingSignal.emit("아직 매크로 데이터를 불러오지 않았습니다.")
            return
        
        if not data : 
            self.loggingSignal.emit("선택한 매크로가 없습니다.")
            return

        target = mainUI.start_cb.currentIndex()                 # Test code / please modify the contents of this line.
        # action_num = int(data)                # Test code / please modify the contents of this line.

        global power, action_time_limit
        power = True
        action_time_limit = int(mainUI.start_le.text())


        if mainUI.start_typeNum_rb.isChecked() : 
            pass                # Test code / please delete the contents of this line.
        elif mainUI.start_typeTime_rb.isChecked() : 
            pass                # Test code / please delete the contents of this line.




class StopKeyListenerThread(QObject) : 
    def detectStopKey(self) : 
        global power
        while power == True : 
            if keyboard_is_pressed(stop_key) : 
                power = False
                break




class TimerThread(QObject) : 
    def startTimer(self) : 
        if mainUI.start_typeTime_rb.isChecked() : 
            global action_time_limit, power
            while (power == True) and (action_time_limit > 0) : 
                timeSleep(1)
                action_time_limit -= 1
                pass                # Test code / please delete the contents of this line.





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()
