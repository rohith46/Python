#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:41:57 2018

@author: rohithbharatha
"""
with open("/Users/rohithbharatha/Desktop/python scripts/withcommand.txt",'w') as file:
    file.write("This is with command")
    
file= open("/Users/rohithbharatha/Desktop/python scripts/withcommand.txt",'r')
print(file.read())