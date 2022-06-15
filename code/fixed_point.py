# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:47:43 2022

@author: Dell
"""
import numpy as np

from scipy import optimize
def func(x, c1):
    y = (0.5*x*c1)/(1+ np.absolute(x*c1)) +0.5
    print(y)
    return y

c1 = np.array([.33])
#c2 = np.array([3, 5.])
y = optimize.fixed_point(func, [0.8], args=(c1))
print(y)




# from scipy import optimize
# def func(x, c1, c2):
#    return np.sqrt(c1/(x+c2))
# c1 = np.array([10,12.])
# c2 = np.array([3, 5.])
# print(optimize.fixed_point(func, [0, 0], args=(c1,c2)))