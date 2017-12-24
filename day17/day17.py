from collections import deque

puzzle = 349
def spinner(num):
    spinlock = deque([0])
    for i in range(1, num+1):
        spinlock.rotate(-puzzle)
        spinlock.append(i)

    return spinlock

d1 = spinner(2017)
print("Part 1 {0}".format(d1[0]))

d2 = spinner(50000000)
print("Part 2 {0}".format(d2[d2.index(0) + 1]))
