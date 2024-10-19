# pandas plotting
# frist create rresult .csv file 

import pandas as pd 
dct={'jan':[200,300,120],'feb':[400,550,230]}
df=pd.DataFrame(dct)
df.to_csv("result1.csv",index=False)
