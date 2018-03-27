#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:48:53 2018

@author: rohithbharatha
"""
import simplekml
import pandas
kml=simplekml.Kml()
df=pandas.read_csv("/Users/rohithbharatha/Desktop/python scripts/data sets/coords.csv")
for lon,lat in zip(df["Longitude"],df["Latitude"]):
    kml.newpoint(coords=[(lon,lat)])
kml.save("/Users/rohithbharatha/Desktop/python scripts/newpoints3.kml")
