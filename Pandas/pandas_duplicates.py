#This is smilar to handling null values in dataframe.
import pandas as pd
data = {
    "name": ["Sumit", "Rahul", "Ankit", "Ankit"],
    "age": [25, 30, 30, 30],
    "salary": [25000, 30000, 35000, 35000],
}
df = pd.DataFrame(data)
#df.drop_duplicates(inplace=True) #This will drop the duplicate rows from the dataframe.
print(df)
#By default it deletes last row. We can use keep parameter to keep last row like below
df.drop_duplicates(keep='last', inplace=True)
print(df)

#We can mention column in subset parameter to drop duplicates based on that column only.
df.drop_duplicates(subset='age', keep='last', inplace=True)