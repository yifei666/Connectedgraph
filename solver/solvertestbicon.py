# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:47:54 2021

@author: Michael
"""

from ortools.linear_solver import pywraplp


def Shortestpath():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    
    a = solver.NumVar(0, 1, 'a')
    b = solver.NumVar(0, 1, 'b')
    c = solver.NumVar(0, 1, 'c')
    d = solver.NumVar(0, 1, 'd')
    e = solver.NumVar(0, 1, 'e')
    f = solver.NumVar(0, 1, 'f')
    g = solver.NumVar(0, 1, 'g')
    h = solver.NumVar(0, 1, 'h')
    i = solver.NumVar(0, 1, 'i')
    print('Number of variables =', solver.NumVariables())
    
    solver.Add(b + d - a - c == -1)
    solver.Add(a - b - e - f == 0)
    solver.Add(c + e + h - d - g == 0)
    solver.Add(f + g - i == 0)
    solver.Add(i - h == 1)

    print('Number of constraints =', solver.NumConstraints())


    solver.Minimize(a + 3*b + 4*c + 2*d + 4*e + f + 7*g + 8*h +i)

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('a =', a.solution_value())
        print('b =', b.solution_value())
        print('c =', c.solution_value())
        print('d =', d.solution_value())
        print('e =', e.solution_value())
        print('f =', f.solution_value())
        print('g =', g.solution_value())
        print('h =', h.solution_value())
        print('i =', i.solution_value())        
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())


Shortestpath()