#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:00:38 2018

@author: rohithbharatha
"""

import pandas as pd
import numpy as np

df = pd.read_csv("/Users/rohithbharatha/Desktop/popularity.csv")



per = np.percentile(df[' shares'],78)

print(per)