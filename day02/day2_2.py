f = open("day02/input.txt")

selection_score = {'X': 1, 'Y': 2, 'Z': 3}

# opponent moves: A for Rock, B for Paper, and C for Scissors
# player moves: X for Rock, Y for Paper, and Z for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

winning_moves = {'A':'Y', 'B': 'Z', 'C': 'X'}
tie_moves = {'A':'X', 'B': 'Y', 'C': 'Z'}
losing_moves = {'A':'Z', 'B': 'X', 'C': 'Y'}

lines = [x.strip().split(' ') for x in f.readlines()]

score = 0

for line in lines:
    outcome = line[-1]

    if outcome == 'Z':
        player_move = winning_moves[line[0]]
        score += 6
    elif outcome == 'Y':
        player_move = tie_moves[line[0]]
        score += 3
    else:
        player_move = losing_moves[line[0]]

    score += selection_score[player_move]
    


print(score)