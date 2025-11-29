import pandas
data={
    "name":["sachin","rahul","virendra","sourav"],
    "department":["it","it","comp","comp"],
    "salary":[1000,2000,3000,4000]
}
df=pandas.DataFrame(data)
#print(df)

#select name from emp;
#coldata=df.filter(items=["name"])
#print(coldata)

#select salary from emp;
#coldata1=df.filter(items=["salary"])
#print(coldata1)

#to display employee whose salary is greater than 2000
greatersal=df[df['salary']>2000]   #select *from emp where salary>2000
print(greatersal)

#to display emp whose salary is greater than 1000 and department is 'it'
cond=df[(df['salary']>1000)   &  (df['department']=='it')]
 #select *from emp where salary>1000 and department='it'

print(cond)

#select *from emp order by name;
asc=df.sort_values(by="name")
print(asc)





