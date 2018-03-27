#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:29:01 2018

@author: rohithbharatha
"""

list_of_usernames=['rocky','rohit','kumar','bharatha']
input_name=input("Enter the email id:")
userid_split=input_name.split('@')
print(userid_split)
if userid_split[0:len(userid_split)] == list_of_usernames[0:len(list_of_usernames)]:
    print('true')
else:
    print('false')
    

