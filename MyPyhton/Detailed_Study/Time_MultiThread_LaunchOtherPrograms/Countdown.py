#! python3
# this programs runns for 60 seconds and then sounds alarm

import time, subprocess
import webbrowser

timeLeft = 5

while timeLeft>0:
    print(f"Time Left : {timeLeft}")
    time.sleep(1)
    timeLeft -= 1

# TODO: At the end of the countdown, play a sound file.
#subprocess.Popen(['start', 'alarm.wav'], shell=True)
webbrowser.open('https://www.youtube.com/watch?v=W_9KR3mYkUo&list=PL9Z_KwF-qaztJlEdtO1Kiw-6UKVZbk75I')

