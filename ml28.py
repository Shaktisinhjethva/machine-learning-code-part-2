# create csv file for following data 

import pandas as pd
dct={'country':['india','Usa','japan'],'GDP':[120,100,200]}
df=pd.DataFrame(dct)
df.to_csv('gdp.csv',index=False)