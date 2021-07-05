
# if the specified path is a directory then  
# 'IsADirectoryError' error will raised  
    
# Similarly if the specified file path does not exists or   
# is invalid then corresponding 'OSError' will be raised




# Python program to explain os.remove() method
	
# importing os module
import os
	
# path
path = './RemoveFile_Directory/RemoveDir'
	
# Remove the specified
# file path
try:
	os.remove(path)
	print("% s removed successfully" % path)
except OSError as error:
	print(error)
	print("File path can not be removed")


# os.rmdir() method in Python is used to remove or delete a empty directory. 
# OSError will be raised if the specified path is not an empty directory.