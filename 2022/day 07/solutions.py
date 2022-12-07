with open('input.txt', 'r') as file:
    lines = file.readlines()

all_dirs = {'home': 0}
current_dir = ['home']

for line in lines:
    line = line.strip()
    if line[0] == '$':  # command
        if line[2:4] == 'cd':
            if line[5] == '/':  # move to home dir
                current_dir = ['home']
            elif line[5] == '.':  # move one level up
                current_dir.pop()
            else:  # move one level down
                new_dir = line[5:]
                current_dir.append(new_dir)
    else:
        if line[0:3] == 'dir':
            dir_name = line[4:]
            parents_dir = '/'.join(current_dir)
            new_dir = parents_dir + '/' + dir_name
            all_dirs[new_dir] = 0  # create new dir
        else:  # is a file
            size, file_name = line.split()
            size = int(size)
            # save size to all parents root:
            for i in range(len(current_dir)):
                path = '/'.join(current_dir[:len(current_dir)-i])
                all_dirs[path] += size

# part 1
dirs_under_100k = [size for size in all_dirs.values() if size < 100000]
print(sum(dirs_under_100k))

# part 2
total_space = 70000000
used_space = all_dirs['home']
free_space = total_space-used_space
space_needed_for_update = 30000000
need_to_delete = space_needed_for_update - free_space
dirs_over = [size for size in all_dirs.values() if size >= need_to_delete]
print(min(dirs_over))


