'''
# if delimiter given- 
df = pd.read_csv(r'alignmnent.txt', sep='\t')


# 3 cols from a df and a common col from another df, apply merge operation-
dataset_1 = call_plan.merge(alignment[['base_functerrid','teamname','base_geoname']], how = 'left', 
                            left_on = 'func_territory_id', right_on = 'base_functerrid')


# convert str to int dtype-
dataset_1['annualcalls'] = dataset_1['annualcalls'].astype(int)
'''