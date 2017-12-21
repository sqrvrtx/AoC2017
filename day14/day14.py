s = 'a0c2017'
z = lambda y: "{0:b}".format((int(y, 16))).zfill(4)[-4:]
a = ''.join([z(x) for x in s])

hasher = lambda x: '#' if x == '1' else '.'
print ''.join([hasher(x) for x in a])

