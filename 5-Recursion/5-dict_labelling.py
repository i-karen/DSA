import json
import math


# def label_children(child, label=1, chain_label="1"):
#     children = child.get("children", None)
#     if not children:
#         child["level"] = label
#         child["number"] = chain_label
#         return
#     else:
#         for c in children:
#             label_children(c, label+1, chain_label+"."+str(label+1))
#             c["level"] = label
#             c["number"] = chain_label

def label_children(child, label=1):
    unique_id = child["id"]
    children = child.get("children", None)
    if not children:
        child["level"] = label
        return
    else:
        child["level"] = label
        for c in children:
            label_children(c, label+1)
            

def numbering_children(child, number):
    unique_id = child["id"]
    children = child.get("children", None)
    if not children:
        child["number"] = number
        return
    else:
        child["number"] = number
        for i,c in enumerate(children):
            numbering_children(c, number+"."+str(i+1))
            
            


with open("input.json", "r") as f:
    data = json.load(f)


for i,output in enumerate(data):
    issue = output.get("issue", None)
    if issue:
        label_children(issue, 1)
        numbering_children(issue, str(i))

json_output = json.dumps(data)

with open("output.json", "w") as f:
    f.write(json_output)
