
import pandas as pd
df = pd.read_csv('orders.csv')
df['profit_flag'] = 1
print(df.head(10))
df.loc[df['profit'] < 0, 'profit_flag'] = 0 #This will update profit_flag column to 0 for all rows where profit is less than 0.
print(df.head(10))

df['profit_loss'] = 'loss'
df['sales_amount_percentage'] = 0
df.loc[(df['profit'] > 0) & (df['profit'] < 50), 'profit_loss'] = 'low profit'
df.loc[df['profit'] > 50 , 'profit_loss'] = 'high profit' 
df.loc[df['profit'] < 0, 'profit_loss'] = 'loss' 
print(df)
df_category_len = df['category'].apply(len) #This will return a series with the length of each category value.
#Similarly we can create function and apply
def sales_amount_pecentage(sales):
    return sales/df['sales'].sum()*100
df['sales_amount_percentage'] = df['sales'].apply(sales_amount_pecentage)
print(df.head(10))
