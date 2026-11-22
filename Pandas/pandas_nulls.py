import pandas as pd
df = pd.read_csv('orders.csv')
print(df.dropna()) #This will give 3 rows as we have 3 null values
#f.dropna(inplace=True) #This will drop the rows with null values from the dataframe.
print(df.dropna(subset ='category')) # One removed for null category row
print(df.dropna(subset =['category','customer_id'])) # Two removed for null category and customer_id row
#fillna method is used to fill the null values with some value.
#print(df.fillna('unknown')) #This will fill the null values with 'unknown' in the dataframe.
df.fillna('unknown', inplace=True) #This will fill the null values with 'unknown' in the original dataframe 
print(df)
#To spicify columns to fill the null values we can use subset parameter in fillna method.
df[['category','customer_id']].fillna('unknown', inplace=True) 
print(df) #This will fill the null values with 'unknown' in the original dataframe for category and customer_id columns only.
