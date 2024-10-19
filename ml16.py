# print frist few row and last row with head and tail function
import pandas as pd
dl={'Acno':[101,102,103,104,105,106],'Balance':[6000,None,7000,1500,4500,6000]}
df=pd.DataFrame(dl)
print(df)

# print 1 and 2 rows
print(df.head(2))
# print last 3 rows
print(df.tail(3))
 
#  output
#    Acno  Balance
# 0   101   6000.0
# 1   102      NaN
# 2   103   7000.0
# 3   104   1500.0
# 4   105   4500.0
# 5   106   6000.0
#    Acno  Balance
# 0   101   6000.0
# 1   102      NaN
#    Acno  Balance
# 3   104   1500.0
# 4   105   4500.0
# 5   106   6000.0
