import pandas as pd 

#cutmer's dataframe
df_customers=pd.DataFrame({
    'customer_id':[1,2],
    'name':['Ramesh','Suresh']
})

#order dataframe
df_orders=pd.DataFrame({
    'customer_id':[3,4],
    'orderamount':[250,450,]
})

#merge
df_concat=pd.concat([df_customers,df_orders],axis=1,ignore_index=True)
print(df_concat)