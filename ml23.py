# removing duplicates

import pandas as pd
dl={'acno':[101,102,103,104,105,106,107,104]}
df=pd.DataFrame(dl)
print(df)
df2=df.drop_duplicates()
print(df2)