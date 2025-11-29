import pandas

data={

    "name":["sachin","sachin","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,1000,3000,4000]
}

dataframe=pandas.DataFrame(data)

result=dataframe.drop_duplicates()

print(result)