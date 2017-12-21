import re
from collections import defaultdict

with open('data.in', 'r') as f:
    lines  = [re.search(r'(\S+) (inc|dec) (-?\d+) if (.*)', s).groups()  for s in f.read().splitlines()]

# ('cxz', 'inc', '-20', 'cxz == 10')
d = defaultdict(int)
[d[z] for z in  list(set([x[0] for x in lines]))]

print d

for line in lines:
    if eval(line[3]):
        if line[1] == 'inc':
            d[line[0]] += int(line[2]) 
        else: 
            d[line[0]] -= int(line[2])

print max(d.values())  


