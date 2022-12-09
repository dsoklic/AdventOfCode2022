f = open("day09/input.txt")

def align_knots(previous, current):
    clone = current.copy()
    if previous['x'] == current['x']:
        if previous['y'] > current['y']:
            clone['y'] += 1
        else:
            clone['y'] -= 1
    elif previous['y'] == current['y']:
        if previous['x'] > current['x']:
            clone['x'] += 1
        else:
            clone['x'] -= 1
    else: # diagonal
        if previous['y'] > current['y']:
            clone['y'] += 1
        else:
            clone['y'] -= 1
        if previous['x'] > current['x']:
            clone['x'] += 1
        else:
            clone['x'] -= 1
    
    return clone


rope = [ {'x': 0, 'y': 0}.copy() for _ in range(10) ]

visited = set()

for instruction in f.readlines():
    dir, amount = instruction.strip().split(' ')
    
    for _ in range(int(amount)):
        match dir:
            case 'U':
                rope[0]['y'] += 1
            case 'D':
                rope[0]['y'] -= 1
            case 'L':
                rope[0]['x'] -= 1
            case 'R':
                rope[0]['x'] += 1

        for i in range(1, len(rope)):
            if not (rope[i-1]['x']-1 <= rope[i]['x'] <= rope[i-1]['x']+1) or not (rope[i-1]['y']-1 <= rope[i]['y'] <= rope[i-1]['y']+1):
                rope[i] = align_knots(rope[i-1], rope[i])
        
        visited.add((rope[-1]['x'], rope[-1]['y']))

print(len(visited))