# creating CSV file with No index

import pandas as pd
dl={'acno':[101,102,103],'balance':[600,900,1100]}
df=pd.DataFrame(dl)
print(df)
df.to_csv('bank.csv',index=False)
