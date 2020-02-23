# Rather than having all of your code wait until the time.sleep() function finishes, you can execute the delayed or scheduled code in a separate thread using Python’s threading module.
import time, datetime, threading
startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)
print('Program now starting on Halloween 2029')
# --snip--


# To make a separate thread, you first need to make a Thread object by calling the threading.Thread() function.
print('Start of program.')
def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)  # target=takeANap ; This means the function we want to call in the new thread is takeANap()
# Notice that the keyword argument is target=takeANap, not target=takeANap().
# This is because you want to pass the takeANap() function itself as the argument, not call takeANap() and pass its return value.

threadObj.start() # creates the new thread and start executing the target function in the new thread
print('End of program.')

"""output of teh program 
Start of program.
End of program.
Wake up!

# The reason Wake up! comes after it is that when threadObj.start() is called, the target function for threadObj is run in a new thread of execution. 
This program has two threads.
The first is the original thread that began at the start of the program and ends after print('End of program.'). 
The second thread is created when threadObj.start() is called, begins at the start of the takeANap() function, and ends after takeANap() returns

A Python program will not terminate until all its threads have terminated.
When you ran thi sprogram, even though the original thread had terminated, the second thread was still executing the time.sleep(5) call.

"""
# ======================passing arguments to the thread functions ====================================================
# When passing arguments to a function in a new thread, use the threading.Thread() function’s args an kdwargs keyword arguments
# The regular arguments can be passed as a list to the args keyword argument in threading.Thread().
# The keyword argument can be specified as a dictionary to the kwargs keyword argument in threading.Thread()

# ex : print()
print('Cats', 'Dogs', 'Frogs', sep=' & ')
# prints Cats & Dogs & Frogs

# the print() can be called in thread() with argumantes as
hreadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()
# prints Cats & Dogs & Frogs

# threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))   is teh incorrect way.it will throw error. args and kwargs has to be used to pass parameteres

# Calling a Thread object’s join() method will block until that thread has finished.
# By using a for loop to iterate over all the Thread objects in the downloadThreads list,
# the main thread can call the join() method on each of the other threads.
downloadThreads = []
def downloadXkcd(start, end):
    # -- code snipet--
    print("code")
for i in range(0, 1400, 100): # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()print('Done.')

print("Done")
