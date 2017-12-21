import csv

def load_data():
    total = 0
    with open('data.tab', 'rb') as f:
        for line in csv.reader(f, delimiter='\t'):
            yield [int(x) for x in line]


def divisor(line):
    sorted_line = sorted(line, reverse=True)
    line_length = len(sorted_line)
    for x in range(line_length):
        for y in sorted_line[x+1:]:
            if sorted_line[x]%y == 0:
                return sorted_line[x]/y


def main(lol):
    print sum(divisor(line) for line in lol)


if __name__ =="__main__":
    lol = list(load_data())
    main(lol)
    ls = [[5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5]]
    main(ls)
