#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:57:14 2018

@author: rohithbharatha
"""

file= open("/Users/rohithbharatha/Desktop/python scripts/testingfile.txt",'w')
file.write("Such a nice file i am !")
file.close()
file= open("/Users/rohithbharatha/Desktop/python scripts/testingfile.txt",'r')
content=file.read()
print(content)
file= open("/Users/rohithbharatha/Desktop/python scripts/testingfile.txt",'w')
file.write("This is a new line!")
file.close()
file= open("/Users/rohithbharatha/Desktop/python scripts/testingfile.txt",'r')
print(file.read())
file= open("/Users/rohithbharatha/Desktop/python scripts/testingfile.txt",'w')
file.close()
file= open("/Users/rohithbharatha/Desktop/python scripts/testingfile.txt",'a')
file.write("/nthisis a second line bro!!!")
file.close()
file= open("/Users/rohithbharatha/Desktop/python scripts/testingfile.txt",'r')
print(file.read())
file.close()