def load_data():
    with open('data.txt', 'r') as f:
        return [int(x) for x in f.read().splitlines()]
data = [0, 3,  0,  1,  -3]
data = load_data()
def main(decrement=False):
    steps = 0
    pos = 0
    while 1:
        try:
            increment = data[pos]
            if increment >= 3 and decrement is True:
                data[pos] -= 1
            else:
                data[pos] += 1
            pos += increment
        except:
            break
        steps += 1
    print steps
main()
data = [0, 3,  0,  1,  -3]
data = load_data()
main(decrement=True)

