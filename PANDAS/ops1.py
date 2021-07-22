
# importing pandas as pd
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					 'Cost':[10000, 5000, 15000, 2000]})

# Print the dataframe
# print(df)

# Operation 1 
df['Discounted_Price'] = df.apply(lambda row: row.Cost - (row.Cost * 0.1), axis=1)
print(df)


# Alternatively,
# create a new column
df['Discounted_Price'] = df['Cost'] - (0.1 * df['Cost'])
print(df)