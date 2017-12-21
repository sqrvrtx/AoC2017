import re

ls = []
with open('data.in', 'r') as f:
    lines = f.read().splitlines()

for line in lines: 
    dirty_line = re.search(r'(-?\d+,-?\d+,-?\d+).*<(-?\d+,-?\d+,-?\d+).*<(-?\d+,-?\d+,-?\d+)',line).groups()
    p,v,a =[[int(x) for x in x.split(',')] for x in dirty_line]
    print p,v,a
    for i in range(2):
        p[i] += (v[i] + a[i])
    ls.append(sum([abs(q) for q in p]))

print ls.index(min(ls))
# 362 is too high
