# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:18:25 2021

@author: Michael
"""
import time
from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import random
import operator
import json
import matplotlib.pyplot as plt
import numpy as np
from solver import main



def latencyheur(g, nodes, max_latency):
    
    global solution
        #### creating the heuristic model
    time_start=time.time()
    allpath_list=[]
    allpath_dict = {}
    for path in nx.all_simple_paths(g, source=0, target=nodes-1):
        allpath_list.append(path)

    
    for path in allpath_list:
        total_length = 0
        total_latency = 0
        for i in range(len(path)-1):
            source, target = path[i], path[i+1]
            edge = g[source][target]
            length = edge['weight']
            lat = edge['latency']
            total_length += length
            total_latency += lat
        allpath_dict[(total_latency,total_length)] = path
    sortedlist = sorted(allpath_dict.items())
    
    
    solution = "Null"
    for pair in sortedlist:
        if pair[0][0] <= max_latency:
            solution = pair
            break
            
    time_end = time.time()
    time_used = (time_end-time_start)*1000
    
    

    return [solution,time_used]

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def nxgraphgenerator(nodes,p,max_latency):
    # random.seed(seed)
    g = erdos_renyi_graph(nodes,p)
    while True:
        if nx.is_connected(g):
            break
        else:
            g = erdos_renyi_graph(nodes,p)

    link_dict = {}
    # print(g.edges)

    edgelist = list(g.edges)
    
    ## generate each node's parent node
    for pair in g.edges:
        if pair[0] in link_dict:
            link_dict[pair[0]].append(pair[1])
        else:
            link_dict[pair[0]]=[pair[1]]
        
        if pair[1] in link_dict:
            link_dict[pair[1]].append(pair[0])
        else:
            link_dict[pair[1]]=[pair[0]]
    linknum = 2*len(g.edges)
         
    sorted_dict = dict(sorted(link_dict.items(), key=operator.itemgetter(0)))  

    
    
    ## show every link (bidirectional link means 2 different link)
    link_list = []
    for startnode in sorted_dict:
        for endnode in sorted_dict[startnode]:
            link_list.append([startnode, endnode])
            
    # print("link list wo title: "+str(link_list))
    
    ## generte a link name list for future look up and reference
    linktitle_dict={}
    for n in range(len(link_list)):
        linktitle_dict[n] = link_list[n]

    
    ## create the  contraint matrix of 0s
    nodenum = len(g.nodes)    
    inputmatrix = []
    for n in range(nodenum):
        inputmatrix.append(zerolistmaker(linknum))
    # print(inputmatrix)
    # print()
    
    ## input values based on the linklist into the matrix, 1 means flow into the nodes, -1 meanse flow out of the node
    c = 0
    for line in inputmatrix:
        n = 0
        for link in link_list:
            if link[0] == c:
                inputmatrix[c][n] = -1
                n= n+1
            elif link[1] == c:
                inputmatrix[c][n] = 1
                n=n+1
            else:
                n=n+1
        c = c+1
    # print("new input"+str(inputmatrix))
        
    distance_list = []
    latency_list = []
   
    for (u,v,w) in g.edges(data=True):
        w['weight'] = random.randint(10,1000000000) #10-10^9
        
        latency = random.randint(10,100) #10,100 1/100 msec
        w['latency'] =latency
        distance_list.append(w['weight']) 
        latency_list.append(latency) 
    
    inputdistance = zerolistmaker(len(link_list))
    inputlatency = zerolistmaker(len(link_list))
    # print(inputdistance)
    
    ## look up and form the distance and latency array for each link
    count = 0
    for link in link_list:
        try:
            inputdistance[count] = distance_list[edgelist.index((link[0],link[1]))]
            count = count+1
        except ValueError:
            inputdistance[count] = distance_list[edgelist.index((link[1],link[0]))]
            count = count+1
            
    count = 0        
    for link in link_list:
        try:
            inputlatency[count] = latency_list[edgelist.index((link[0],link[1]))]
            count = count+1
        except ValueError:
            inputlatency[count] = latency_list[edgelist.index((link[1],link[0]))]

    pos = nx.spring_layout(g)
    
    print()
    # Draw the graph according to node positions
    # nx.draw(g, pos, with_labels=True)

    sortedanswer = latencyheur(g,nodes,max_latency)[0]
    time = latencyheur(g,nodes,max_latency)[1]
    
    print("sorted answer: "+str(sortedanswer))
    
 
    
    
    rhs = zerolistmaker(nodes)
    rhs[0] = -1
    rhs[-1] = 1    
    jsonoutput = {}
    jsonoutput['constraint_coeffs'] = inputmatrix
    jsonoutput['bounds'] = rhs
    jsonoutput['obj_coeffs'] = inputdistance
    jsonoutput['num_vars'] = len(link_list)
    jsonoutput['num_constraints'] = len(inputmatrix)
    jsonoutput['max_latency'] = max_latency
    with open('data.json', 'w') as json_file:
        json.dump(jsonoutput, json_file,indent=4)
  
    try:
        output = sortedanswer[0][1]
    except IndexError:
        output = "Null"
    return [output,time]

# err=[]
# for n in range(15,20):
#     i = 0
#     while i<5:
#         heur = nxgraphgenerator(n,0.1,100)
#         if heur != "Null":
#             solver = main()
#             if heur - solver > 10:
#                 errper = abs(heur - solver)/solver
#                 err.append([solver,heur])
#                 i+=1
# print(err)

        
        
# print(totalerr)



# heur = nxgraphgenerator(20,0.2,100)
# print(heur)

# print(main())


