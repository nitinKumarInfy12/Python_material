#! python3
import os
targetfolder = 'C:\\Users\\kumar\\OneDrive\\Desktop\\Study Material\\Pyhton\\Python_Study\\Python_youtube\\Test'

num = 1
for i in range(100):
    filename = f"Sample{i}.txt"
    if i in (3,15,24,87,69,45,32,45,86,25,49,6,87,52,31):
        continue
    else:
        with open(os.path.join(targetfolder,filename),'w') as f:
            f.write("this is test")


