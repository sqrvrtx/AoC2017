data_str = "11  11  13  7   0   15  5   5   4   4   1   1   7   1   15  11"
data = [int(x) for x in data_str.split()]
print data
length = len(data)
cycles = [data]

def get_highest(data_input):
    z = [(x, i) for i,x in enumerate(data_input)]
    return sorted(z, key=lambda x: x[0], reverse=True)[0]

def distribute(data, highest, indx):
    data[indx] = 0
    for i in range(highest):
        try:
            data[indx+i] += 1
        except IndexError:
            data[i - (length - index)] += 1


while 1:
    highest, indx = get_highest(data)
    print highest, indx
    data = distribute(data, highest, indx)
    if data in cycles:
        break
    cycles.append(data)

print data, len(cycles) + 1

