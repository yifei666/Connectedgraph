# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:15:50 2021

@author: Michael
"""

from randomgraph import nxgraphgenerator
from solver import main


time_list=[]

for i in range(5,41):
    nxgraphgenerator(i, 0.7)
    time = main()
    time_list.append(time)   

print(time_list)