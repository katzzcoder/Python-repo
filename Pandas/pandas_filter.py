import pandas as pd
df = pd.read_csv('orders.csv')
filter_condition1 = df['sales'] > 500 #This will create a boolean series with True for rows where sales is greater than 5000
#and False for rows where sales is less than or equal to 5000.
print(filter_condition1)
print(df.loc[filter_condition1]) #This will return a dataframe with only the rows where sales is greater than 5000.
filter_condition2 = df['region'] == 'South'
df_south = df.loc[filter_condition2] #This will return a dataframe with only the rows where region is South.
print(df_south) #This will return a dataframe with only the rows where region is South.
print(df.loc[df['region'] == 'South', ['order_id','region']])#Selection of clumns based on condition. 
print(df.loc[df['category'] == 'Furniture', 'order_id':'product_id']) #Range of columns
#Multiple conditions can be used to filter the dataframe. 
print(df.loc[filter_condition1 & filter_condition2]) #This ill return a dataframe with only the rows where sales is greater than 5000 and region is South.
#You acn also use or condition to filter the dataframe.
#print(df.loc[filter_condition1 | filter_condition2]) #This will return a dataframe with only the rows where sales is greater than 5000 or region is South.
#Use of ~opposite of codition to filter the dataframe.
print(df.loc[~filter_condition2]) #This will return a dataframe with only the rows where region is not South.