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
from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtCore import QThread, QCoreApplication, QObject, Qt, Signal


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

        # Macro Thread
        global QMacroThread, macroThread
        QMacroThread = QThread()
        QMacroThread.start()
        macroThread = MacroThread()
        macroThread.moveToThread(QMacroThread)

        # StopKey Listener Thread
        global QStopKeyListenerThread, stopKeyListenerThread
        QStopKeyListenerThread = QThread()
        QStopKeyListenerThread.start()
        stopKeyListenerThread = StopKeyListenerThread()
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
    


    def signal(self): 

        pass                # Test code / please delete this line.




class MacroThread(QObject): 
    pass                # Test code / please delete this line.




class StopKeyListenerThread(QObject): 
    pass                # Test code / please delete this line.
        




if __name__ == "__main__": 
    launch()