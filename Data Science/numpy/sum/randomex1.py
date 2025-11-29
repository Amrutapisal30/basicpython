import numpy as np  
a=np.random.randint(3,size=10)  
print(a) 

b=np.random.randint(15,size=(7,3))
print(b)

b = np.random.randint(5, 15, size=7, dtype=np.int64)  
print(b)  
print(b.dtype)  # int64

# If you actually want floats between 5 and 15, use uniform instead:

b = np.random.uniform(5, 15, size=7)
print(b)
print(b.dtype)  # float64