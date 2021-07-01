
# LOC vs ILOC in Pandas: Difference Between LOC and ILOC in Pandas
'''
1) iloc in Python:
    > You can use iloc in Python for selection. 
    > It is integer-location based and helps you select by the position

2) loc in Pandas:
    > You can use loc in Pandas to access multiple rows and columns by using labels.

'''

import pandas as pd

df = pd.read_csv('./PANDAS/ComputerSales.csv')
print(df)

# loc 
print(df.loc[5,"Contact"])     # label based

# iloc
print(df.iloc[5,1])             # integer-location based

# output in both the cases:   # Sally Struthers