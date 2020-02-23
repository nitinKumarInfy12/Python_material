#! pyhton3
# traceback details froom teh call stack can be obtained in file or so using teh traceback module
# traceback.format_exc() converts teh traceback detals into string


import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc()) # traceback info gets writtenn in the file
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')


print ("program continued followig exception")
