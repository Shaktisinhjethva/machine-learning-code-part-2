# cleaning empty cell
import pandas as pd
df1=pd.DataFrame({"a":[1,2,None],"b":[3,None,5]})
print(df1)
df2=df1.fillna(0)
print(df2)
