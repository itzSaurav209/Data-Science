import pandas as pd

data={
    "Name":['Saurav Shukla','ram manohar', 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,22,157,23,21,78,34,56],
    "salary":[10000,50000,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,56,78,34,56,76,55,65]
}
df=pd.DataFrame(data)
print (df)

print("             ")
#here we are sorting single column only 
df.sort_values(by='Age',ascending=True,inplace=True)
print ("after sorting")
print(df)