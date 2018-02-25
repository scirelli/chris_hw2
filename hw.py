#!/usr/local/bin/python3

import numpy as np
import math as ma

dataFile = './Session 3_Camera_noname.csv'
np_array = np.genfromtxt(dataFile, delimiter = ',', dtype=None, names=True)

for row in np_array:
	print(row[1])
