f = open("day01/input.txt")

lines = [x.strip() for x in f.readlines()]

elves = [0]
index = 0
tops = [0, 0, 0]

for l in lines:
    if l:
        elves[index] += int(l)
    else:
        index += 1
        elves.append(0)

print(elves)
print(max(elves))