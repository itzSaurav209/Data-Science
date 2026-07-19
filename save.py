# ab ham log khud ka apna data banayenge in the dictionary aur usko ek dataframe me store  karayenge aur use ham read karenge then use ham csv file bana denge with the help of built in methods  
import pandas as pd

data={
    "Name":['Saurav Shukla','ram manohar', 'mahatma gandhi'],
    "Age":[21,22,157],
    "city":['Prayagraj','bihar','porbandar']
}        #here is our dictionary has been created in which w have store our data set 

#now we will create the data fram of the particular dataset and store in the df 

df=pd.DataFrame(data)
# now print the data
print(df)


#now we will convert this dataframe into csv file with the help of to_csv("file_name")
#df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)