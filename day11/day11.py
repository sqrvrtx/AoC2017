with open('data.in', 'r') as f:
    data = f.read()[:-1].split(',')

ne = lambda x,y: (x + 0.5, y + 0.5)
e = lambda x,y: (x + 1, y)
nw = lambda x,y: (x - 0.5, y + 0.5)
n = lambda x,y: (x, y + 1)
se = lambda x,y: (x + 0.5, y - 0.5)
sw = lambda x,y: (x - 0.5, y - 0.5)
w = lambda x,y: (x-1, y)
s = lambda x,y: (x, y - 1)
ls = []
def main(data):
    x, y = 0, 0
    for direction in data:
        f =  eval(direction)
        x, y =  f(x, y)
        ls.append(abs(x) + abs(y))
    return abs(x) + abs(y), max(ls)

"""
ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
"""
data1 = 'ne,ne,ne'.split(',') # is 3 steps away.
data2 = 'ne,ne,sw,sw'.split(',') # is 0 steps away (back where you started).
data3 = 'ne,ne,s,s'.split(',') # is 2 steps away (se,se).
data4 = 'se,sw,se,sw,sw'.split(',') # 3
print main(data1)
print main(data2)
print main(data3)
print main(data4)
print main(data) # 1043 too high, 522 is too low

