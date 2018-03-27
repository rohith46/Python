#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:50:53 2018

@author: rohithbharatha
"""

"""import numpy as np

rand_array= np.random.random((1000,300))


print("Shape : {}".format(rand_array.shape))
print("dtype : {}".format(rand_array.dtype))
print("ndim : {}".format(rand_array.ndim))
print("Item size : {}".format(rand_array.itemsize))


array_3d = np.arange(24).reshape(3,2,4)

print(array_3d)




list_1 = input("Enter the rows:")
list_2 = input("Enter the columns:")

import numpy as np
array_1 = np.array([list_1,list_2])

print("Shape :{}".format(array_1.Shape))
print("Dimension :{}".format(array_1.ndim))


array_1d = np.arange(10)
print(array_1d)

print(array_1d[0::2])

array_3d=np.arange(24).reshape(2,3,4)
print(array_3d[:,:2])

for column in array_3d:
    print(column)


import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
import numpy as np
array_2d =np.array(input_list) 

print(array_2d[:,1])




list_1 = [i for i in range(1000000)]
list_2 = [j**2 for j in range(1000000)]
import time
t0=time.time()
product_list=list(map(lambda x,y: x*y, list_1, list_2))
t1=time.time()
list_time= t1-t0
print(t1-t0)

array_1=np.array(list_1)
array_2=np.array(list_2)
t0=time.time()
array_3=array_1*array_2
t1=time.time()
numpy_time=t1-t0
print(t1-t0)

"""
import numpy as np
array = np.arange(0,12).reshape(3,4)
print(array)

print(array.reshape(4,-1))
print(array.T)