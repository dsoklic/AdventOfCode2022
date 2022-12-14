from itertools import pairwise, product

f = open("day14/input.txt")

stationary_points = set()

lines = []
for line in f.readlines():
  line = line.strip()
  edges = [a.split(',') for a in line.split(' -> ')]
  edges = [(int(a[0]),int(a[1])) for a in edges]
  lines.append(edges)

for line in lines:
  for a,b in pairwise(line):
    a1,a2 = a
    b1,b2 = b

    x_spread = list(range(min(a1,b1),max(a1,b1)+1))
    y_spread = list(range(min(a2,b2),max(a2,b2)+1))

    for it in product(x_spread,y_spread):
      stationary_points.add(it)

floor = max([y for x,y in stationary_points]) + 2

sand_count = 0

running = True

while running:
  sand_count += 1

  current = [500, 0]
  while True:
    if current[1] == floor - 1:
      stationary_points.add(tuple(current))
      break
    if (current[0], current[1]+1) not in stationary_points:
      current[1] += 1
    elif (current[0]-1, current[1]+1) not in stationary_points:
      current[0] -= 1
      current[1] += 1
    elif (current[0]+1, current[1]+1) not in stationary_points:
      current[0] += 1
      current[1] += 1
    else:
      # rest
      stationary_points.add(tuple(current))

      if (current[0],current[1]) == (500,0):
        running = False
      break

print(sand_count)