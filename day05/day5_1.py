import re

f = open("day05/input.txt")

field, instructions = f.read().split('\n\n')
field = field.split('\n')

stack_num = len(re.findall('(\d+)', field[-1]))
stacks = [ [] for _ in range(stack_num) ]

field.reverse()

for line in field[1:]:
    for i in range(stack_num):
        container = line[i*4 + 1].strip()

        if container:
            stacks[i].append(container)

instructions = re.findall('move (\d+) from (\d+) to (\d+)', instructions)

for instruction in instructions:
    amount, a, b = [int(x) for x in instruction]
    
    for _ in range(amount):
        stacks[b-1].append(stacks[a-1].pop())
    
print(''.join([x.pop() for x in stacks]))