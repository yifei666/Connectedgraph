import glob
import json


read_files = glob.glob("*.json")
main_object = {}
for f in read_files:
    with open(f, 'r') as current_file:
        raw = current_file.read()
        current_object = json.loads(raw)
        main_object.append(current_object)
with open("merged_link.json", "w") as outfile:
    raw = json.dumps(main_object, indent=4, sort_keys=True)
    outfile.write(raw)
    outfile.close()