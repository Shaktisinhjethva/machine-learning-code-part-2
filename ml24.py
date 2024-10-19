# CSV vs TSV

# comma seperated values\
# 1,AJAY,800  
#  2,RAJ,700

# tab seperated values
# 1 AJAY 800
#  2 RAJ 700

# creating CSV file

import pandas as pd
dl={'acno':[101,102,103],'balance':[600,900,1100]}
df=pd.DataFrame(dl)
print(df)
df.to_csv('c:\\bank.csv')