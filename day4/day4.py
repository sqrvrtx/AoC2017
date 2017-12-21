import re

def load_data(file_name, sort=False):
    with open(file_name, 'r') as f:
        for line in f.read().splitlines():
            words = re.findall(r'\w+', line)
            yield words if not sort else [''.join(sorted(x)) for x in words]


print sum((len(set(x))==len(x)) for x in load_data('data.txt'))
print sum((len(set(x))==len(x)) for x in load_data('data.txt', sort=True))

