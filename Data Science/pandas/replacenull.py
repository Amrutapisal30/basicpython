import pandas

dataframe=pandas.read_csv("C:/python/New folder/pandas/mycsv.csv")

print(dataframe)

#result=dataframe.fillna(0)

result=dataframe.dropna(inplace=True)

# if inplace=True is present then original dataframe will get modified 

print(result)

print("original dataframe\n",dataframe)