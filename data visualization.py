#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:26:24 2018

@author: rohithbharatha
"""
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(5,100,100)
y= np.linspace(10,1000,100)

plt.plot(x,y)

plt.show()

plt.xlabel("Time")
plt.ylabel("Variance")
plt.title("Graph ")

plt.xlim(20,80)
plt.ylim(200,1000)

plt.plot(x,y,'g+')


x=np.linspace(1,10,100)
y=np.log(x)
plt.figure(1)

plt.subplot(121)
plt.title('y=log(x)')
plt.plot(x,y)

plt.subplot(122)
plt.title('y=log(x)**2')
plt.plot(x,y**2)
plt.figure(1)
plt.subplot(221)
plt.title("cubic")
plt.plot(x,x**3)

plt.subplot(222)
plt.title("log")
plt.plot(x,np.log(x))

plt.subplot(223)
plt.title("exponential")
plt.plot(x,x**2)

plt.subplot(224)
plt.title("linear")
plt.plot(x,x) """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/rohithbharatha/Desktop/python learning week/Session2+-+Plotting+Distributions/global_sales_data/market_fact.csv")
"""
plt.boxplot(df['Order_Quantity'])

plt.boxplot(df['Sales'])

plt.subplot(1,2,1)
plt.boxplot(df['Sales'])

plt.subplot(1,2,2)
plt.boxplot(df['Sales'])
plt.yscale('log')

plt.hist(df['Sales'])
plt.yscale('log')
plt.show()

plt.scatter(df['Sales'],df['Profit'])


image = plt.imread("/Users/rohithbharatha/Desktop/Session1+-+Basics+of+Plotting/number.png")
plt.imshow(image)

"""

import seaborn as sns 
#sns.distplot(df['Shipping_Cost'])

#sns.distplot(df['Sales'][:1000],rug=True)

df=df[df.Profit > 0]
sns.jointplot('Sales','Profit',df)







