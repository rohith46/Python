#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:29:31 2018

@author: rohithbharatha
"""

import simplekml
kml=simplekml.Kml()
kml.newpoint(name="sample1",coords=[(17,20)])
kml.newpoint(name="sample2",coords=[(10,56)])
kml.save("/Users/rohithbharatha/Desktop/python scripts/ponits.kml")