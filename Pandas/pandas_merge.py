import pandas as pd
df_orders = pd.read_csv('orders.csv')
df_returns = pd.read_csv('returns.csv')
#We can merge the two dataframes on order_id column using merge method.
df_merged = pd.merge(df_orders, df_returns, on='order_id', how='inner') 
#If joining column names are diffrent in both dataframes then we can use left_on and right_on parameters to specify the joining columns.
#df_merged = pd.merge(df_orders, df_returns, left_on='order_id', right_on='order_id', how='inner')
print(df_merged) 
df_merged_gb = df_merged.groupby('sales').sum()
print(df_merged_gb)
df_merged.to_csv('orders_returns.csv', index=False) #This will save the merged dataframe to a csv file without index.
df_merged.to_json('orders_returns.json', orient='records', index=False) #This will save the merged dataframe to a JSON file without index.
df_merged.to_excel('orders_returns.xlsx', index=False) #This will save the merged dataframe to a excel file without index.