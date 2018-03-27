#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:47:21 2018

@author: rohithbharatha
"""

score= int(input("Enter your marks: "))
if score == 100:
    print("Perfect")
elif score >=90:
    print("You scored a distinction")
elif 65<=score<90:
    print("You are on first class")
elif 40<=score<65:
    print("You have barely passed")
elif score < 40:
    print("Sorry you have failed")

    