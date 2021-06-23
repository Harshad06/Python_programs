
# importing pandas as pd
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					'Cost':[10000, 5000, 15000, 2000]})

# Print the dataframe
# print(df)

df['Flag'] = df.apply(lambda row: True if row.Cost>5000 else False, axis=1)
# print(df)

df['Amount'] = df.apply(lambda row: row.Cost if row.Cost>5000 else None, axis=1)
print(df)
