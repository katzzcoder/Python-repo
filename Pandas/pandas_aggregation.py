
import pandas as pd
df = pd.read_csv('orders.csv')
print(df['sales'].max()) #This will return the maximum value of sales column in the dataframe.
print(df['sales'].min()) #This will return the minimum value of sales column in the dataframe.
print(df['sales'].mean()) #This will return the mean value of sales column in the dataframe.
print(df['sales'].sum()) #This will return the sum of all values in the sales column in the dataframe.
print(df['category'].count()) #This will return the count of all values in the categories column in the dataframe.
print(df['category'].nunique()) #This will return the count of unique values in the categories column in the dataframe. 
print(df['category'].unique()) #This will return the unique values in the categories column in the dataframe.
print(df['category'].value_counts()) #This will return the count of each unique value in the categories column in the dataframe.
print(df.groupby('category')['sales'].sum()) #This will return the sum of sales for each unique value in the categories column in the dataframe.
#We can combine aggregation functions with groupby method to get the required result.
print(df.groupby('category')['sales'].agg(['sum','mean','max','min'])) 
#We can get different aggregation functions for different columns using agg method.
print(df.groupby('category').agg({'sales':['sum','mean'],'profit':['sum','count']})) #This will return the sum and mean of sales and profit for each unique value in the categories column in the dataframe.
print(pd.pivot_table(df, index='category', columns='region',values='sales', aggfunc=['sum','mean'],fill_value=0)) #This will return the sum, mean, max and min of sales for each unique value in the categories column in the dataframe.