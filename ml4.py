# column name as per user choice
import numpy as np
import pandas as pd
a=np.array([[1,2,3],[4,5,6]])
b=pd.DataFrame(a,columns=['A','B','C'])
print(b)