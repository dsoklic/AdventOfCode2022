import re
from dataclasses import dataclass
from itertools import chain

@dataclass
class Point:
  x: int
  y: int
  radius: int

def manhattan_distance(x1, y1, x2, y2):
  return abs(x1-x2) + abs(y1 - y2)

f = open("day15/input.txt")

points = []
beacons = set()
limits = {}

for line in f.readlines():
  matches = re.findall("Sensor at x=([\-\d]+), y=([\-\d]+): closest beacon is at x=([\-\d]+), y=([\-\d]+)", line)[0]
  x1, y1, x2, y2 = [int(foo) for foo in matches]
  dist = manhattan_distance(x1, y1, x2, y2)

  beacons.add((x2, y2))

  if limits == {}:
    limits = {'left':x1,'right':x1,'up':y1,'down':y1}

  limits['left'] = min(limits['left'], x1-dist)
  limits['right'] = max(limits['right'], x1+dist)
  limits['up'] = min(limits['up'], y1-dist)
  limits['down'] = max(limits['down'], y1+dist)

  points.append(Point(x1, y1, dist))

max_XY = 4000000

points_to_check = None

for sensor in points:
  x_span_neg = range(sensor.x - sensor.radius - 1, sensor.x+1)
  y_span_neg = range(sensor.y - sensor.radius - 1, sensor.y+1)
  x_span_pos = range(sensor.x, sensor.x + sensor.radius + 2)
  y_span_pos = range(sensor.y, sensor.y + sensor.radius + 2)

  top_right = zip(x_span_pos, y_span_neg)
  bottom_right = zip(reversed(x_span_pos), y_span_pos)
  top_left = zip(x_span_neg, y_span_pos)
  bottom_left = zip(x_span_neg, y_span_neg)

  if points_to_check is None:
    points_to_check = chain(top_right,bottom_right,top_left,bottom_left)
  else:
    points_to_check = chain(points_to_check,top_right,bottom_right,top_left,bottom_left)
  
for test_x, test_y in points_to_check:
  if test_x < 0 or test_x > max_XY or test_y < 0 or test_y > max_XY:
    continue

  found_outlier = True
  for sensor2 in points:
    if manhattan_distance(test_x, test_y, sensor2.x, sensor2.y) <= sensor2.radius:
      found_outlier = False
      break
  
  if found_outlier:
    print(test_x, test_y)
    print(test_x * 4000000 + test_y)
    break
  