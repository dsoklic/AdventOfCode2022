import itertools

f = open("day08/input.txt")

lines = [ [int(c) for c in [*l.strip()]] for l in f.readlines() ] 

max_score = 0

for x in range(len(lines)):
  for y in range(0, len(lines)):
    current = lines[y][x]

    vertical_slice = [ lines[i][x] for i in [i for i in range(len(lines))] ]

    view_left = lines[y][0:x]
    view_right = lines[y][x+1:len(lines)]
    view_up = vertical_slice[0:y]
    view_down = vertical_slice[y+1:len(lines)]

    # Don't count hidden trees higher thatn current tree
