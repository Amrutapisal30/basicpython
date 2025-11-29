# A=[1 2]
# B=[1 2
#    3 4   
#]

# 1  2 ==1rs apple  2 rs jerry

  #                        mon   tues
# 		1     2
# 		3     4


# 1*1+2*3=1+6=7  monday sales
# 1*2 + 2*4=2+8=10  tuesday sales

#7  10
#matrix multiplication
import numpy as np  
# array1=np.array([[1,2]])  
# array2=np.array([[1,2],[3,4]])  
# result=np.dot(array1,array2)  
# print(result) #[[ 7 10]]
# # 1*1+2*3=1+6=7  
# # 1*2 + 2*4=2+8=10

a1=np.array([[1,2],[3,4]])
a2=np.array([[10,20],[30,40]])
re=np.vdot(a1,a2)
print(re)
#1*10+2*20+3*30+4*40
#10+40+90+160=300