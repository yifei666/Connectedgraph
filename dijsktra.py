import heapq
infinite = 99999999  # for comparision
node_data = {
    "A": {"cost": infinite, "pre": []},
    "B": {"cost": infinite, "pre": []},
    "C": {"cost": infinite, "pre": []},
    "D": {"cost": infinite, "pre": []},
    "E": {"cost": infinite, "pre": []},
    "F": {"cost": infinite, "pre": []}
}

def dijkstra(graph, start_node, end_node):
    visited_node = []

    node_data[start_node]["cost"] = 0
    current = start_node

    for i in range(len(graph) - 1):
        if current not in visited_node:
            visited_node.append(current)
            min_heap = []
            for ele in graph[current]:  # find the min cost neighbour
                if ele not in visited_node:
                    cost = node_data[current]["cost"] + graph[current][ele]
                    if cost < node_data[ele]["cost"]:  # assign the value if has shorter path
                        node_data[ele]["cost"] = cost
                        node_data[ele]["pre"] = node_data[current]["pre"] + list(current)
                    heapq.heappush(min_heap, (node_data[ele]["cost"], ele))
                    # print(min_heap)

        # print("\n")
        print(node_data)
        heapq.heapify(min_heap)
        print(min_heap)

        print("visited" + str(visited_node))
        print(current)

        current = min_heap[0][1]
        print("current" + current)
        print("\n")

    print("Shortest distance is " + str(node_data[end_node]["cost"]))
    print("Shortest path is " + str(node_data[end_node]["pre"] + list(end_node)))




def dijnew(graph, start_node, end_node):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start_node] = 0
    # print(shortest_distance)

    while unseenNodes: # loop all the nodes in the list
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node  # find the current node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = end_node # run path backwards to get the real path
    while currentNode != start_node:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start_node)
    if shortest_distance[end_node] != infinity: # check if the end_node has been reached
        print('Shortest distance is ' + str(shortest_distance[end_node]))
        print('And the path is ' + str(path))



