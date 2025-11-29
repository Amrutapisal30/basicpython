import pandas


data={

    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}

dataframe=pandas.DataFrame(data)

print(dataframe)

dataframe=dataframe.set_index('name')

print(dataframe)


departmentname=dataframe.loc["rahul"]["department"]

print("department name of rahul is ",departmentname)

alldetails=dataframe.loc["rahul"]

print("alldetails of rahul are /n",alldetails)