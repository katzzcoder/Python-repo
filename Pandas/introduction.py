import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],'age': [25, 30, 35, 40],'salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print(df)
df = pd.read_csv('orders.csv') #If header is missing give header =None to consider data from 1st row itself
#print(df.head(10))
#print(df.tail(10))
print(df.info())
print(df.dtypes)
print(df.describe())
print(df.columns) #This is used to change the column name
df.columns =['order_identifier', 'order_date', 'ship_date', 'ship_mode', 'customer_id',
       'region', 'product_id', 'category', 'sales', 'quantity', 'profit']
#Or we can use rename, df.rename(columns={'order_id':'order_identifier','region':'rgn'}, inplace=True)
print(df.columns)
print(['order_identifier', 'order_date'])
col = ['order_identifier', 'order_date']
df_new = df[col] #This will create new datafram
print(df_new.dtypes)
df1=df['order_identifier']
print(df1)
print(df['order_identifier']) #print(df.order_identifier) does same thing.Called series.
print(type(df1)) # series type: dataframe with 1 column is called series
#df.iloc and df.loc are used to access rows and columns in a dataframe. iloc is used for integer-location based indexing
# (Last limit not included),while loc is used for label-based indexing(Last limit included).
print(df.iloc[0:5]) #This will print first 5 rows
print(df.loc[0:4]) #same as above
print(df.iloc[[2,4,6],3:6]) #This will row 2,4,6 and column 3,4,5
print(df.iloc[2:5,3:6]) #This will print row 2,3,4 and column 3,4,5

#Loc is useful beacuse we can give column names instead of index number. 
# This is useful when we have large dataframes and we don't know the index number of the column.
print(df.loc[2:5,['ship_mode','customer_id']]) #This will print row 2,3,4,5 and column ship_mode and customer_id
df.set_index('order_identifier', inplace=True) #This will set the index of the dataframe to order_identifier column
#This helps to pull data based on the order_identifier instead of row_number because we will not know  the row_number for a particular order_identifier.
print(df.loc['CA-2020-152156'])
#You can also give column range in above.
print(df.loc['CA-2020-152156','order_date':'ship_mode']) #will give order_date, ship_date and ship_mode for given order_identifier
#You can select specific columns by giving column names in a list.
print(df.loc['CA-2020-152156',['order_date','region']]) #will give order_date and region for given order_identifier
print(df.reset_index(inplace=True)) #This will reset the index to default index and order_identifier will become a column again.
#You can also use df.reset_index(drop=True, inplace=True) to reset the index and drop the old index.
# Because only using reset_index will create a new column with old index values. drop=True will drop the old index column.