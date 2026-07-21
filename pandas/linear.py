import pandas as pd
data={
    "time":[1,2,3,4,5],
    "values":[10,None,30,None,50]
}
df=pd.DataFrame(data)
print(df)
print("    ")

df['values']=df['values'].interpolate(method="linear")
print(df)