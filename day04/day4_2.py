f = open("day04/input.txt")

lines = [x.strip() for x in f.readlines()]

count = 0

for line in lines:
    a, b = line.split(',')

    a1, a2 = [int(x) for x in a.split('-')]
    b1, b2 = [int(x) for x in b.split('-')]

    a = set(range(a1, a2+1))
    b = set(range(b1, b2+1))

    if len(a.intersection(b)):
        count += 1

print(count)