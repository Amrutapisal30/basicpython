import pandas
p=pandas.Series(["john","blake","martin"])
print(p)
print(p[0])# john
print(p[2])#martin

data=pandas.Series(["john","blake","martin"],index=["a","b","c"])
print(data)
print(data['a']) #john
print(data['b'])#blake
print(data['c'])#martin