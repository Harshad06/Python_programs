import pandas as pd

df1 = pd.DataFrame([1,1,1], columns=['id'])
df2 = pd.DataFrame([1,1,1,1], columns=['id'])

print(df1)
print(df2)

df3 = df1.join(df2, lsuffix='_l', rsuffix='_r')
print(df3)

df4 = df2.join(df1, lsuffix='_r', rsuffix='_l')
print(df4)