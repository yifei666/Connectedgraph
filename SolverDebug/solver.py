# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:25:20 2021

@author: Michael
"""

from ortools.linear_solver import pywraplp
import numpy as np
import json

max_latency = input("Please input the max latency for the network(ms): ")



  
def create_data_model():
    with open('data.json') as f:
          graph = json.load(f)
  
  
    data = {}
    data['constraint_coeffs'] = graph['constraint_coeffs']

    data['bounds'] = graph['bounds']
    data['bounds'].append(int(max_latency)) # append the user input min_latency to the RHS of the last constraint



    data['obj_coeffs'] = graph['obj_coeffs']
    data['num_vars'] = len(data['constraint_coeffs'][0])
    data['num_constraints'] = graph['num_constraints']
    print(data)
    return data


def main():
    data = create_data_model()
    solver = pywraplp.Solver.CreateSolver('SCIP')

    x = {}

    # set the variables to be binary
    for j in range(data['num_vars']):
        x[j] = solver.IntVar(0, 1, 'x[%i]' % j)
    print('Number of variables =', solver.NumVariables())

    # setup the equality of the constraints and RHS
    for i in range(data['num_constraints'] - 1):
        constraint = solver.RowConstraint(data['bounds'][i], data['bounds'][i], '')
        for j in range(data['num_vars']):
            constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])

    # for i in [data['num_constraints']-1,data['num_constraints']]:
    #     constraint = solver.RowConstraint(0, data['bounds'][i], '')
    #     for j in range(data['num_vars']):
    #         constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])

    # set the limit of latency to be the last constraint
    constraint = solver.RowConstraint(0, data['bounds'][-1], '')
    # constraint = solver.RowConstraint(0, data['bounds'][-2], '')

    for j in range(data['num_vars']):
        constraint.SetCoefficient(x[j], data['constraint_coeffs'][-1][j])
    print('Number of constraints =', solver.NumConstraints())

    # setup the objective function
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], data['obj_coeffs'][j])
    objective.SetMinimization()

    status = solver.Solve()

    solution = []
    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
            solution.append(x[j].solution_value())
        total_latency = sum(np.multiply(np.array(solution), np.array(data['constraint_coeffs'][-1])))
        
        print()
        print(solution)
        print(data['constraint_coeffs'][-1])
        print("Current latency: "+str(total_latency))
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()
