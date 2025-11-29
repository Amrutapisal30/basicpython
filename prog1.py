#1D Array 
import numpy as np 
arr1=np.array([10,20,30,40,59,56])
print(arr1)
print(arr1.shape) #(r,) r-no of rows

#2D Array-    it contains row and cols
arr2=np.array([
     [1,2],
     [3,4]
     ])
print(arr2)
print(arr2.shape)#(r,c)  (2, 2)

arr3=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr3)

#3D Array- A 3D array is like multiple 2D Arrays stacked together//(n,r,c)-
#n-no of 2 D array ,r- no of rows ,c-no of cols

arr4=np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[11,22,33]],
    [[4,5,8],[6,7,9]]
])
print(arr4) 

print(arr4.shape)