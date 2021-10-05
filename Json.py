import json

graph = {"A": {"B": 1, "C": 2},
    "B": {"A": 1, "D": 3, "E": 5},
    "C": {"A": 2, "D": 4},
    "D": {"B": 3, "C": 4, "E": 1},
    "E": {"B": 5, "D": 1, "F": 9},
    "F": {"E": 9}
}

with open('graphjson.json', 'w') as json_file:
  json.dump(graph, json_file)

f =open("graphjson.json")
data =json.load(f)
print(data)




