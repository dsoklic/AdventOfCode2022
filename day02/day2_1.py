f = open("day02/input.txt")

selection_score = {'X': 1, 'Y': 2, 'Z': 3}

# opponent moves: A for Rock, B for Paper, and C for Scissors
# player moves: X for Rock, Y for Paper, and Z for Scissors

winning_moves = [['A','Y'], ['B', 'Z'], ['C', 'X']]
tie_moves = [['A','X'], ['B', 'Y'], ['C', 'Z']]

lines = [x.strip().split(' ') for x in f.readlines()]

score = 0

for line in lines:
    score += selection_score[line[-1]]
    if line in winning_moves:
        score += 6
    elif line in tie_moves:
        score += 3


print(score)