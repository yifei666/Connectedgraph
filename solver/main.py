from ortools.linear_solver import pywraplp
min_latency = input("Please input the minimum latency for the network(ms): ")

def create_data_model():
    data = {}
    data['constraint_coeffs'] = [
        [-1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, -1, -1, -1, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, -1, -1, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 1, -1, -1, -1],
        [8, 10, 10, 6, 7, 2, 6, 4, 7, 12, 4]
    ]
    data['bounds'] = [-1, 0, 0, 1]
    data['bounds'].append(int(min_latency)) # append the user input min_latency to the RHS of the last constraint
    data['obj_coeffs'] = [3, 4, 8, 2, 5, 6, 2, 2, 5, 6, 2]
    # data['obj_coeffs'] = [999, 4, 8, 2, 999, 6, 2, 2, 5, 6, 2]
    data['num_vars'] = 11
    data['num_constraints'] = 5
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

    # set the limit of latency to be the last constraint
    constraint = solver.RowConstraint(0, data['bounds'][-1], '')
    for j in range(data['num_vars']):
        constraint.SetCoefficient(x[j], data['constraint_coeffs'][-1][j])
    print('Number of constraints =', solver.NumConstraints())

    # setup the objective function
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], data['obj_coeffs'][j])
    objective.SetMinimization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()
