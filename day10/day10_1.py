f = open("day10/input.txt")

cycle = 1
noted_values = []
x = 1

def note_value_and_increase_cycle():
    global cycle
    global noted_values

    cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        noted_values.append(x*cycle)
    

for line in f.readlines():
    split_up = line.strip().split(' ')
    cmd = split_up[0]

    if cmd != "noop":
        amount = int(split_up[1])
    
    match cmd:
        case 'addx':
            note_value_and_increase_cycle()
            x += amount
            note_value_and_increase_cycle()
        case 'noop':
            note_value_and_increase_cycle()

print(sum(noted_values))
