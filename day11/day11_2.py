import re
from functools import reduce

f = open("day11/input.txt")

data = f.read().split('\n\n')

monkies = []

def inspect(item, operation) -> int:
    operator, amount = operation

    if amount == 'old':
        amount = item
    else:
        amount = int(amount)

    match operator:
        case '+':
            item += amount
        case '-':
            item -= amount
        case '/':
            item /= amount
        case '*':
            item *= amount

    return int(item)

for monkey in data:
    monkey = monkey.split('\n')
    items = [int(x) for x in re.findall('(\d+)', monkey[1])]
    operation = re.findall('Operation: new = old ([+\-\*/]) (\d+|old)', monkey[2])[0]
    test_divisibility = int(re.findall('Test: divisible by (\d+)', monkey[3])[0])
    true_monkey = int(re.findall('If true: throw to monkey (\d+)', monkey[4])[0])
    false_monkey = int(re.findall('If false: throw to monkey (\d+)', monkey[5])[0])

    monkies.append({
        'items': items,
        'operation': operation,
        'test_divisibility': test_divisibility,
        'true_monkey': true_monkey,
        'false_monkey': false_monkey,
        'inspections': 0
    })

# Common devisor is the product of all devisibility test numbers
common_devisor = reduce((lambda x, y: x * y), [x['test_divisibility'] for x in monkies])

for _ in range(10000):
    for monkey in monkies:
        for item in monkey['items']:
            monkey['inspections'] += 1

            item = inspect(item, monkey['operation'])
            item = int(item) % common_devisor

            # Is divisible?
            if item % monkey['test_divisibility'] == 0:
                monkies[monkey['true_monkey']]['items'].append(item)
            else:
                monkies[monkey['false_monkey']]['items'].append(item)

        monkey['items'] = [] # threw everything away

activity_list = sorted([x['inspections'] for x in monkies], reverse=True)
print(activity_list[0] * activity_list[1])