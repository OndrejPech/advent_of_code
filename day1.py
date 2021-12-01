with open('day_1_file.txt') as file:
    lines = file.readlines()

nums = [int(line.strip()) for line in lines]

# --part1
increased = 0
last_depth = nums[0]
for num in nums:
    if num > last_depth:
        increased += 1

    last_depth = num

print(increased)

# --part2
length = len(nums)
increased_trips = 0
for i in range(length):
    if i in (0, length-1, length-2):
        continue
    if nums[i-1] < nums[i+2]:
        increased_trips += 1

print(increased_trips)
