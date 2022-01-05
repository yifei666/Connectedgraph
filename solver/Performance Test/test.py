#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:13:44 2021

@author: yifeiwang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:28:47 2021

@author: yifeiwang
"""
from solver import main
from randomgraph import nxgraphgenerator
import numpy as np
import matplotlib.pyplot as plt


def test(latency, nodes, n, samplenumber, coefficient):
    data=[]
    perlist=[]
    for node in range(nodes[0],nodes[1]):
        i = 0
        while i < samplenumber:
            heur = nxgraphgenerator(node, n, coefficient*node)[0]
            heurtime = nxgraphgenerator(node, n, coefficient*node)[1]
            if heur != "Null":
                solver = main()[0]
                solvertime = main()[1]
                if heur - solver > 10:
                    errper = abs(heur - solver)/solver
                    perlist.append(errper)
                    data.append([solver,heur,solvertime,heurtime])
                    i+=1
    solvertimelist = []
    heurtimelist = []
    solveravglist = []
    heuravglist = []
    heurstd = []
    length = int(nodes[1]-nodes[0])
    for n in range(length):
        solvertime = []
        heurtime = []
        solversol = []
        heursol= []
        c = 0
        while c < samplenumber:
            heursol.append(data[n * samplenumber+c][0])
            solversol.append(data[n * samplenumber+c][1])
            solvertime.append(data[n * samplenumber+c][2])
            heurtime.append(data[n * samplenumber+c][3])
            c=c+1
        solvertimelist.append(np.mean(solvertime))
        heurtimelist.append(np.mean(heurtime))
        solveravglist.append(np.mean(solversol))
        heuravglist.append(np.mean(heursol))
        print(heursol)
        heurstd.append(np.std(heursol))

    
            
            
        
        
    print(solvertimelist)
    print(heurtimelist)
    print(solveravglist)
    print(heuravglist)
    print(heurstd)


    CTEs = solveravglist
    error = heurstd
    # Build the plot
    labels = []
    x_axis = []
    for num in range(nodes[0],nodes[1]):
        labels.append(str(num))
        x_axis.append(num)

    x_pos = np.arange(len(labels))
    fig, ax = plt.subplots()
    ax.bar(x_pos, CTEs,
           yerr=error,
           align='center',
           alpha=0.5,
           ecolor='black',
           capsize=10)

    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_title('Solver solution with Heuristic Solution Std')
    ax.yaxis.grid(True)
    ax.set_xlabel("Number of Nodes")
    ax.set_ylabel('Path Weights')
    
    # Save the figure and show
    plt.tight_layout()
    plt.savefig('bar_plot_with_error_bars.png', dpi = 300)
    plt.show()
    
    

    plt.plot(x_axis, solvertimelist, label = "solver")
    plt.plot(x_axis, heurtimelist, label = "heur")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Milliseconds")
    plt.title("Computation Time: Solver Vs Heuristic")
    plt.legend()
    plt.savefig("Computatoin Time", dpi = 300)
    plt.show()
    
    
    


test(nodes=[15,35],n=0.1,samplenumber=5, coefficient=7,latency = 0)