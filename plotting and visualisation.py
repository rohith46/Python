#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:44:19 2018

@author: rohithbharatha
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

market_df=pd.read_csv("/Users/rohithbharatha/Desktop/Session3+-+Categorical+Data+++Time+Series/global_sales_data/market_fact.csv")
product_df=pd.read_csv("/Users/rohithbharatha/Desktop/Session3+-+Categorical+Data+++Time+Series/global_sales_data/prod_dimen.csv")
customer_df=pd.read_csv("/Users/rohithbharatha/Desktop/Session3+-+Categorical+Data+++Time+Series/global_sales_data/cust_dimen.csv")
order_df=pd.read_csv("/Users/rohithbharatha/Desktop/Session3+-+Categorical+Data+++Time+Series/global_sales_data/orders_dimen.csv")
"""df=pd.merge(market_df,product_df, how='inner', on= 'Prod_id')
df = pd.merge(df, customer_df, how='inner', on='Cust_id')

plt.figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
df=df[(df.Profit < 1000) & (df.Profit > -1000)]
# specify hue="categorical_variable"
sns.boxplot(x='Customer_Segment', y='Profit', hue="Product_Category", data=df)
plt.figure(figsize=(10, 8))

# subplot 1: Sales
plt.subplot(2, 2, 1)
sns.boxplot(x='Customer_Segment', y='Product_Category', data=df)
plt.title("Sales")
plt.yscale('log')

# subplot 2: Profit
plt.subplot(2, 2, 2)
sns.boxplot(x='Product_Category', y='Profit',hue='Customer_Segment', data=df)
plt.title("Profit")

plt.show()
"""
df = pd.merge(market_df, order_df, how='inner', on='Ord_id')

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

time_df=df.groupby('Order_Date')['Sales'].sum()

sns.tsplot(time_df)

df['month']=df['Order_Date'].dt.month
df['year']=df['Order_Date'].dt.year
df.head()

df_time=df.groupby(['month','year']).Sales.mean()

df_time.head()

sns.tsplot(df_time)
plt.xlabel('Time')
plt.ylabel('Sales')


year_month=pd.pivot_table(df, values='Sales',index='year',columns='month', aggfunc='mean')

year_month.head()

sns.heatmap(year_month,cmap='YlGnBu')