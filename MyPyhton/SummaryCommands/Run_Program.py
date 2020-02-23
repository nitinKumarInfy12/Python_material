# Shebang Line

The first line of all your Python programs should be a shebang line, which tells your computer that you want Python to execute this program.
The shebang line begins with #!, but the rest depends on your operating system.
>>>On Windows, the shebang line is #! python3.
>>>On OS X, the shebang line is #! /usr/bin/env python3.
>>>On Linux, the shebang line is #! /usr/bin/python3.

You will be able to run Python scripts from IDLE without the shebang line,
but the line is needed to run them from the command line

# Running Python Programs on Windows
On Windows, the Python 3.4 interpreter is located at C:\Python34\python.exe

# To make it convenient to run your Python program, create a .bat batch file for running the Python program with py.exe.
# To make a batch file, make a new text file containing a single line like the following:
@py.exe C:\path\to\your\pythonScript.py %*


It is recommend you place all your batch and .py files in a single folder, such as C:\MyPythonScripts or C:\Users\YourName\PythonScripts.
The C:\MyPythonScripts folder should be added to the system path on Windows so that
you can run the batch files in it from the Run dialog. To do this, modify the PATHnenvironment variable. 
Click the Start button and type Edit environment variables for your account
select the Path variable and click Edit. In the Value text field,append a semicolon, type C:\MyPythonScripts, and then click OK.
Now you can run any Python script in the C:\MyPythonScripts folder by simply pressing WIN-R and entering the
script’s name. Running pythonScript, for instance, will run pythonScript.bat, which in
turn will save you from having to run the whole command py.exe C:\MyPythonScripts\pythonScript.py from the Run dialog