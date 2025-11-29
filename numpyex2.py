import numpy as np
arr1=np.array([34,23,12,45,67])
print(arr1)
print(arr1.sum())#181

m=np.max(arr1)
print("max  element=",m)#67

n=np.min(arr1)
print("min element=",n)#12

#display array elements in ascending order
b=np.array([56,14,82,17,32])
asc=np.sort(b)
print(asc) #[14 17 32 56 82]

#display array elements in descending orderb=np.array([56,14,82,17,32])
desc=np.sort(b)[::-1]
print(desc)#[82 56 32 17 14]