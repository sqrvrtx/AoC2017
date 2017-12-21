p = 703
q = 516
a = lambda x: (x*16807)%2147483647
b = lambda x: (x*48271)%2147483647
c = lambda x: bin(x)[-16:]
val = 0
count = 0
while count <40000000:
    p, q = a(p) , b(q)
    if c(p) == c(q):
        val += 1
    count +=1

print val, count


