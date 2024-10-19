# removing outliers
# remove all account number which has value >= 1000
import pandas as pd
dl={'acno':[101,102,103,104,105,106]}
df=pd.DataFrame(dl)
print(df)
df2=df[df['acno']<1000]
print(df2)
