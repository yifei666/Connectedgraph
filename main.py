import json
from dijsktra import dijnew,graph_simplify, backup_path

f = open("graph4.json")
graph = json.load(f)
backup_path(graph,"A", "D")