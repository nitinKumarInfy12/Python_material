
# ===================debuging with exceptions========================
# custom exceptions by raiing Exception and catching in except block 
try-except-else-finally


# ============================Traceback==============================
# traceback.format_exc() of traceback module
This allows to get the traceback info from teh call stack into file or string
for this needd to import tracebck module


# ============================Assertion===============================
using Assert keyword with condition, value when the condition is false
this exception must not be caught in the try-except block

# ============================Logging================================
# logging module, must be imported after the python shebang
# these 2 lines of code must be in the begging of tehprogram
#! python3
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# if want to write the log in file instead of displaying on screen. add the filername parameter to logging.basicConfig
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# then logging.debug('Start of program')/ logging.debug('End of program') type of logs can be used according to loging function selected
# logging levels/functions are 5 types. DEBUG (loging.debug()), INFO (loging.info(), WARNING (loging.warning()), ERROR (loging.error()), CRITICAL (loging.critical())
# it can always be disable them later by adding a single logging.disable(logging.CRITICAL) call. it will suppress all log messages at that level or lower
# log messages are for teh developers not to be used as print(). Print() is for application/user. 
# print() and logging must not be confused



