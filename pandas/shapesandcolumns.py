
#here we are using the attributes named as shapes and columns 
import pandas as pd 
data={
    "Name":['Saurav Shukla','ram manohar', 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,22,157,23,21,45,34,56],
    "salary":[10000,50000,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,56,78,34,56,76,55,65]
}
df=pd.DataFrame(data)
print(f'no of rows and columns:{df.shape}')
print(f'column names:{df.columns}')