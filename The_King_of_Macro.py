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
from typing import List, Tuple, Union, Dict, Deque
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

import traceback


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

data: Dict[str, Deque[Union[Tuple[str, Tuple[int, int]], Tuple[str, float]]]]

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
        global QMacroProcessorThread, macroProcessorThread
        QMacroProcessorThread = QThread()
        QMacroProcessorThread.start()
        macroProcessorThread = MacroProcessor()
        macroProcessorThread.moveToThread(QMacroProcessorThread)

        # StopKey Listener Thread
        global QStopKeyListenerThread, stopKeyListenerThread
        QStopKeyListenerThread = QThread()
        QStopKeyListenerThread.start()
        stopKeyListenerThread = StopKeyListener()
        stopKeyListenerThread.moveToThread(QStopKeyListenerThread)

        global load_status, stop_key, palette_phase, palette
        load_status = False
        stop_key = "esc"
        palette_phase = 1
        palette = deque([(255, 0, 255)])

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())

        ### ----- init() end ----- ###
    


    def signal(self) -> None: 
        ## Rudimentary exit
        QCoreApplication.instance().aboutToQuit.connect(self.quit)


        ## Logging
        uiProcessorThread.logging_signal.connect(self.logging)
        dataProcessorThread.logging_signal.connect(self.logging)
        macroProcessorThread.logging_signal.connect(self.logging)
        stopKeyListenerThread.logging_signal.connect(self.logging)

        uiProcessorThread.logging_with_color_signal.connect(self.logging)
        dataProcessorThread.logging_with_color_signal.connect(self.logging)
        macroProcessorThread.logging_with_color_signal.connect(self.logging)
        stopKeyListenerThread.logging_with_color_signal.connect(self.logging)


        ## Main UI
        mainUI.keep_BT.clicked.connect(mainUI.showMinimized)
        mainUI.exit_BT.clicked.connect(self.quit)

        mainUI.setting_BT.clicked.connect(settingUI.show)

        mainUI.addNewMacro_BT.clicked.connect(dataProcessorThread.addNewMacro)
        mainUI.addNewMacro_LE.returnPressed.connect(dataProcessorThread.addNewMacro)

        mainUI.edit_BT.clicked.connect(uiProcessorThread.toggleEditUI)

        mainUI.delete_BT.clicked.connect(dataProcessorThread.deleteMacro)

        # mainUI.start_BT.clicked.connect(macroProcessorThread.startMacro)
        # mainUI.start_LE.returnPressed.connect(macroProcessorThread.startMacro)


        ## Setting UI
        settingUI.exit_BT.clicked.connect(settingUI.close)

        settingUI.load_BT.clicked.connect(dataProcessorThread.loadData)
        # settingUI.setStopKey_BT.clicked.connect(dataProcessorThread.setStopKey)
        settingUI.winToTop_CKB.clicked.connect(UiProcessor.winToTop)

        settingUI.github_BT.clicked.connect(lambda: openWebBrowser("https://github.com/Yoon-men/The_King_of_Macro"))


        ## Edit UI
        editUI.exit_BT.clicked.connect(uiProcessorThread.toggleEditUI)

        # editUI.setMacro_CB.currentIndexChanged.connect(uiProcessorThread.setMacro)

        editUI.editMacro_LW.itemMoved.connect(lambda: logger.info("아이템의 이동이 감지되었습니다."))               # Test code / please delete this line.

        # editUI.addClick_BT.clicked.connect(dataProcessorThread.addClick)
        # editUI.addKeyboard_BT.clicked.connect(dataProcessorThread.addKeyboard)
        # editUI.addDelay_BT.clicked.connect(dataProcessorThread.addDelay)
        # editUI.addColorChecker_BT.clicked.connect(dataProcessorThread.addColorChecker)

        # editUI.delete_BT.clicked.connect(dataProcessorThread.removeMacroElement)
        # editUI.remove_item_signal.connect(dataProcessorThread.removeMacroElement)


        ## AddDelay UI
        addDelayUI.exit_BT.clicked.connect(addDelayUI.close)

        addDelayUI.add_BT.clicked.connect(addDelayUI.accept)
        addDelayUI.addDelay_LE.returnPressed.connect(addDelayUI.accept)
        addDelayUI.cancel_BT.clicked.connect(addDelayUI.reject)


        ## AddColorChecker UI
        addColorCheckerUI.exit_BT.clicked.connect(addColorCheckerUI.close)

        # addColorCheckerUI.setCoordinate_BT.clicked.connect(uiProcessorThread.setCoordinate)

        # addColorCheckerUI.addPalette_BT.clicked.connect(uiProcessorThread.addPalette)

        # addColorCheckerUI.palette_1_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_2_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_3_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_4_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_5_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_6_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_7_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_8_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_9_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_10_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_11_RB.clicked.connect(uiProcessorThread.setRGB)
        # addColorCheckerUI.palette_12_RB.clicked.connect(uiProcessorThread.setRGB)

        # addColorCheckerUI.R_LE.textChanged.connect(uiProcessorThread.setColor)
        # addColorCheckerUI.G_LE.textChanged.connect(uiProcessorThread.setColor)
        # addColorCheckerUI.B_LE.textChanged.connect(uiProcessorThread.setColor)

        # addColorCheckerUI.copyColor_BT.clicked.connect(uiProcessorThread.copyColor)

        # addColorCheckerUI.add_BT.clicked.connect(addColorCheckerUI.accept)

        ### ----- signal() end ----- ###



    def quit(self) -> None: 
        QUiProcessorThread.quit()
        QDataProcessorThread.quit()
        QMacroProcessorThread.quit()
        QStopKeyListenerThread.quit()

        QCoreApplication.instance().quit()
    
        ### ----- quit() end ----- ###
    


    def logging(self, _msg: str, _level: int, _color: str = "#dddddd") -> None: 
        log = QListWidgetItem(f"[{time_strftime('%H:%M:%S')}] - {_msg}")
        log.setTextColor(QColor(_color))

        mainUI.log_LW.addItem(log)
        mainUI.log_LW.setCurrentRow(mainUI.log_LW.count() - 1)
        mainUI.log_LW.scrollToBottom()

        logger.log(_level, _msg)

        ### ----- logging() end ----- ###

    ### ----- Main() end ----- ###




class UiProcessor(QObject): 
    logging_signal = Signal(str, int)
    logging_with_color_signal = Signal(str, int, str)

    is_edit_ui_opened = False


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
        if UiProcessor.is_edit_ui_opened: editUI.show()

        ### ----- winToTop() end ----- ### 



    def toggleEditUI(self) -> None: 
        editUI.show() if not self.is_edit_ui_opened else editUI.close()
        is_edit_ui_opened = not is_edit_ui_opened

        ### ----- toggleEditUI() end ----- ###

    ### ----- UiProcessor() end ----- ###




class DataProcessor(QObject): 
    logging_signal = Signal(str, int)
    logging_with_color_signal = Signal(str, int, str)

    data_path = None


    def loadData(self) -> None: 
        try: 
            self.file_path, _ = QFileDialog.getOpenFileName()

            if not self.file_path: 
                self.logging_with_color_signal.emit("데이터 불러오기를 취소했습니다.", INFO, "#f55b5b")
                return
            
            file_name = os_path.basename(self.file_path)
            if file_name != "data.dat": 
                self.logging_with_color_signal.emit("데이터를 불러오는데 실패했습니다.", WARNING, "#f55b5b")
                return
            
            with open(self.file_path, "rb") as file: 
                global data
                data = pickle_load(file)
            
            for macro_name in data.keys(): 
                mainUI.delete_CB.addItem(macro_name)
                mainUI.start_CB.addItem(macro_name)
                editUI.setMacro_CB.addItem(macro_name)
            
            global load_status
            load_status = True

            self.logging_signal.emit(f"data: \n{data}", DEBUG)                # Test code / please delete this line.

            self.logging_with_color_signal.emit("데이터를 불러오는데 성공했습니다.", INFO, "#4491fa")
        except: 
            exc_type, exc_value, exc_traceback = sys.exc_info()
            formatted_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback)
            self.logging_with_color_signal.emit(f"아래의 오류가 발생했습니다.\n{''.join(formatted_traceback)}", ERROR, "#f55b5b")

        ### ----- loadData() end ----- ###



    def addNewMacro(self) -> None: 
        if load_status == False: 
            self.logging_with_color_signal.emit("아직 매크로 데이터를 불러오지 않았습니다.", WARNING, "#f55b5b")
            return

        macro_name = mainUI.addNewMacro_LE.text()
        mainUI.addNewMacro_LE.clear()

        if macro_name == '': 
            self.logging_with_color_signal.emit("공백은 매크로 이름으로 사용할 수 없습니다.", WARNING, "#f55b5b")
            return

        if macro_name in data.keys(): 
            self.logging_with_color_signal.emit("이미 존재하는 매크로 이름입니다.", WARNING, "#f55b5b")
            return

        data[macro_name] = deque()

        mainUI.delete_CB.addItem(macro_name)
        mainUI.start_CB.addItem(macro_name)
        editUI.setMacro_CB.addItem(macro_name)

        with open(self.file_path, 'wb') as file: 
            pickle_dump(data, file)
        
        self.logging_with_color_signal.emit("새로운 매크로를 추가했습니다.", INFO, "#4491fa")

        ### ----- addNewMacro() end ----- ###
    


    def deleteMacro(self) -> None: 
        if load_status == False: 
            self.logging_with_color_signal.emit("아직 매크로 데이터를 불러오지 않았습니다.", WARNING, "#f55b5b")
            return
        
        if not data: 
            self.logging_with_color_signal.emit("삭제할 매크로가 없습니다.", WARNING, "#f55b5b")
            return
        
        target_index = mainUI.delete_CB.currentIndex()
        target_name = mainUI.delete_CB.currentText()

        mainUI.delete_CB.removeItem(target_index)
        mainUI.start_CB.removeItem(target_index)
        editUI.setMacro_CB.removeItem(target_index)

        del data[target_name]

        with open(self.file_path, 'wb') as file: 
            pickle_dump(data, file)

        self.logging_with_color_signal.emit("매크로를 삭제했습니다.", INFO, "#4491fa")

        ### ----- DataProcessor() end ----- ###




class MacroProcessor(QObject): 
    logging_signal = Signal(str, int)
    logging_with_color_signal = Signal(str, int, str)

    pass                # Test code / please delete this line.

    ### ----- MacroProcessor() end ----- ###




class StopKeyListener(QObject): 
    logging_signal = Signal(str, int)
    logging_with_color_signal = Signal(str, int, str)
    
    pass                # Test code / please delete this line.

    ### ----- StopKeyListener() end ----- ###
        




if __name__ == "__main__": 
    launch()