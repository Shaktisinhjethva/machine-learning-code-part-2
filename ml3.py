# dataframes
# [1] creating DataFrames from numpy array
# default column heading
import numpy as np 
import pandas as pd
a=np.array([[1,2,3],[4,5,6]])
df=pd.DataFrame(a)
print(df)
