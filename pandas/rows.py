import pandas as pd

df=pd.read_csv("train.csv")

print("print top 10 number of rows")
print(df.head(2))

print("print last 10 number of row ")
print(df.tail(2))