#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 01:51:05 2018

@author: rohithbharatha
"""

"""def count(i):

       cont=0
       if i[0] == 'S':
          cont += 1
       return cont

ls =['San Jose', 'San Francisco', 'Santa Fe', 'Houston']

#print(len(map(count,ls)))
i=0
for x in ls:
#def ct(x,i) :
    if x[0]== 'S':
        i +=1

print(i)
print(map(ct,ls)) """

ls =['San Jose', 'San Francisco', 'Santa Fe', 'Houston']
def ct(x):
    i=0
    if x[0]== 'S':
        i +=1
    sum(i)

count = len(list(map(ct,ls)))
print(count)

ls =['San Jose', 'San Francisco', 'Santa Fe', 'Houston']
count= sum(list(map(lambda x: x[0]=='S',ls)))
print(count)


ls=['soap','sharp','shy','silent','ship','summer','sheep']
sp = list(filter((lambda x: (x[0]=='s') & (x[-1]=='p')),ls))

print(sp)