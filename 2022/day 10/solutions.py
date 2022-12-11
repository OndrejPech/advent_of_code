def spirit_positions(x_value):
    return {x_value - 1, x_value, x_value + 1}


def get_row_col(cycle_num):
    row_num = cycle_num // 40
    col_num = cycle_num % 40
    return row_num, col_num


with open('input.txt', 'r') as file:
    lines = file.readlines()


counted_cycles = (20, 60, 100, 140, 180, 220)
signal_total = 0
x = 1
cycles = 0
valid_crt_indexes = []


for line in lines:

    # WET, code not refactored
    cycles += 1
    if cycles in counted_cycles:
        signal_total += cycles * x
    row, col = get_row_col(cycles-1)
    if col in spirit_positions(x):
        valid_crt_indexes.append((row, col))
    # END OF WET

    if line.startswith('a'):
        # WET, code not refactored
        cycles += 1
        if cycles in counted_cycles:
            signal_total += cycles * x
        row, col = get_row_col(cycles-1)
        if col in spirit_positions(x):
            valid_crt_indexes.append((row, col))
        # END OF WET

        value = int(line.split()[1])
        x += value

# part 1
print(signal_total)

# part 2
for row in range(6):
    for column in range(40):
        if (row, column) in valid_crt_indexes:
            char = '█'
        else:
            char = ' '
        print(char, end='')
    print(' ')
