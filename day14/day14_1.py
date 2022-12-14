from dataclasses import dataclass
from itertools import pairwise

@dataclass
class Point:
  x: int
  y: int

f = open("day14/sample.txt")

stationary_points = set()

lines = []
for line in f.readlines():
  line = line.strip()
  edges = [a.split(',') for a in line.split(' -> ')]
  edges = [(int(a[0]),int(a[1])) for a in edges]
  lines.append(edges)

for line in lines:
  for a,b in pairwise(line):
    print(a, b)

    