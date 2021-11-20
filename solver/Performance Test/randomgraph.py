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

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def nxgraphgenerator(nodes,p):
    # random.seed(seed)
    g = erdos_renyi_graph(nodes,p)
    while True:
        if nx.is_connected(g):
            break
        else:
            g = erdos_renyi_graph(nodes,p)

    link_dict = {}
    print(g.edges)

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
    print("link list: "+str(sorted_dict))
    print()
    
    
    ## show every link (bidirectional link means 2 different link)
    link_list = []
    for startnode in sorted_dict:
        for endnode in sorted_dict[startnode]:
            link_list.append([startnode, endnode])
            
    print("link list wo title: "+str(link_list))
    
    ## generte a link name list for future look up and reference
    linktitle_dict={}
    for n in range(len(link_list)):
        linktitle_dict[n] = link_list[n]
    print("link list with title: " + str(linktitle_dict))
    print()
    
    
    ## create the  contraint matrix of 0s
    nodenum = len(g.nodes)    
    inputmatrix = []
    for n in range(nodenum):
        inputmatrix.append(zerolistmaker(linknum))
    print(inputmatrix)
    print()
    
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
    print("new input"+str(inputmatrix))
        
    distance_list = []
    latency_list = []
    for (u,v,w) in g.edges(data=True):
        w['weight'] = random.randint(1,10)
        latency = random.randint(1,10)
        distance_list.append(w['weight']) 
        latency_list.append(latency) 
    
    inputdistance = zerolistmaker(len(link_list))
    inputlatency = zerolistmaker(len(link_list))
    print(inputdistance)
    
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
            count = count+1
    print("input distance: "+str(inputdistance))
    print("input latency: "+str(inputlatency))
        
    pos = nx.spring_layout(g)
    
    print()
    # Draw the graph according to node positions
    nx.draw(g, pos, with_labels=True)
    plt.savefig("graph.png", dpi=300)

    ## append the latency constraint to the constraint matrix
    inputmatrix.append(inputlatency)
    print(inputmatrix)
    for e  in g.edges.data():
        labels=(e)
        print(labels)
    # Draw edge labels according to node positions
    # nx.draw_networkx_edge_labels(g, pos, edge_labels=g.edges.data()[2]['weight'])
    
    print(nx.dijkstra_path(g, 0, nodes-1))
    # [0, 16, 3, 10, 19]
    
    rhs = zerolistmaker(nodes)
    rhs[0] = -1
    rhs[-1] = 1    
    print(rhs)
    jsonoutput = {}
    jsonoutput['constraint_coeffs'] = inputmatrix
    jsonoutput['bounds'] = rhs
    jsonoutput['obj_coeffs'] = inputdistance
    jsonoutput['num_vars'] = len(link_list)
    jsonoutput['num_constraints'] = len(inputmatrix)
    with open('data.json', 'w') as json_file:
        json.dump(jsonoutput, json_file,indent=4)
  



nxgraphgenerator(10, 0.2)








