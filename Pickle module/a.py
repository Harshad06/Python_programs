import pickle

cars = ["AUDI", "BMW", "KIA"]

file = "mycars.pkl"
fileObj = open(file, 'wb')

pickle.dump(cars, fileObj)
fileObj.close()
