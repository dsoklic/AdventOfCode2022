f = open("day03/input.txt")

lines = [x.strip() for x in f.readlines()]

ord_a = ord('a')
ord_A = ord('A')

sum = 0

for line in lines:
    half_point = int(len(line)/2)
    first_half = set(line[:half_point])
    second_half = set(line[half_point:])

    joint_letters = first_half.intersection(second_half)

    for letter in joint_letters:
        if letter.islower():
            points = ord(letter) - ord_a + 1
        else:
            points = ord(letter) - ord_A + 27
        
        sum += points

print(sum)