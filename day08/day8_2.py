f = open("day08/input.txt")

lines = [ [int(c) for c in [*l.strip()]] for l in f.readlines() ] 

max_score = 0

def count_visible(trees, max_height):
  count = 0

  for tree in trees:
    count += 1
    if tree >= max_height:
      break
    
  return count

for x in range(len(lines)):
  for y in range(0, len(lines)):
    current = lines[y][x]

    vertical_slice = [ lines[i][x] for i in [i for i in range(len(lines))] ]

    view_left = lines[y][0:x]
    view_right = lines[y][x+1:len(lines)]
    view_up = vertical_slice[0:y]
    view_down = vertical_slice[y+1:len(lines)]

    view_left.reverse()
    view_up.reverse()

    # Don't count hidden trees higher than current tree
    score = count_visible(view_left, current)
    score *= count_visible(view_right, current)
    score *= count_visible(view_up, current)
    score *= count_visible(view_down, current)

    if score > max_score:
      max_score = score

print(max_score)