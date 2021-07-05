
# Python program to explain os.remove() method
	
# importing os module
import os

# File name
file = 'file1.csv'

# File location
location = "./RemoveFile/"

# Path
path = os.path.join(location, file) 


# Remove the file
# 'file1.csv'
os.remove(path)
print(f'CSV File successfully removed')
