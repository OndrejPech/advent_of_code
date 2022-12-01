with open('day_2_file.txt') as file:
    lines = file.readlines()

commands = [line.strip().split() for line in lines]  # list of tuples

# --part1
horizontal = 0
vertical = 0

for item in commands:
    command = item[0]
    units = int(item[1])

    if command == 'forward':
        horizontal += units
    elif command == 'up':
        vertical -= units
    elif command == 'down':
        vertical += units

print(horizontal * vertical)


# --part2
horizontal = 0
vertical = 0
aim = 0

for item in commands:
    command = item[0]
    units = int(item[1])

    if command == 'forward':
        horizontal += units
        vertical += aim * units
    elif command == 'up':
        aim -= units
    elif command == 'down':
        aim += units

print(horizontal * vertical)
