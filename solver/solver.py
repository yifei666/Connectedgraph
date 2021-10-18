### Solver test for graph3

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

    print('Number of variables =', solver.NumVariables())

    solver.Add(a + b == 1)
    solver.Add(b - d == 0)
    solver.Add(a - e - c == 0)
    solver.Add(c + d - f == 0)
    solver.Add(e + f - g == 0)
    solver.Add(g == 1)

    print('Number of constraints =', solver.NumConstraints())

    solver.Minimize(a + + 2 * b + 3 * c + 4 * d + 5 * e + f + 9 * g)

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
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())


Shortestpath()