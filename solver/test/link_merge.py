import json

def parsing(filename, start_node, end_node):
    f = open(filename)
    data = json.load(f)

    cost = {}
    delay = {}

    for link in data:
        id = link["id"]
        latency = link["latency"]
        cost = link["available_bandwidth"]
        parentnode = link["ports"][0]["id"]
        childnode = link["ports"][1]["id"]
        print(parentnode)
        cost["graph"]=parentnode
        # cost["graph"][parentnode].append(childnode)
        print(cost)



parsing("multilink.json", "A", "F")
