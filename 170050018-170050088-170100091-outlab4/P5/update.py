#! /usr/bin/python3
import json

# with open("infinity_stones.json","r") as abc, open("update_stones.json","w") as to:
#    to.write(abc.read())

with open("infinity_stones.json","r") as xyz:
    data=json.load(xyz)
    
for ele in data["Infinity Stones"]:
    ele["Containment Unit"]="Infinity Gauntlet"
        
with open("update_stones.json","w") as xyz:
    json.dump(data,xyz)
