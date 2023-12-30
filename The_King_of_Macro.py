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

## PySide2 Moduels
from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtCore import QThread, QCoreApplication, QObject, Qt, Signal

## User-defined Modules
from YM_Logger import (
    init_logger, 
    DEBUG, INFO, WARNING, ERROR, CRITICAL
)
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
    pass                 # Test code / please delete this line.



if __name__ == "__main__": 
    pass                # Test code / please delete this line.