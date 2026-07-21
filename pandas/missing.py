import pandas as pd

data={
    "Name":['Saurav Shukla','ram manohar', 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,22,157,23,21,78,34,56],
    "salary":[10000,50000,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,56,78,34,56,76,55,65]
}
df=pd.DataFrame(data)
print (df)

#now we eil check whther there is a missing number or not in the data set 
print(df.isnull())#deho iska answer false hi aya hai so it means no missing value is there 

#if you want to count how  many missing number are there in the data set then we use sum() with isnull()
print(df.isnull().sum())
