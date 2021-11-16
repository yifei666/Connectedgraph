# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:08:45 2021

@author: Michael
"""


from __future__ import print_function
from ortools.graph import pywrapgraph


def main():


    start_node = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7]
    end_node = [1, 2, 2, 3, 1, 3, 4, 5, 6, 3, 6, 7, 6, 8, 5, 7, 8, 6, 8]
    capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    distance = [4, 2, 2, 7, 4, 9, 6, 1, 5, 2, 3, 2, 1, 5, 4, 3, 6, 2, 6]


    rhs = [1, 0, 0, 0, 0, 0, 0, 0, -1]

    min_cost_flow = pywrapgraph.SimpleMinCostFlow()

    for i in range(0, len(start_node)):
        min_cost_flow.AddArcWithCapacityAndUnitCost(start_node[i], end_node[i],
                                                    capacity[i], distance[i])


    for i in range(0, len(rhs)):
        min_cost_flow.SetNodeSupply(i, rhs[i])

    if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
        print('Minimum distance:', min_cost_flow.OptimalCost())
        print('')
        print(' Path    Used / Capacity  Distance')
        for i in range(min_cost_flow.NumArcs()):
            cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
            print('%1s -> %1s    %3s   / %3s       %3s' % (
                min_cost_flow.Tail(i),
                min_cost_flow.Head(i),
                min_cost_flow.Flow(i),
                min_cost_flow.Capacity(i),
                cost))
    else:
        print('There is an issue to solve the problem.')


if __name__ == '__main__':
    main()