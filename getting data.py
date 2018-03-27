#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:04:06 2018

@author: rohithbharatha
"""

import requests,bs4
url="https://play.google.com/store/apps/details?id=com.facebook.orca&hl=en"
req=requests.get(url)

soup=bs4.BeautifulSoup(req.text,"html5lib")
reviews = soup.select('.review-body')
print(type(reviews))
print(len(reviews))
print("\n")
"""
# printing an element of the reviews list
print(reviews[6])

r=reviews[6]"""

review_text= [str(r).split('</span>')[1].split('<div class="review-link"')[0] 
                                    for r in reviews]
print(review_text[1:10])