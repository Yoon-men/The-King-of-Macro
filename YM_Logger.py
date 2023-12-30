"""
YM Logger

ver 1.0.0

Import: 
    from YM_Logger import *

Usage: 
    global logger
    logger = init_logger({name of program}, {version of program}, {console log level}, {file log level}, {path to save log file})


~ Mon, Dec 18, 2023 ~

"""

#* ------------------------------------------------------------ *#

import logging

from os import (
    path as os_path, 
    makedirs as os_makedirs
)

from time import (
    strftime as time_strftime
)

#* ------------------------------------------------------------ *#

DEBUG    = logging.DEBUG
INFO     = logging.INFO
WARNING  = logging.WARNING
ERROR    = logging.ERROR
CRITICAL = logging.CRITICAL

#* ------------------------------------------------------------ *#


def init_logger(program_name: str, version: str, c_level: int, f_level: int, f_path: str = "./log") -> logging.Logger: 
    logger = logging.getLogger(name=program_name)
    logger.setLevel(DEBUG)
    logger.propagate = False

    c_handler = logging.StreamHandler()
    c_handler.setLevel(c_level)
    c_format = logging.Formatter("%(asctime)s [%(version)s | %(levelname)s]\n%(message)s\n", defaults={"version": version})
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)

    if not os_path.isdir(f_path): os_makedirs(f_path)
    f_handler = logging.FileHandler(filename=f"{f_path}/{time_strftime('%Y-%m-%d')}.log", encoding="utf-8")
    f_handler.setLevel(f_level)
    f_format = logging.Formatter("%(asctime)s [%(version)s | %(levelname)s]\n%(message)s\n", defaults={"version": version})
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)

    return logger

    ### ----- init_logger() end ----- ###