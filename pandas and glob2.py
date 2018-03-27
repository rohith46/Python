#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:05:12 2018

@author: rohithbharatha
"""
import pandas
import glob2
filelist= glob2.glob("/Users/rohithbharatha/Desktop/python scripts/data sets/*.txt")
for file in filelist:
    df=pandas.read_csv(file)
    m=df.mean()
    print(m)
    
    