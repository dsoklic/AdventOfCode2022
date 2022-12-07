f = open("day07/sample.txt")

lines = f.readlines()

cwd = []
fs = {'/': {}}

def get_current_dir_fs():
  global cwd
  global fs

  fs_to_return = fs
  for dir in cwd:
    fs_to_return = fs_to_return[dir]

  return fs_to_return

for line in lines:
  line = line.strip()
  if line[0] == '$': # command
    command = line[2:4]

    if command == 'cd':
      parameter = line[5:]
      if parameter == '..':
        cwd.pop()
      else:
        cwd.append(parameter)
    
    elif command == 'ls':
      pass
  else:
    # All lines have information about the file system
    current_fs = get_current_dir_fs()
    left, right = line.split(' ')

    if left == 'dir':
      current_fs[right] = {}
    else:
      current_fs[right] = int(left)

# Figure out all directory sizes
directory_sizes = {}

def getDirSize(key_list, dictionary):
  global directory_sizes

  size = 0

  for key, value in dictionary.items():
    new_key_list = key_list + [key]
    if type(value) is dict:
      size += getDirSize(new_key_list, value)
    else:
      size += value

  directory_sizes['/'.join(key_list)] = size

  return size

getDirSize([], fs)

print(directory_sizes)