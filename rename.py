import os 
import shutil
import fnmatch
import glob
import re 
class Rename(object):

    def move_file(self):
    
        self.source_name = '/home/nithin/toolname_description'
        self.destination_name = '/home/nithin/tool_name'
        self.values_collection = []
        self.keys_collection = []
       
        files = glob.iglob(os.path.join(self.source_name, "*.ctx"))
        for file in files:
            shutil.copy2(file, self.destination_name)
        filenames = glob.iglob(os.path.join(self.destination_name, "*.ctx"))
        with open('file_new.ctx', 'w') as tmp:
            for filename in filenames:
                with open(filename) as ctxfile:
                    for row in ctxfile:
                        tmp.write(row)               
        
        with open('file_new.ctx', 'r')as ourfile:
            for line in ourfile:
                description = re.search('<Attribute name="Description">(.+?)</Attribute>', line)
                name = re.search('<Attribute name="Name">(.+?)</Attribute>', line)
                
                if name:
                    key = name.group(1)
                    self.keys_collection.append(key)
                    
            
                if description:
                    
                    value = description.group(1)
                    self.values_collection.append(value)
                           
    def output(self):   
        finish = '/home/nithin/tool_description'
        imp_dict = {key:value for key, value in zip(self.keys_collection, self.values_collection)}
        
        files = os.listdir(self.destination_name)
        for file, value in zip(files, self.values_collection):
            current_file = os.path.join(self.destination_name , file)
            future_file = os.path.join(finish, value + '.ctx') 
            new_file = os.rename(current_file, future_file)
            print(new_file)

        files = glob.iglob(os.path.join(self.source_name, "*.ctx"))
        for file in files:
            shutil.copy2(file, self.destination_name)           


obj = Rename()
obj.move_file()
obj.output()



   































































































































































                    
                    
                    




                
            
                    
                    
                   
                    

              
             
                                      
















      













