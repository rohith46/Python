#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:27:08 2018

@author: rohithbharatha
"""
def milestokm(miles):
    global km
    km=miles*1.60934
    print(km)
miles=int(input("enter the miles: "))
milestokm(miles)