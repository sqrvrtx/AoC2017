with open('data.in', 'r') as f:
    data = f.read()[:-1].split(',')

def p(d, var1, var2):
    idx1, idx2 = d.index(var1), d.index(var2)
    d[idx1], d[idx2] = d[idx2], d[idx1]
    return d

def s(d, num):
    num = num * -1
    d = d[num:] + d[:(num)]
    return d

def x(d, var1, var2):
    d[var1], d[var2] = d[var2], d[var1]
    return d

"""
s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
"""
inst = list('abcde')
res = s(inst, 1)
assert res == list('eabcd'), res
inst = list('eabcd')
res = x(inst, 3, 4)
assert res == list('eabdc'), res
inst = list('eabdc')
res = p(inst, 'e', 'b')
assert res == list('baedc'), res

def starter():
    return map(chr, range(ord('a'), ord('p') +1))

def process(val, res):
    if val.startswith('s'):
        res = s(res, int(val[1:]))
    else:
        a, b = val[1:].split('/')
        if val[0] == 'x':
            res = x(res, int(a), int(b))
        else:
            res = p(res, a, b)
    return res

def problem_1():
    res = starter()
    for val in data:
        res = process(val, res)

    print ''.join(res)

def problem_2():
    res = starter()
    len_data = len(data)

    for x in xrange(10000000):
        z = x % len_data
        res = process(data[z], res)
        if res == starter():
            break
    for x in xrange(10000000 % (x+1)):
        x = x % len_data
        res = process(data[x], res)
    print ''.join(res)


problem_1()
problem_2()


