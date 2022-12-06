input = open("day06/input.txt").readline()

window_size = 14

for i in range(len(input)-window_size+1):
  window = input[i:i+window_size]

  if window_size == len(set(window)):
    print(i+window_size)
    break