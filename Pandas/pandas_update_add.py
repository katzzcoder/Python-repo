import pandas as pd
df = pd.read_csv('orders.csv')
df['country'] = 'india' #This will add country if not exist or update country column to india if it already exist.
print(df.head(10)) 
df['ship_mode'] = 'regular air' #This will update ship_mode column to regular air for all rows.
print(df.head(10))#Assignment make change in original dataframe. 
#Dropping a column from dataframe. We can use drop method to drop a column from dataframe.
df.drop(columns='profit', inplace=True) #This will drop the country column from the dataframe.
print(df.head(10))
#Dropping multiple columns from dataframe. We can use drop method to drop multiple columns from dataframe.
df.drop(columns=['country','ship_mode']) #This will drop the country and ship
#Calculate avg of sales and add new column as avg
df['avg_sales'] = df['sales'].mean() #This will calculate the average of sales and add a new column avg_sales to the dataframe.
print(df.head(10))
#Without function we can also calculate avg of sales and add new column as avg
#df['avg_sales'] = df['sales'].sum()/df['sales'].count() 

