'''
[1:01 PM] Agarwal, Nishant-ZA (Guest)
    dict_dfs = {​'A": df1, " B": df2, "C": df3}​
​[1:02 PM] Agarwal, Nishant-ZA (Guest)
    Q1) Get all the keys from above dict in a list.
​[1:02 PM] Agarwal, Nishant-ZA (Guest)
    Q2) Combine all the dfs into one giant df.
​[1:02 PM] Shringi, Harshad
    dict_dfs.keys()
​[1:03 PM] Shringi, Harshad
    dict_dfs.values()
​[1:06 PM] Shringi, Harshad
    df = dict_dfs.values()
​[1:07 PM] Shringi, Harshad
    pd.to_excel

[1:08 PM] Agarwal, Nishant-ZA (Guest)
    Code #2 : Convert Pandas dataframe column type from string to datetime format.
import pandas as pd
df = pd.DataFrame({​​​​​​​'Date':['11/8/2011', '04/23/2008', '10/2/2019'],
'Event':['Music', 'Poetry', 'Theatre'],
'Cost':[10000, 5000, 15000]}​​​​​​​)
df.info()
​[1:09 PM] Shringi, Harshad
    Date, Event, Cost
​[1:09 PM] Shringi, Harshad
    object type
​[1:11 PM] Shringi, Harshad
    obj,obj,int

[1:11 PM] Agarwal, Nishant-ZA (Guest)
    The data type of the ‘Date’ column is object i.e. string. You need to convert it to datetime format
​[1:12 PM] Shringi, Harshad
    df['New_Date'] = pd.to_datetime['Date']

[1:13 PM] Agarwal, Nishant-ZA (Guest)
    Q) Create a class to add or subtract a day from a date. Do not use python's inbuilt datetime module
​[1:19 PM] Shringi, Harshad
    d.split('/')
​[1:20 PM] Shringi, Harshad
    lst[0]
​[1:20 PM] Shringi, Harshad
    def find(lst[0]):
'''