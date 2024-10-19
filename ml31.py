import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,2,3,4],[1,4,2,3],color='red',linestyle='--',marker='o',label='Data')
plt.title("graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()
