import json
from dijsktra import dijnew,graph_simplify, backup_path
from delaycalculation import costdelaycal
import time

f = open("graph2.json")
data = json.load(f)
graph = data.get("graph")
start_node = data.get("start_node")
end_node = data.get("end_node")

delay = open("graph2delay.json")
delaydata = json.load(delay)
delaygraph = delaydata.get("graph")

delay = 900
result = dijnew(graph,start_node, end_node)
state = True

if costdelaycal("graph2delay.json", result[1]) <= delay:
    print("Shortest distance and path: " + str(result))
    print("Delay is " + str(costdelaycal("graph2delay.json", result[1])))
elif dijnew(delaygraph, start_node, end_node)[0] > delay:
    print("There is no solution")
else:
    pc = dijnew("graph2.json",start_node, end_node)[1]
    pd = dijnew("graph2delay.json",start_node, end_node)[1]
    while state:
        lamda = (costdelaycal("graph2.json", pc) - costdelaycal("graph2.json", pd))/(costdelaycal("graph2delay.json", pd) - costdelaycal("graph2.json", pc))





