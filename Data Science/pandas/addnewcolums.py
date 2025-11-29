import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convert student names into a Dataframe
df = pd.DataFrame(students)

print(df)

df['fullname']=df['firstname'] + " " + df['lastname']

print(df)

df.drop('fullname',axis=1,inplace=True)

print(df)
