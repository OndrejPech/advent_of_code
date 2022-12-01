with open('input.txt', 'r') as file:
    elve_num = 1
    all_elves = {}
    while True:
        line = file.readline()
        if not line:
            break
        line = line.rstrip()

        if line == '':
            elve_num += 1
        else:
            all_elves[elve_num] = all_elves.get(elve_num, 0) + int(line)


# PART 1
highest = max(all_elves.values())
print(highest)

# PART 2
top_three = sorted(all_elves.values(), reverse=True)[:3]
print(sum(top_three))
