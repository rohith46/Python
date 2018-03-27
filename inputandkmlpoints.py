#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:33:43 2018

@author: rohithbharatha
"""

import simplekml
kml=simplekml.Kml()
A=int(input("Enter the longitude: "))
B=int(input("Enter the latitude: "))
kml.newpoint(name="sample",coords=[(A,B)])
kml.save("/Users/rohithbharatha/Desktop/python scripts/point2.kml")
