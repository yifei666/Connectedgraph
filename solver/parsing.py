import json

f = open('graph4.json', 'r')
db = json.load(f)
distance={}
latency={}
count = 0
distance = []
latency = []
for parentnode in db["graph"]:
    for childnode in db["graph"][parentnode]:
        if type(db["graph"][parentnode][childnode]) == "list":
            for link in range(len(db["graph"][parentnode][childnode])):
                print(db["graph"][parentnode][childnode][link]["distance"])
                print(count)
                distance.append(db["graph"][parentnode][childnode][link]["distance"])
                latency.append(db["graph"][parentnode][childnode][link]["latency"])
                count = count + 1
                print(distance)
                print(latency)
        else:
            distance.append(db["graph"][parentnode][childnode]["distance"])
            latency.append(db["graph"][parentnode][childnode]["latency"])


# print(distance)
# print(latency)
print(distance)
print(latency)