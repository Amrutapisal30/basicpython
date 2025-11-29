import pandas

data={

    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}


result=pandas.DataFrame(data)

#result.to_csv("ouput.csv")

result.to_csv("output.csv",index=False)