# create file for plotting
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("gdp.csv")
df2=df[["country","GDP"]][:3]
print(df2)
df2.plot(x="country",y="GDP",kind="line")
plt.title("GDP details")
plt.xlabel("country")
plt.ylabel("GDP in Rs.(crores)")
plt.show()