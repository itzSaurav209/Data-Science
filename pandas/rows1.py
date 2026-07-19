import pandas as pd

data={
    "Name":['Saurav Shukla','ram manohar', 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,22,157,23,21,78,34,56],
    "salary":[10000,50000,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,56,78,34,56,76,55,65]
}
df=pd.DataFrame(data)
#here we will do filtration of rows based on single condition and multiple condition 
#ques) aise logo ki information digiye jinki salary 50000 ke upr hai 
high_salary=df[df['salary']>50000]
print("printing the salary which is greter than 50000")
print(high_salary)

#filtering rows salary>50000 and age >30
filtered=df[(df['salary']>50000)& (df['Age']>50)]
print("give me info about those students whose age are above than 30 and salary is more than 50000")
print(filtered)