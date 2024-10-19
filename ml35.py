import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

plt.plot([1,2,3,4],[1,4,2,3],color='red',linestyle='--',marker='o',label='Data')
plt.annotate('HighSide',xy=(2,4),xytext=(2,5),arrowprops=dict(facecolor='black',arrowstyle='->'))
circle = Circle((2,4), 0.4, facecolor='blue', alpha=0.5)
plt.gca().add_patch(circle)
plt.title("graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()

