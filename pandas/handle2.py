import pandas as pd

data={
    "Name":['Saurav Shukla','attu', 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,None,157,23,21,78,34,56],
    "salary":[10000,None,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,None,78,34,56,76,55,65]
}
df=pd.DataFrame(data)
print (df)


#now we will fill 1 inplace of missing values with the help of fillna()
#df.fillna(1,inplace=True)
#print(df)


#now we want that mean value aa jaye  jaha jaha mssing vakue hai column ke hisab se 
df['Age']=df['Age'].fillna(df['Age'].mean())
df['salary']=df['salary'].fillna(df['salary'].mean())
print(df)
