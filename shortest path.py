# from dijsktra import shortestpath as sp
from dijsktra import dijnew,graph_simplify, backup_path
import json
graph1 = {
    "A": {"B": 1, "C": 2},
    "B": {"A": 1, "D": 3, "E": 5},
    "C": {"A": 2, "D": 4},
    "D": {"B": 3, "C": 4, "E": 1},
    "E": {"B": 5, "D": 1, "F": 9},
    "F": {"E": 9}
}

graph2 = {
    "A": {"B": [0.5, 2, 10], "C": 4},
    "B": {"A": 2, "C": 3, "D": 8},
    "C": {"A": 4, "B": 3, "E": 5, "D": 2},
    "D": {"B": 8, "C": 2, "E": 11, "F": 22},
    "E": {"C": 5, "D": 11, "F": 1},
    "F": {"D": 22, "E": 1}
}

graph3 = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 3, "C": 4, "D": 1},
    "C": {"A": 2, "B": 3, "D": 7},
    "D": {"E": 1},
    "E": {"C": 8}
}

graph4 = {
    "A": {"B": [3,4], "C": 8},
    "B": {"C": 2, "D": [5, 6]},
    "C": {"B": 2, "D": 2},
    "D": {"B": [5, 6],"C": 2}
}

with open('graph1.json', 'w') as json_file:
  json.dump(graph1, json_file)
with open('graph2.json', 'w') as json_file:
  json.dump(graph2, json_file)
with open('graph3.json', 'w') as json_file:
  json.dump(graph3, json_file)
with open('graph4.json', 'w') as json_file:
  json.dump(graph4, json_file)