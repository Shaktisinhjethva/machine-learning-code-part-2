# remove marks which has value <0 and >50 because paper has maximum marks 50
import pandas as pd
dl={'balance'[34,0,14,56,40,334,32,0,81]}
df=pd.DataFrame(dl)
print(df)
df2=df[(df['marks']>=0 & df['marks']<=50)]
print(df2)