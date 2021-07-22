
import pandas as pd

df1 = pd.DataFrame([1,1], columns=['col_A'] )
#print("DataFrame #1: \n", df1)

df2 = pd.DataFrame([1,1,1], columns=['col_A'] )
#print("DataFrame #2: \n", df2)

df3 = pd.merge(df1, df2, on='col_A', how='inner')
print("DataFrame after inner join: \n", df3)



# Output:    2x3 --> 6 times it will be printed. [one-many operation] 
# It maybe any type of join ---> inner/outer/right/left  
'''
DataFrame after inner join: 
    col_A
0      1 
1      1 
2      1 
3      1 
4      1 
5      1
'''


# In case where any df data is "NaN" or "None", then value will be empty column- 
# df1 = pd.DataFrame([NaN, NaN], columns=['col_A'] )
'''
DataFrame after inner join: 
 Empty DataFrame
Columns: [col_A]
Index: []       
'''
