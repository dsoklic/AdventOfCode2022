f = open("day08/sample.txt")

lines = [ [int(c) for c in [*l.strip()]] for l in f.readlines() ] 

def visible_horizontal(y, reverse):
  global lines

  visible_in_line = 0

  max_height = -1

  if not reverse:
    range_used = range(len(lines[y]))
  else:
    range_used = range(-(len(lines[y])), 0)

  for x in range_used:
    height = lines[y][x]
    if height > max_height:
      visible_in_line += 1
      max_height = height
  
  return visible_in_line

def visible_vertical(x, reverse):
  global lines

  visible_in_line = 0

  max_height = -1

  if not reverse:
    range_used = range(len(lines))
  else:
    range_used = range(-(len(lines)), 0)

  for y in range_used:
    height = lines[y][x]
    if height > max_height:
      visible_in_line += 1
      max_height = height

  return visible_in_line

visible = 0

for i in range(len(lines)):
  visible += visible_vertical(i, False)
  visible += visible_vertical(i, True)

  visible += visible_horizontal(i, False)
  visible += visible_horizontal(i, True)

print(visible)