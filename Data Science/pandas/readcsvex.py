import pandas

dataframe=pandas.read_csv("C:/python/New folder/pandas/mycsv.csv")

#print(dataframe)

first2rows=dataframe.head(2)

#print(first2rows)


last2rows=dataframe.tail(2)

print(last2rows)