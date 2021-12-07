from statistics import median

with open('day_7_file.txt') as file:
    content = file.read()
    crabs = [int(num) for num in content.split(',')]


#  part1
# median is the position to move
med = int(median(crabs))

# moves for each crab
moves = list(map(lambda x: abs(med-x), crabs))
print(sum(moves))


# part2
def total_fuel(position):
    """count fuel needed for all crabs if they move to this position"""
    total = 0
    for crab in crabs:
        distance = abs(crab-position)
        fuel = sum(range(distance+1))
        total += fuel

    # print(f'{position}|{total}')
    return total


# using binary search to find this position
low = min(crabs)
high = max(crabs)+1
while high-low > 1:
    middle = (high+low)//2
    if total_fuel(middle - 1) > total_fuel(middle):  # fuel needed decreasing
        # need to go to higher position
        low = middle
    else:  # fuel needed increasing
        # need to go to lower position
        high = middle

print(total_fuel(middle))
