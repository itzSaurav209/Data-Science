import pandas as pd
# ham purana data bhi le skte the lekin hame jo answer milti vo abhut bado milti j ki hame smjh me na aata 
#isliye hamne naya data banaya hai dictinary k help se 
data={
    "Name":['Saurav Shukla','ram manohar', 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,22,157,23,21,45,34,56],
    "salary":[10000,50000,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,56,78,34,56,76,55,65]
}
df=pd.DataFrame(data)

print ("all the descriptive analysis of this data set")
print (df.describe())