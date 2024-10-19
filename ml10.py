# creating CSV file
# C = comma 
# S =seperate 
# V = value

# craeting CSV file for following Data
 
#  steps to create CSV 
# 1 create dictionary
# 2 create DataFrame
# 3 From Data Frame cerate new CSV file

import pandas as pd
data={"rollno":[1,2],"perc":[70.5,99.9]}
df=pd.DataFrame(data)
print(df)
df.to_csv("result.csv")