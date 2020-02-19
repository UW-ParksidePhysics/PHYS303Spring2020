# -*- coding: utf-8 -*-
"""
Computational Physics Spring 2020 Chapter 3
"""
#
#from math import exp
#
## Calculate derivative
#x = 2.0
#def f(x):
#    f = x * exp(-x) 
#    return f
#
#while True:
#    deltax = eval(input("delta_x: "))
#    if deltax < 0:
#        break
#    derivative=(f(x+deltax)-f(x))/deltax
#    print("delta_x = ", deltax, "df/dx = ", derivative)
    
    
## Finding the run time of a program
#from time import time
#
#start = time() # start time
#n = 0
#nmax = int(1e8 + 1)
#for i in range(1, nmax):
#    n = n + i
#    
#end  = time() # end time
#print(start, ",", end)
#print("run time = ", end - start, "seconds")
## print (n)

import numpy as np
import matplotlib.pyplot as plt

def lennardjones(separations, zero_potential_separation, well_depth):
    scaled_separation = zero_potential_separation / separations
    scaled_separation_six = np.power(scaled_separation, 6)
    scaled_separation_twelve = np.power(scaled_separation, 12)
    potential = 4 * well_depth * (scaled_separation_twelve - 
                                  scaled_separation_six)
    return potential

zero_potential_separation = 0.2
well_depth = 2.0
number_of_separation_values = 100
maximum_separation = 1.0


minimum_separation = maximum_separation / float(number_of_separation_values)
separation_values = np.linspace(minimum_separation, maximum_separation, 
                         number_of_separation_values)

plt.plot(separation_values, lennardjones(separation_values, 
                                         zero_potential_separation, 
                                         well_depth))
plt.axis([0, maximum_separation, -well_depth, well_depth])


plt.show()