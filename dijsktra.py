import heapq
graph={
    "A": {"B": 1, "C": 2},
    "B": {"A": 1, "D": 3, "E": 5},
    "C": {"A": 2, "D": 4},
    "D": {"B": 3, "C": 4, "E": 1},
    "E": {"B": 5, "D": 1, "F": 9}
}

start_node = "A"
end_node = "F"
infinite=99999999  # for comparision

node_data={
    "A": {"cost": infinite, "pre": []},
    "B": {"cost": infinite, "pre": []},
    "C": {"cost": infinite, "pre": []},
    "D": {"cost": infinite, "pre": []},
    "E": {"cost": infinite, "pre": []}
}
visited_node=[]

node_data[start_node]["cost"]=0
current = start_node

for i in range(len(graph)-1):
    if current not in visited_node:
        visited_node.append(current)
        min_heap=[]
        for ele in graph[current]: # find the min cost neighbour
            if ele not in visited_node:
                cost = node_data[current]["cost"]+graph[current][ele]
                if cost < node_data[ele]["cost"]:
                    node_data[ele]["cost"] = cost
                    node_data[ele]["pre"] = node_data[current]["pre"]+list(current)
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