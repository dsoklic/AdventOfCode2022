from queue import PriorityQueue
from math import inf
from dataclasses import dataclass, field

@dataclass(order=True)
class PathItem:
    path_len: int
    position: list=field(compare=False)

f = open("day12/input.txt")

pq = PriorityQueue()
lines = [ [ord(c) for c in [*l.strip()]] for l in f.readlines() ]
visited = set()

distances = [ [inf for _ in range(len(lines[0]))] for _ in range(len(lines)) ]

def find(char, sub):
    global lines

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == ord(char):
                lines[y][x] = ord(sub)
                return (x, y)

def get_possible_neighbors(pos):
    global lines
    global pq

    x, y = pos
    height = lines[y][x]
    options = []

    if x > 0 and lines[y][x-1] <= height+1 and (x-1,y) not in visited and distances[y][x-1] == inf:
        options.append((x-1,y))
    if x < len(lines[0])-1 and lines[y][x+1] <= height+1 and (x+1,y) not in visited and distances[y][x+1] == inf:
        options.append((x+1,y))
    if y > 0 and lines[y-1][x] <= height+1 and (x, y-1) not in visited and distances[y-1][x] == inf:
        options.append((x, y-1))
    if y < len(lines)-1 and lines[y+1][x] <= height+1 and (x,y+1) not in visited and distances[y+1][x] == inf:
        options.append((x,y+1))

    return options

# find start
start = find('S', 'a')
end = find('E', 'z')

pq.put(PathItem(0, start))

while not pq.empty():
    item = pq.get()

    x, y = item.position
    distances[y][x] = item.path_len

    if item.position == end:
        print(item.path_len)
        break

    options = get_possible_neighbors(item.position)

    for opt in options:
        visited.add(opt)
        pq.put(PathItem(item.path_len + 1, opt))
