import re
d = dict()
with open('data.in', 'r') as f:
    lines = f.read().splitlines()
    ls = [re.findall(r'\d+', s) for s in lines]
    for x in ls:
        d[x[0]] = x[1:]


print d['0']

zls = d['0']
ls = ['0']
def adder(z):
    for item in z:
       if item not in ls:
           ls.append(item)
       
           adder(d[item])

adder(zls)

print len(set(ls))
print set(ls)
print set(d.keys()) - set(ls)
groups = []
for k in d:
    ls = [k]
    adder(d[k])


