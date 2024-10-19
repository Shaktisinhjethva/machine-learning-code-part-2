# plotting 
import pandas as pd
import matplotlib.pyplot as plt 
df=pd.read_csv("result1.csv")
df2=df[["jan","feb"]][:3]
print(df2)
df2.plot()
plt.show()