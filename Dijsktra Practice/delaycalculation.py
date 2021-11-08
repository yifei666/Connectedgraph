import json
path = ['A', 'C', 'E', 'F']

def costdelaycal(filename, path):
    f = open(filename)
    data = json.load(f)
    graph = data.get("graph")
    delay = 0
    c = 0
    for node in path:
        c = c + 1
        if c+1<= len(path):
            delay = delay + graph[node][path[c]]
    return delay
