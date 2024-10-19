# Handling missing value 
# Fillna() method 

import pandas as pd
dl={'marks':[34,0,None,56,40,None,32,0,81]}
df=pd.DataFrame(dl)
print(df)
df2=df.fillna(0)
print(df2)
