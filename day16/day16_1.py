import re
from dataclasses import dataclass

@dataclass
class Valve:
    name: str
    connections: list[str]
    flow_rate: int

f = open("day16/sample.txt")

valves = {}

for line in f.readlines():
    valves_list = re.findall('([A-Z]{2})', line)

    this_valve = valves_list[0]
    connections = valves_list[1:]

    flow = int(re.findall('(\d+)', line)[0])
    valves[this_valve] = Valve(this_valve, connections, flow)

print(valves)