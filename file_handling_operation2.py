# create a new file

# file = open("new_file.txt", "x")
# file.close()

# checking if the file exist

import os
print("checking if the file exist")

if os.path.exists("sample.txt"):
    print("removing a file")
    os.remove("sample.txt")
    
else:
    print("file does not exist")
    
    
# creating a file that does not exist
# my_file = open("my_file.txt", "w")
# my_file.write("hi this is mehrish")
# my_file.close()

os.rmdir("my_folder")