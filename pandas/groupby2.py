import pandas as pd

data={
    "Name":['Saurav Shukla', 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,78,23,21,78,34,23],
    "salary":[10000,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,78,34,56,76,55,65]
}
df=pd.DataFrame(data)
print (df)

#just make group on the basis of age and find the sum of slaary and now we are grouping two columns 
grouped=df.groupby(["Age","Name"])["salary"].sum()
print(grouped)