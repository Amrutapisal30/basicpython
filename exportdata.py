import pandas
data={
    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}
result=pandas.DataFrame(data)
print(result)

result.to_csv("emp.csv")
