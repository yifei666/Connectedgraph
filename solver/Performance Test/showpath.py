# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:23:43 2021

@author: Michael
"""
from randomgraph import nxgraphgenerator
from solver import main


path = []

link_dict = nxgraphgenerator(20, 0.05, 50)
solution = main()
for i in range(len(solution)):
    if solution[i] == 1:
        path.append(link_dict[i])

print(path)