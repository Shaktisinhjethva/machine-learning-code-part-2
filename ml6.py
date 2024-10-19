# DataFrame from python list
import pandas as pd
data=[["pasta",15],["meggi",12],["pepsi",20]]
df=pd.DataFrame(data,columns=["items","prices"])
print(df)