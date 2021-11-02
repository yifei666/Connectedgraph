import os
import json
path_to_jsonfiles = 'test'
alldicts = []
for file in os.listdir(path_to_jsonfiles):
    full_filename = "%s/%s" % (path_to_jsonfiles, file)
    with open(full_filename,'r') as fi:
        dict = json.load(fi)
        alldicts.append(dict)