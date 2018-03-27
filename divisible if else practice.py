#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:40:29 2018

@author: rohithbharatha
"""

num = int (input("Enter the number: "))
if num%2 == 0 :
    print("This is a even number")
    if num%4 == 0:
        print('This is a divisible of 4')
    else:
        print('This is not a divisible of 4')
else:
    print("This is a odd number")
    if num%3 == 0:
        print("This is a divisible of 3")
    else:
        print('This is not a divisible of 3')
