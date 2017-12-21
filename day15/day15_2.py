p = 703
q = 516

def a(x, z=1):
    while z%4 != 0:
        x = (x*16807)%2147483647
        z=x
    return z

def b(x, z=1):
    while z%8 != 0:
        x = (x*48271)%2147483647
        z=x
    return z

   
c = lambda x: bin(x)[-16:]
val = 0
count = 0
while count <5000000:
    p, q = a(p) , b(q)
    if c(p) == c(q):
        val += 1
    count +=1

print val, count


