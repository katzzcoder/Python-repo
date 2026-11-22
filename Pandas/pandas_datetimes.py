import pandas as pd
df = pd.read_csv('orders.csv')
print(df.dtypes) #All str or numeric
#pd.to_datetime(df['order_date']) #This will give error saying format doesn't match
df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y') #This will convert the order_date column to datetime format.
print(df.dtypes) #order_date column is now datetime format.
#We can extract date, month, year, day, weekday from the datetime column using dt accessor.
df['order_date_day'] = df['order_date'].dt.day
df['order_date_month'] = df['order_date'].dt.month
df['order_date_year'] = df['order_date'].dt.year
print(df[['order_date','order_date_day','order_date_month','order_date_year']])
#Now filtering on date will work on column order_date as it is in datetime format.
df_filtered = df[df['order_date'] > '2020-01-01']
print(df_filtered) #This will give all the rows where order_date is greater than 2020-01-01.