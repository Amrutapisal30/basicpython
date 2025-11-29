import pandas
data={
    "name":["pooja","anuja","rutuja","nisha"],
    "department":["it","comp","comp","it"],
    "salary":[4000,5000,3000,7000]
}
result=pandas.DataFrame(data)
print(result)

#iloc[rowindex,colundex]-
# dataframe iloc property accepts rowindex,colindex and gives value present at it 
print(result.iloc[2,2]) #3000
print(result.iloc[3,1])#it

result=result.rename(columns={"name":"a","department":"b"})
print(result)