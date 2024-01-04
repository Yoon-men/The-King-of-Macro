'''
The King of Macro

"From now on, all the bothersome tasks will disappear."

ver 2.2.0

~ Sun, Dec 31, 2023 ~

'''

VERSION = "2.2.0"

#* ------------------------------------------------------------ *#

## Python Modules
import sys
import logging
from typing import List, Tuple
from time import (
    sleep as time_sleep, 
    strftime as time_strftime
)
from os import (
    path as os_path
)
from pickle import (
    load as pickle_load, 
    dump as pickle_dump
)
from keyboard import (
    read_hotkey as keyboard_read_hotkey, 
    is_pressed as keyboard_is_pressed
)
from pyautogui import (
    position as getPosition, 
    screenshot, moveTo, click, rightClick, hotkey
)
from webbrowser import open as openWebBrowser
from collections import deque


## PySide2 Moduels
from PySide2.QtWidgets import QApplication, QFileDialog, QListWidgetItem
from PySide2.QtCore import QThread, QCoreApplication, QObject, Qt, Signal
from PySide2.QtGui import QColor


## User-defined Modules
from YM_Logger import (
    init_logger, 
    DEBUG, INFO, WARNING, ERROR, CRITICAL
)

from KOM_UI_Main import MainUI
from KOM_UI_Setting import SettingUI
from KOM_UI_Edit import EditUI, AddDelayUI, AddColorCheckerUI, DeletePaletteUI, StyleSheets

#* ------------------------------------------------------------ *#

def launch() -> None: 
    global logger
    logger = init_logger(
        program_name="The King of Macro", 
        version=VERSION, 
        c_level=DEBUG, 
        f_level=DEBUG,                  # Test code / please modify this line. (DEBUG -> INFO)
        f_path="./log"
    )
    
    app = QApplication(sys.argv)
    Main(app)
    ### ----- launch() end ----- ###

#* ------------------------------------------------------------ *#
    
class Main(QObject): 
    def __init__(self, app: QApplication): 
        super().__init__()

        # UIs
        global mainUI, settingUI, editUI, addDelayUI, addColorCheckerUI, deletePaletteUI
        mainUI, settingUI, editUI, addDelayUI, addColorCheckerUI, deletePaletteUI = MainUI(), SettingUI(), EditUI(), AddDelayUI(), AddColorCheckerUI(), DeletePaletteUI()

        # UI Processor Thread
        global QUiProcessorThread, uiProcessorThread
        QUiProcessorThread = QThread()
        QUiProcessorThread.start()
        uiProcessorThread = UiProcessor()
        uiProcessorThread.moveToThread(QUiProcessorThread)

        # Data Processor Thread
        global QDataProcessorThread, dataProcessorThread
        QDataProcessorThread = QThread()
        QDataProcessorThread.start()
        dataProcessorThread = DataProcessor()
        dataProcessorThread.moveToThread(QDataProcessorThread)

        # Macro Thread
        global QMacroThread, macroThread
        QMacroThread = QThread()
        QMacroThread.start()
        macroThread = MacroProcessor()
        macroThread.moveToThread(QMacroThread)

        # StopKey Listener Thread
        global QStopKeyListenerThread, stopKeyListenerThread
        QStopKeyListenerThread = QThread()
        QStopKeyListenerThread.start()
        stopKeyListenerThread = StopKeyListener()
        stopKeyListenerThread.moveToThread(QStopKeyListenerThread)

        global load_status, stop_key, is_edit_ui_opened, palette_phase, palette
        load_status = False
        stop_key = "esc"
        is_edit_ui_opened = False
        palette_phase = 1
        palette = deque([(255, 0, 255)])

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())

        ### ----- init() end ----- ###
    


    def signal(self) -> None: 
        # Rudimentary exit
        QCoreApplication.instance().aboutToQuit.connect(self.quit)

        # Logging
        macroThread.logging_signal.connect(self.logging)
        stopKeyListenerThread.logging_signal.connect(self.logging)
        pass                # Test code / please delete this line.

        ### ----- signal() end ----- ###



    def quit(self) -> None: 
        QMacroThread.quit()
        QStopKeyListenerThread.quit()

        QCoreApplication.instance().quit()
    
        ### ----- quit() end ----- ###
    


    def logging(self, _msg: str, _level: int, _color: str = "black") -> None: 
        log = QListWidgetItem(f"[{time_strftime('%H:%M:%S')}] - {_msg}")
        log.setTextColor(QColor(_color))

        mainUI.log_LW.addItem(log)
        mainUI.log_LW.setCurrentRow(mainUI.log_LW.count() - 1)
        mainUI.log_LW.scrollToBottom()

        logger.log(_level, _msg)

        ### ----- logging() end ----- ###

    ### ----- Main() end ----- ###




class UiProcessor(QObject): 
    def winToTop(self) -> None: 
        flags = Qt.FramelessWindowHint
        if settingUI.winToTop_CKB.isChecked(): 
            flags |= Qt.WindowStaysOnTopHint
        
        mainUI.setWindowFlags(flags)
        settingUI.setWindowFlags(flags)
        editUI.setWindowFlags(flags)
        addDelayUI.setWindowFlags(flags)
        addColorCheckerUI.setWindowFlags(flags)
        deletePaletteUI.setWindowFlags(flags)

        mainUI.show()
        settingUI.show()
        if is_edit_ui_opened: editUI.show()

        ### ----- winToTop() end ----- ###




class DataProcessor(QObject): 
    pass                # Test code / please delete this line.

    ### ----- DataProcessor() end ----- ###




class MacroProcessor(QObject): 
    pass                # Test code / please delete this line.

    ### ----- MacroProcessor() end ----- ###




class StopKeyListener(QObject): 
    pass                # Test code / please delete this line.

    ### ----- StopKeyListener() end ----- ###
        




if __name__ == "__main__": 
    launch()