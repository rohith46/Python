#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:48:10 2018

@author: rohithbharatha
"""
"""import pandas as pd
df = pd.DataFrame({'name': ['Vinay', 'Kushal', 'Aman', 'Saif'], 
                   'age': [22, 25, 24, 28], 
                    'occupation': ['engineer', 'doctor', 'data analyst', 'teacher']})
df


import numpy as np
import pandas as pd
series_1 = pd.Series([6,7,8,9,2,3,4,5])
series_2 = series_1.apply(lambda x: x**2)
print(series_1)
print(series_2)

import pandas as pd
market_df=pd.read_csv("/Users/rohithbharatha/Desktop/pandas/global_sales_data/market_fact.csv")

print(market_df.head())

market_df.set_index('Ord_id', inplace= True)

market_df.head()

market_df.sort_index(axis=0, ascending = False)

print(market_df.head())

market_df.sort_values(by=['Prod_id','Sales'], ascending= False).head()



import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.set_index('X', inplace= True)
print(df_2.head())

import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.loc[(df.area > 0) & (df.wind > 1) & (df.temp > 15),:]
print(df_2.head(20))

import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_by_monthday= df.groupby(['month','day'])
df_1 = df_by_monthday['rain','wind'].mean()
print(df_1.head(20)) """



import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_1 = df.pivot_table(values=['rain','wind'],
                      index=['month','day'],aggfunc= 'mean') 
print(df_1.head(20))



