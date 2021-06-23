
import pandas as pd 

df = pd.read_csv('./PANDAS/ComputerSales.csv', chunksize=10)
# print(data)

id = 0

for data in df:
    print("Chunk:", id)
    id +=1
    print(data)
