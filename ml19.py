import pandas as pd
dl={'Acno':[10,102,103,104,105,106],'balance':[6000,None,7000,1500,None,6000],'Branch':['bhuj','anjar','bhuj',None,'ghandhidham','mundra']}
df=pd.DataFrame(dl)
print(df)
df2=df.replace('bhuj','mundra')
print(df2)