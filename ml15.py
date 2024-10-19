# to drop column with empty None write Axis for That column
import pandas as pd 
df1=pd.DataFrame({"a":[1,2,3],"b":[4,None,5]})
print(df1)
df2=df1.dropna(axis=1)
print(df2)
