#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:43:19 2018

@author: rohithbharatha
"""

import pandas

delay=int(input("Enter the delay time:"))
ramprate=int(input("Enter the ramp:"))
points=(60/delay)*(1/ramprate)
print(points)
temps=int(input("Enter the numbers:"))
df=pandas.read_csv("/Users/rohithbharatha/Desktop/Book1.csv")
for i in temps:
    z=df.loc[df["x"] == i,"y"]
    c=sum(z)
    avg=(c/points)
    print(avg)