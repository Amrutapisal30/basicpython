import pandas

data={"rollno":[1,2],"name":["sachin","ramesh"]}

firstdataframe=pandas.DataFrame(data)


data={"rollno":[1,2],"marks":[90,70]}

seconddataframe=pandas.DataFrame(data)

mergeresult=firstdataframe.merge(seconddataframe)

print(mergeresult)