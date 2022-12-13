import json
f = open("day13/input.txt")

data = f.read().split('\n\n')

# negative is right
# 0 is same
# positive is wrong
def compare(left, right):
    # print(left, right)

    if (type(left) is list) != (type(right) is list): # xor
        if type(left) is int:
            left = [left]
        else:
            right = [right]

    if type(left) is int and type(right) is int:
        return left - right
    
    if type(left) is list and type(right) is list:
        for i in range(max(len(left), len(right))):
            if i >= len(left): # left ran out
                return -1
            if i >= len(right): # right ran out
                return 1

            res = compare(left[i], right[i])
            if res != 0:
                return res

        return 0

comparisons = []

for i, pair in enumerate(data):
    i += 1

    l, r = pair.split('\n')
    l = json.loads(l)
    r = json.loads(r)

    res = compare(l, r)

    if res < 0:
        comparisons.append(i)

print(sum(comparisons))
