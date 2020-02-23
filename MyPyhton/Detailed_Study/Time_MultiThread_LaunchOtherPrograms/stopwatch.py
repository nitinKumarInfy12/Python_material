#! python3

# a simple stopwatch program

import time


# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1


# TODO: Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        #print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        #print("Pretty format")
        lap = 'lap # {} {} ({})'.format((str(lapNum)+ ':').ljust(3),
                                         str(totalTime).rjust(5),
                                         str(lapTime).rjust(6))
        print(lap, end='')

        """ Since the user pressing ENTER for the input() call will print a newline to the screen,
        pass end='' to the print() function to avoid double-spacing the output."""
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')


