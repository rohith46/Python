#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:51:24 2018

@author: rohithbharatha
""

import pandas as pd
df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
print(df.isnull().sum())

import pandas as pd
df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
print(round(100*(df.isnull().sum()/len(df.index)),2)) """


import pandas as pd
import numpy as np
df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
df = df[df.isnull().sum(axis=1) <= 5 ]

#(np.isnan(df['Product_Base_Margin']).mean()) = df['Product_Base_Margin']

df.loc[np.isnan(df['Product_Base_Margin']),['Product_Base_Margin']] = df['Product_Base_Margin'].mean()
print(round(100*(df.isnull().sum()/len(df.index)),2))