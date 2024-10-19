import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

plt.plot([1,2,3,4],[1,4,2,3],color='red',linestyle='--',marker='o',label='Data')
plt.annotate('HighSide',xy=(2,4),xytext=(2,5),arrowprops=dict(facecolor='black',arrowstyle='->'))
rect=patches.Rectangle((1,8,3,8),0.5,0.5,facecolor='blue',alpha=0.5)
plt.gca().add_patch(rect)
plt.title("graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")    
plt.legend()
plt.grid(True)
plt.show()