import pandas as pd
df = pd.read_csv('orders.csv')
print(df.head(10))
#We need to convert the column to string type before using str methods as 1 column df is type series and series has str methods.
df['category_length'] = df['category'].str.len()
df['category_upper'] = df['category'].str.upper()
print(df[['category','category_length','category_upper']])
df.drop(columns=['category_length','category_upper'], inplace=True)
print(df.head(10))