import json
import csv
import pandas as pd
f = open('Android.bp')
text = f.read()
raw = text.splitlines(True)
print(raw)

# A stack to hold the parsed objects
stack = [{}]

reader = csv.reader(raw, delimiter=' ', skipinitialspace=True)



for row in reader:
    #print(row)
    key = row[0]
    if key == '}':
        # The end of the current object
        stack.pop()
        continue
    if key[-1] == ':' :
        key = key[:-1]
    if key[0:2] == '//':
        continue
    val = row[-1]
    if val == '{':
        # A new subobject
        stack[-1][key] = d = {}
        stack.append(d)
    elif val[-1] == ',':
         val = val[:-1]
         stack[-1][key] = val
    else:
        # A line of plain data
        stack[-1][key] = val


out = json.dumps(stack[0], indent=4)
print(out)
