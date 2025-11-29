#1D array
import numpy
arr1=numpy.array([10,20,30,40,50])
print(arr1)
print(arr1.shape) #(5,)

arr2=numpy.array(["john","blake","martin"])
print(arr2)

#2D array
a2=numpy.array([
    [1,2,3],
    [5,6,7],
    [7,8,9]
])
print(a2)
print(a2.shape) #(3, 3)
#Multidimensional Array-(n,r,c)  -n- no of arrays r-no of rows c-no of col
n4=numpy.array([
    [[1,2,3],[4,5,6]],
    [[10,20,30],[40,50,60]]
])
print(n4) 
print(n4.shape)#(2, 2, 3)