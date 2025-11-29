import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convert student names into a Dataframe
df = pd.DataFrame(students)

print(df)

df=df.rename(columns={"firstname":"fname","lastname":"lname"})

print(df)
