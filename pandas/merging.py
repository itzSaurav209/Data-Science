import pandas as pd 

#cutmer's dataframe
df_customers=pd.DataFrame({
    'customer_id':[1,2,3],
    'name':['Ramesh','Suresh','kalesh']
})

#order dataframe
df_orders=pd.DataFrame({
    'customer_id':[1,2,4],
    'orderamount':[250,450,350]
})

#merge
df_merged=pd.merge(df_customers,df_orders,on="customer_id",how="inner")
print(df_merged)