f = open("day03/input.txt")

lines = [x.strip() for x in f.readlines()]

ord_a = ord('a')
ord_A = ord('A')

sum = 0

for lines_3 in [lines[i:i+3] for i in range(0, len(lines), 3)]:
    line_sets = [set(x) for x in lines_3]

    joint_letters = line_sets[0].intersection(line_sets[1])
    joint_letters = joint_letters.intersection(line_sets[2])

    for letter in joint_letters:
        if letter.islower():
            points = ord(letter) - ord_a + 1
        else:
            points = ord(letter) - ord_A + 27
        
        sum += points

print(sum)