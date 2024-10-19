# creating dataframes from another dataframes
# 1st create data dictionary and then create dataframes and then base on dataframes create another dataframes
import pandas as pd
a={"Rollno":[1,2],"Name":["abc","def"]}
b=pd.DataFrame(a)
c=pd.DataFrame(b)
print(b)
print(c)