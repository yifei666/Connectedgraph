import json
from dijsktra import dijnew,graph_simplify, backup_path
import time

f = open("graph2.json")
data = json.load(f)
graph = data.get("graph")
start_node = data.get("start_node")
end_node = data.get("end_node")
time_start = time.time()
result = dijnew(graph,start_node, end_node)
time_end = time.time()
time_used = 1000000 * (time_end - time_start)
print(time_start)
print(time_end)
print("Problem solved in " + str(time_used) + "/1000 ms")
print(result)