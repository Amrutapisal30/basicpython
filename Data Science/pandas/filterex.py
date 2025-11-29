import pandas


data={

    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}

dataframe=pandas.DataFrame(data)

selectecolumnsdata=dataframe.filter(items=["name","salary"])
print(selectecolumnsdata)

filterbasedoncondition=dataframe[dataframe["salary"]>2000]

print(filterbasedoncondition)

sortedresult=dataframe.sort_values(by="name")

print(sortedresult)
