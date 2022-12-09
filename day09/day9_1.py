f = open("day09/input.txt")

head = {'x': 0, 'y': 0}
tail = {'x': 0, 'y': 0}

visited = set()

for instruction in f.readlines():
    dir, amount = instruction.strip().split(' ')
    
    for _ in range(int(amount)):
        previous_head = head.copy()

        match dir:
            case 'U':
                head['y'] += 1
            case 'D':
                head['y'] -= 1
            case 'L':
                head['x'] -= 1
            case 'R':
                head['x'] += 1
        
        if not (head['x']-1 <= tail['x'] <= head['x']+1) or not (head['y']-1 <= tail['y'] <= head['y']+1):
            tail = previous_head
        
        visited.add((tail['x'], tail['y']))

print(len(visited))