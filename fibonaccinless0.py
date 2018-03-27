#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:05:05 2018

@author: rohithbharatha
"""
n= int (input("Enter the nth number:"))
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
   
    elif n==1:
        return 0
   
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

 
print(Fibonacci(n))