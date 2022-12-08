import itertools

f = open("day08/input.txt")

lines = [ [int(c) for c in [*l.strip()]] for l in f.readlines() ] 

visible = 4 * len(lines) - 4

for x in range(1, len(lines)-1):
  for y in range(1, len(lines)-1):
    current = lines[y][x]

    vertical_slice = [ lines[i][x] for i in [i for i in range(len(lines))] ]

    # Check if this is the tallest tree to the left
    tallest_left = all([tree < current for tree in lines[y][0:x]])
    tallest_right = all([tree < current for tree in lines[y][x+1:len(lines)]])
    tallest_up = all([tree < current for tree in vertical_slice[0:y]])
    tallest_down = all([tree < current for tree in vertical_slice[y+1:len(lines)]])

    if tallest_left or tallest_right or tallest_up or tallest_down:
      visible += 1

print(visible)