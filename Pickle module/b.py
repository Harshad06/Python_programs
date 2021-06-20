import pickle

file = "./Pickle module/mycars.pkl"
fileObj = open(file, 'rb')

mycars = pickle.load(fileObj)
print(mycars)