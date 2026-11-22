import pandas as pd
df = pd.read_csv('orders.csv')
df.sort_index(ascending=False, inplace=True) #This will sort the dataframe based on index in descending order
print(df.head(10))
df.sort_values('sales', ascending=True, inplace=True) #This will sort the dataframe based on sales in ascending order
print(df.head(10))
#We can aslo sort based on multiple columns. In this case, we will sort based on sales and profit in ascending order.
df.sort_values(['sales', 'profit'], ascending=[False, False], inplace=True)
print(df)
#df.reset_index(inplace=True) This will reset the index to default index and order_identifier will become a column again.
