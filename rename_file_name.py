import os
class Rename(object):
    def change_filename():
        file_details = {"driller_1": "ASD14", "cutter_1":"ZXC34", "driller_2":"ERTY09" , "cutter_2":"BNM98"}
        #basepath = '/home/nithin/hawaui/Documents'
        with os.scandir('/home/nithin/hawaui/Documents')as filenames:
            for filename in filenames:
                if filename.is_file():
                    print("why it is not printing")
                    print(filename)
                    for key, value in file_details.items():
                        if filename == key:
                            filename= filename.replace(key, value)
                            print(filename)
        return filename                
             


Rename()
#change_filename()

"""
import os

# List all files in a directory using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)





        listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
""" 







