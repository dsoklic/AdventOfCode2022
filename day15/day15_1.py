import re
from dataclasses import dataclass

@dataclass
class Point:
  x: int
  y: int
  radius: int

def manhattan_distance(x1, y1, x2, y2):
  return abs(x1-x2) + abs(y1 - y2)

f = open("day15/input.txt")

points = []

limits = {}

for line in f.readlines():
  matches = re.findall("Sensor at x=([\-\d]+), y=([\-\d]+): closest beacon is at x=([\-\d]+), y=([\-\d]+)", line)[0]
  x1, y1, x2, y2 = [int(foo) for foo in matches]
  dist = manhattan_distance(x1, y1, x2, y2)

  if limits == {}:
    limits = {'left':x1,'right':x1,'up':y1,'down':y1}

  limits['left'] = min(limits['left'], x1-dist)
  limits['right'] = max(limits['right'], x1+dist)
  limits['up'] = min(limits['up'], y1-dist)
  limits['down'] = max(limits['down'], y1+dist)

  points.append(Point(x1, y1, dist))

locations = 0
analysed_y = 10
for analysed_x in range(limits['left'], limits['right'] + 1):
  for point in points:
    if manhattan_distance(analysed_x, analysed_y, point.x, point.y) <= point.radius:
      locations += 1
      break # ignore any duplicates

print(locations)
