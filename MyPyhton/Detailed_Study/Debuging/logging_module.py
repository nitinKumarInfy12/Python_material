# To enable the logging module to display log messages on your screen as your program runs.
# copy the following to the top of your program (but under the #! python shebang line
# it can always be disable them later by adding a single logging.disable(logging.CRITICAL). it will suppress all log messages at that level or lower
# Logging levels provide a way to categorize your log messages by importance. There are five logging levels
# DEBUG (loging.debug()), INFO (loging.info(), WARNING (loging.warning()), ERROR (loging.error()), CRITICAL (loging.critical())

#! python3
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# if want to write the log in file instead of displaying on screen. add the filername parameter to logging.basicConfig
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')    # prints out 2020-02-08 17:45:09,072 - DEBUG - Start of program

def factorial(n):
    logging.debug(f"Start of factorial({n})")
    total = 1
    for i in range(n + 1):   #for i in range(1, n + 1):    correct as this to correct the code output that we get the idea by looking into the log
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug(f"End of factorial({n})")
    return total

print(factorial(5))
logging.debug('End of program')