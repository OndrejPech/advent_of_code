def get_priority_num(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

# part 1
with open('input.txt', 'r') as file:
    total = 0
    while True:
        line = file.readline()
        if not line:
            break

        # split code into two rucksack
        line = line.rstrip()
        half = int(len(line)/2)
        rucksack_1 = line[:half]
        rucksack_2 = line[half:]

        # add priority number of common element to total
        for letter in rucksack_1:
            if letter in rucksack_2:
                total += get_priority_num(letter)
                break
    print(total)

# part 2
with open('input.txt', 'r') as file:
    total = 0
    rucksack_1 = ''
    rucksack_2 = ''
    rucksack_3 = ''
    line_num = 1
    while True:
        line = file.readline()
        if not line:
            break

        modulo = line_num % 3
        rucksack = line.rstrip()
        if modulo == 1:
            rucksack_1 = rucksack
        elif modulo == 2:
            rucksack_2 = rucksack
        else:
            rucksack_3 = rucksack

            # find common element
            for letter in rucksack_1:
                if letter in rucksack_2 and letter in rucksack_3:
                    total += get_priority_num(letter)
                    break

        line_num += 1

    print(total)
