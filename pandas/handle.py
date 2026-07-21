import pandas as pd

data={
    "Name":['Saurav Shukla',None, 'mahatma gandhi','raj','simaran','ghanshyam','aditi','atharvi'],
    "Age":[21,None,157,23,21,78,34,56],
    "salary":[10000,None,40000,780000,1000000,340000,56000,41000],
    "performance score":[80,None,78,34,56,76,55,65]
}
df=pd.DataFrame(data)
print (df)

df.dropna(inplace=True)# tum yaha pe axis=0 aur 1 bhi rakh sakte ho , sirf inplace rakhne se rows aur columns dono delete ho jaa rhi hai jo values missing hai 
print(df)
#hamne upar dataset ke second index pe har jagah none likh diya hai taki jab dropna() vala method chale to second index ki sari values delete ho jaye 