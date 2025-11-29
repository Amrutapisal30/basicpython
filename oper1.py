import numpy as np
a=np.array([10,20,30,40,50])
res=np.sum(a)
print(res)

# sum=0
# l=[10,20,30,40,50]

# for i in l:
#     sum=sum+i
# print(sum)

#max- return maximum element
arr1=np.array([56,34,23,12,8,69])
m=np.max(arr1)
print(m) #69

#min--- return minimum element
m2=np.min(arr1)
print(m2)#8


#to isplay Arry elements in ascending order
s=np.sort(arr1)
print(s) #[ 8 12 23 34 56 69]

#to isplay Array elements in descending order
reverse=s[::-1]
print(reverse)#[69 56 34 23 12  8]

print(np.sort(a)[::-1])

r=np.array(sorted(arr1,reverse=True))
print(r)

# sorted()
# np.sort()