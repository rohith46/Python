#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:35:04 2018

@author: rohithbharatha
"""

import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import os 

os.chdir('Desktop')

earthquakes = pd.read_csv('earthquake_database.csv')
landslides  = pd.read_csv('catalog.csv')
volcanos    = pd.read_csv('volcanos_database.csv')

np.random.seed(0)

print(landslides['date'].head())

landslides['date'].dtype

earthquakes['Date'].dtype

landslides['date_parsed'] = pd.to_datetime(landslides['date'], format = '%m/%d/%y')

landslides['date_parsed'].head()

#earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format = '%m/%d/%y')
earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], infer_datetime_format = True)
earthquakes['date_parsed'].head()

#day_of_month_landslides = landslides['Date'].dt.day

day_of_month_landslides = landslides['date_parsed'].dt.day

day_of_month_landslides.isnull().sum()
day_of_month_landslides = day_of_month_landslides.dropna()


sns.distplot(day_of_month_landslides, kde = False, bins = 31)



day_of_month_earthquakes = earthquakes['date_parsed'].dt.day

day_of_month_earthquakes.isnull().sum()


sns.distplot(day_of_month_earthquakes, kde = False, bins = 31)

#Volcanos 
volcanos['Last Known Eruption'].sample(5)

volcanos['Last Known Eruption'].dtype

s = volcanos['Last Known Eruption'].replace('Unknown', np.nan)

s = s.dropna()


