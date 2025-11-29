import pandas

data={

   'float':[1.0],
   'int':10,
   'string':["python"],
   'datetime':[pandas.Timestamp('20241014')]
}

result=pandas.DataFrame(data)

print(result)
print(result.dtypes)