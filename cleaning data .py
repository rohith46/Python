#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:44:10 2018

@author: rohithbharatha
"""
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/rohithbharatha/Desktop/3_Getting_and_Cleaning_Data/melbourne.csv")

print(df.isnull().any(axis=1))
print(round(100*(df.isnull().sum())/len(df.index),2))

df= df.drop('BuildingArea',axis=1)
df= df.drop('YearBuilt',axis=1)
df= df.drop('CouncilArea',axis=1)
print(round(100*(df.isnull().sum())/len(df.index),2))
print(100*len(df[df.isnull().sum(axis=1) > 5].index)/len(df.index))

df= df[df.isnull().sum(axis=1) <=5]
print(round(100*(df.isnull().sum())/len(df.index),2))

df=df[~np.isnan(df['Price'])]
print(round(100*(df.isnull().sum())/len(df.index),2))




df=df[~np.isnan(df['Landsize'])]

df['Landsize'].describe()
df['Bathroom'].describe()

df.loc[:,['Lattitude', 'Longtitude']].describe()

df.loc[np.isnan(df['Lattitude']),['Lattitude']] = df['Lattitude'].mean()

df.loc[np.isnan(df['Longtitude']),['Longtitude']]=df['Longtitude'].mean()

df.loc[:,['Bathroom','Car']].describe()

df['Car']= df['Car'].astype('category')
df['Car'].value_counts()

df.loc[pd.isnull(df['Car']),['Car']] = 2
print(round(100*(df.isnull().sum())/len(df.index),2))

df['Bathroom']=df['Bathroom'].astype('category')
df['Bathroom'].value_counts()


df.loc[pd.isnull(df['Bathroom']),['Bathroom']] = 1
print(round(100*(df.isnull().sum())/len(df.index),2))