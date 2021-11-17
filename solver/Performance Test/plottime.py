# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:23:57 2021

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt
## n = 0.3
n1_timelist = [2, 2, 2, 2, 3, 5, 3, 5, 4, 13, 6, 5, 7, 6, 9, 7, 19, 18, 13, 12, 10, 17, 20, 20, 30, 29, 31, 28, 43, 35, 50, 37, 45, 47, 50, 75]


## n = 0.5
n2_timelist = [2, 3, 4, 3, 6, 5, 4, 7, 5, 6, 12, 11, 8, 12, 23, 19, 18, 18, 23, 34, 35, 34, 48, 42, 53, 69, 69, 60, 79, 82, 85, 110, 103, 104, 108, 137]

## n = 0.7
n3_timelist = [2, 2, 3, 4, 5, 7, 7, 7, 8, 8, 12, 13, 16, 18, 23, 33, 44, 37, 52, 38, 43, 69, 72, 81, 90, 99, 106, 121, 127, 128, 138, 165, 178, 186, 205, 206]

x = np.linspace(5,41,36)


plt.plot(x,n1_timelist, label = 'n=0.3')
plt.plot(x,n2_timelist, label = 'n=0.5')
plt.plot(x,n3_timelist, label = 'n=0.7')

plt.title("Computing Time with Different n")
plt.xlabel('Number of Nodes')
plt.ylabel("Millisecond")
plt.legend()
plt.grid(linestyle = '--', linewidth = 0.5)
plt.savefig("Compouting Time.png",dpi = 300)
plt.show()