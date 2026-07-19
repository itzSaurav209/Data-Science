import pandas as pd

data={
    "Name":['Saurav Shukla','ram manohar', 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,22,157,23,21,45,34,56],
    "salary":[10000,50000,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,56,78,34,56,76,55,65]
}
df=pd.DataFrame(data)

#ab ham log print karenge particular columns 
print("sample dataframe")
print(df)
print("names (single column return series)")
#selecting particular columns 
name=df['Name']
print(name)

# selecting multiple columns
subset=df['Name','salary']
print(subset)