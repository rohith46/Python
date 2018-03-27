#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:00:42 2018

@author: rohithbharatha
"""
ids=["B1","\nB2","\nB3","\nB4"]
with open("/Users/rohithbharatha/Desktop/python scripts/textfile.txt",'w') as file:
    for item in ids:
     file.write(item)
    
file = open("/Users/rohithbharatha/Desktop/python scripts/textfile.txt",'r')
print(file.read())