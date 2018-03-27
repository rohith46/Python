#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:10:49 2018

@author: rohithbharatha
"""

import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename

def browse():
    global infile
    infile=askopenfilename()
    
def kmlfunction(outfile="/Users/rohithbharatha/Desktop/python scripts/points.kml"):
    df=pandas.read_csv(infile)
    kml=simplekml.Kml()
    for lon,lat in zip(df["Longitude"],df["Latitude"]):
        kml.newpoint(coords=[(lon,lat)])
    kml.save(outfile)
    
root=tkinter.Tk()
root.title("The Kml Generator")
label=tkinter.Label(root,text="this GUI helps browse and save KML files")
label.pack()
browseButton=tkinter.Button(root,text="Browse",command=browse)
browseButton.pack()
kmlButton=tkinter.Button(root,text="KML Generator",command=kmlfunction)
kmlButton.pack()
root.mainloop()
