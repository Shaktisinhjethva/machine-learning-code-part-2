# creating DataFrame from a Dictionary
import pandas as pd
data={"roll no":[1,2,3],"name":["abc","def","ghi"]}
b=pd.DataFrame(data)
print(b)