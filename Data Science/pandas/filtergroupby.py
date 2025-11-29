import pandas

data={

    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}

dataframe=pandas.DataFrame(data)
print(dataframe)

result=dataframe.groupby("department").filter(lambda record:record["salary"].sum()<4000)

print(result)