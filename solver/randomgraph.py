# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:18:25 2021

@author: Michael
"""
import time
from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import random

def nxgraphgenerator(n,p):
    g = erdos_renyi_graph(n, p)
    print(g.nodes)
    print(g.edges)
    
    
    
    
    for (u,v,w) in g.edges(data=True):
        w['weight'] = random.randint(0,10)
        
        
    pos = nx.spring_layout(g)
    
    # Draw the graph according to node positions
    nx.draw(g, pos, with_labels=True)
    
    # Create edge labels
    # labels = {e: str(e) for e in g.edges}
    
    for e  in g.edges.data():
        labels=(e)
        print(labels[2]['weight'])
    # Draw edge labels according to node positions
    # nx.draw_networkx_edge_labels(g, pos, edge_labels=g.edges.data()[2]['weight'])
    
    print(nx.dijkstra_path(g, 0, 19))
    # [0, 16, 3, 10, 19]
    

start_time = time.time()
for i in range(1):    
    nxgraphgenerator(20,0.5)

end_time = time.time()
total_time = end_time-start_time
print(total_time)
