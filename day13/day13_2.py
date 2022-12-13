import json
from functools import cmp_to_key

f = open("day13/input.txt")

data = f.read().split('\n')
data = [json.loads(l) for l in list(filter(lambda x: x, data))]

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

data.append([[2]])
data.append([[6]])

data = sorted(data, key=cmp_to_key(compare))

first = data.index([[2]]) + 1
second = data.index([[6]]) + 1

print(first * second)