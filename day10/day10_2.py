f = open("day10/input.txt")

cycle = 1
x = 1

output = ''

def note_value_and_increase_cycle():
    global cycle
    global output

    # draw
    foo = list(range(x, x+3))
    pos = (cycle % 40) + 1
    if pos in range(x, x+3):
        output += '#'
    else:
        output += ' '

    cycle += 1
    

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

for i, c in enumerate(output):
    print(c, end='')

    i += 1

    if i%40 == 0:
        print()