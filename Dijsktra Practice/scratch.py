import json
data = {
   "graph":{
      "A":{
         "B":1,
         "C":3
      },
      "B":{
         "A":1,
         "C":1,
         "D":4
      },
      "C":{
         "A":3,
         "B":1,
         "E":5,
         "D":1
      },
      "D":{
         "B":4,
         "C":1,
         "E":5,
         "F":6
      },
      "E":{
         "C":5,
         "D":2,
         "F":4
      },
      "F":{
         "D":6,
         "E":4
      }
   },
   "start_node":"A",
   "end_node":"F"
}


with open('graph2delay.json', 'w') as json_file:
    json.dump(data, json_file,  indent=4, sort_keys=True)