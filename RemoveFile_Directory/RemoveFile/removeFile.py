
# Python program to explain os.remove() method
	
# importing os module
import os

# File name
file = 'text1.txt'

# File location
location = "./RemoveFile_Directory/RemoveFile"

# Path
path = os.path.join(location, file) 


# Remove the file
# 'text1.txt'
os.remove(path)
print(f'Text File successfully removed')
