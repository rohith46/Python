#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:08:51 2018

@author: rohithbharatha
"""

import pandas
import simplekml
import tkinter
from tkinter.filedialog import askopenfilename


def Browse():
    global infile
    infile=askopenfilename()
    

def kmlFunction(outfile="/Users/rohithbharatha/Desktop/python scripts/points.kml"):
    kml=simplekml.Kml()
    df=pandas.read_csv(infile)
    for lon,lat in zip(df["Longitude"],df["Latitude"]):
        kml.newpoint(coords=[(lon,lat)])
        kml.save(outfile)
    
root=tkinter.Tk()
root.title("The Kml Generator")
label=tkinter.Label(root,text="This program is to generate KML files")
label.pack()
browseButton=tkinter.Button(root,text="Browse",command=Browse)
browseButton.pack()
kmlButton=tkinter.Button(root,text="KML Generator",command=kmlFunction)
kmlButton.pack()
root.mainloop()