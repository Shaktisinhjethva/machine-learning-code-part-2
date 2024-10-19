# CSV without index 

import pandas as pd
a={"Acno":[101,102,103],"Balance":[4500,8900,12000]}
b=pd.DataFrame(a)
print(b)
b.to_csv("bob2.csv",index=False)
