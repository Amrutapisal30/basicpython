import numpy as np  
dtype = [('name', 'S10'), ('height', float), ('age', int),('gender','S10')]  
values = [('Shubhamrrrrropiuyuu', 5.9, 43, 'M'), ('Arpita', 5.6, 23, 'F'),('Vaishali', 5.2, 30, 'F')]  
x=np.array(values, dtype=dtype)  
print(x)  
y=np.sort(x, order='age')  
print(y)  
