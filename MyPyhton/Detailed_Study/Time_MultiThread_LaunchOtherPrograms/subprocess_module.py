# Python program can start other programs on your computer with the Popen() function in the built-in subprocess module
# Unlike threads, a process cannot directly read and write another process’s variables
# pass the program’s filename to subprocess.Popen().
# (On Windows, right-click the application’s Start menu item and select Properties to view the application’s filename

# Popen() returns object that has two useful methods: poll() and wait()
# The poll() method will return None if the process is still running at the time poll() is called
# The wait() method will block until the launched process has terminated
# The return value of poll()/wait() is the process’s integer exit code. 0 for success and non 0 for errors
# poll returns None if teh process is still running


import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')

 calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
calcProc.poll() == None  # True : process is still running
# close the process and check following
calcProc.wait()   # 0 ;process terminates without error
calcProc.poll()   # 0 ; process terminates without error


# ============================Passing Command Line Arguments to Popen()
# pass a list as the sole argument to Popen().
# The first string in this list will be the executable filename of the program you want to launch.
# all the subsequent strings will be the command line arguments to pass to the program when it starts.
# In effect, this list will be the value of sys.argv for the launched program.

subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
# <subprocess.Popen object at 0x00000000032DCEB8>
# This will not only launch the Notepad application but also have it immediately open the C:\hello.txt file.



# ============================Opening Websites with Python
# The webbrowser.open() function can launch a web browser from your program to a specific website, rather than opening the browser application with subprocess.Popen()


# ===========================Running Other Python Scripts
# You can launch a Python script from Python just like any other application.
# You just have to pass the python.exe executable to Popen() and the filename of the .py script you want to run as its argument
# Ex :
subprocess.Popen(['C:\\python\\python37\\python.exe', 'hello.py'])

# Unlike importing the Python program as a module, when your Python program launches another Python program,
# the two are run in separate processes and will not be able to  share each other’s variables.



# ======================================== Opening Files with Default Applications
# Double-clicking a .txt file on your computer will automatically launch the application associated with the .txt file extension.
# Your computer will have several of these file extension associations set up already. Python can also open files this way with Popen().
# Each operating system has a program that performs the equivalent of double-clicking a document file to open it.
# On Windows, this is the start program. On OS X, this is the open program, On Ubuntu Linux this is the see program
# pass 'start', 'open', or 'see' to Popen() depending on your operating system:
fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()

# Popen() command to open the file
subprocess.Popen(['start', 'hello.txt'], shell=True) # shell=True is required in windows only