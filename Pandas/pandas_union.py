import pandas as pd
emp1 = {
    "id": [1, 2, 3],
    "name": ["Ankit", "Sumit", "Amit"],
    "salary": [100, 200, 300]
}

emp2 = {
    "id": [4, 5, 6],
    "name": ["Nachiket", "Rahul", "Vinay"],
    "salary": [400, 500, 600]
}

df1 = pd.DataFrame(emp1)
df2 = pd.DataFrame(emp2)
# Unioning the two dataframes
df_union = pd.concat([df1, df2], ignore_index=True)
print(df_union)