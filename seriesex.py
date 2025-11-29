#1D array -  Series() - data structure
import pandas as pd
data=pd.Series(["john","blake","martin","tiger"])
print(data)
print(data[1]) #blake
print(data[3])#tiger


s=pd.Series(['harsh','aryan','nikhil'],index=['first','second','third'])
print(s)
print(s['second'])#aryan
print(s['third'])#nikhil