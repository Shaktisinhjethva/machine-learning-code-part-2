# DataFrame with User defined index
import pandas as pd
d={"A":[1,2,3],"B":[6,7,8]}
df=pd.DataFrame(d,index=["row 1","row 2","row 3"])
print(df)