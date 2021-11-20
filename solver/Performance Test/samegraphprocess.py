# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:39:38 2021

@author: Michael
"""


import json
import random
import os
from solver import main
import numpy as np
from matplotlib import pyplot as pl
# f = open("data.json","r")
# data = f.read()
# file = json.loads(data)
# print(file['constraint_coeffs'])
# random.shuffle(file['constraint_coeffs'])
# print(file['constraint_coeffs'])
from randomgraph import nxgraphgenerator



mean_list=[]
var_list=[]
for n in range(15,41):
    nxgraphgenerator(n,0.1)
    time_list=[]
    for i in range(50):
        random.seed(i)
        filename = 'data.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            copy=data['constraint_coeffs'][:-1]
            print(copy)
            random.shuffle(copy)
            print(copy)
            print(data['constraint_coeffs'])
            data['constraint_coeffs'][:-1] = copy
            print(data['constraint_coeffs'])
        
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
        time = main()
        time_list.append(time)   
    
    
    mean_list.append(np.mean(time_list))
    var_list.append(np.var(time_list))
    
    
    
print(mean_list)

print(var_list)
