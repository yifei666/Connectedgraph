import json
from dijsktra import dijnew,graph_simplify, backup_path

f = open("graph2.json")
data = json.load(f)
graph = data.get("graph")
start_node = data.get("start_node")
end_node = data.get("end_node")
backup_path(graph,start_node, end_node)