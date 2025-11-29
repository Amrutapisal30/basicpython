import numpy as np  
a = np.array([[100,200],[23,12]])  
b = np.array([[10,20],[12,21]])  
vdot = np.vdot(a,b)  
print(vdot)  

# 100 *10 + 200 * 20 + 23 * 12 + 12 * 21 = 5528