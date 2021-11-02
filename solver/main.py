from ortools.linear_solver import pywraplp
import numpy as np

max_latency = input("Please input the max latency for the network(ms): ")
max_packetloss = input("Please input the max packet loss for the network: ")

def create_data_model():
    data = {}
    data['constraint_coeffs'] = [
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
        [1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 1
        [0, 1, 1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],  # 2
        [0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
        [0, 0, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0],  # 5
        [0, 0, 0, 1, 0, 0, 0, -1, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, -1, -1],  # 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, -1, 0, 0, 0, 1, 0],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0],  # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0],  # 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # 11
        [0.14, 0.17, 0.16, 0.1, 0.01, 0.1, 0.2, 0.34, 0.2, 0.08, 0.3, 0.4, 0.1, 0.01, 0.05, 0.05, 0.08, 0.2, 0.16, 0.34, 0.08, 0.3],
        [59, 50, 62, 18, 30, 15, 30, 20, 50, 10, 22, 10, 22, 10, 12, 18, 25, 22, 62, 20, 25, 22]
    ]

    data['bounds'] = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    data['bounds'].append(int(max_latency)) # append the user input min_latency to the RHS of the last constraint
    data['bounds'].append(int(max_packetloss))

    # data['obj_coeffs'] = [3, 4, 8, 2, 5, 6, 2, 2, 5, 6, 2]
    data['obj_coeffs'] = [0.6, 1.1, 0.72, 0.2, 0.01, 0.07, 0.3, 0.2, 0.1, 0.06, 0.2, 1.6, 0.1, 0.05, 0.15, 0.07, 0.1, 0.1, 0.72, 0.2, 0.1, 0.2]
    data['num_vars'] = len(data['constraint_coeffs'][0])
    data['num_constraints'] = 13
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
    for i in range(data['num_constraints'] - 2):
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
        total_latency = sum(np.multiply(np.array(solution), np.array(data['constraint_coeffs'][-2])))
        total_packetloss = sum(np.multiply(np.array(solution), np.array(data['constraint_coeffs'][-1])))
        print()
        print(solution)
        print(data['constraint_coeffs'][-2])
        print(data['constraint_coeffs'][-1])
        print("Current latency: "+str(total_latency))
        print("Current packetloss: " + str(total_packetloss))
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()
