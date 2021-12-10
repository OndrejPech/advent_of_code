from collections import deque

with open('day_10_file.txt') as file:
    lines = file.readlines()

duos = {'[': ']', '{': '}', '(': ')', '<': '>'}

stack = deque()
illegal_chars = []
incomplete_lines = []
for line in lines:
    chars = list(line.strip())
    for char in chars:
        if char in duos:  # is opening char
            stack.append(char)
        else:  # is closing char
            needed = duos[stack[-1]]
            if char == needed:
                stack.pop()
            else:  # corrupted line
                illegal_chars.append(char)
                stack.clear()
                break

    closing_chars = []
    while stack:  # incomplete line
        closing_char = duos[stack.pop()]
        closing_chars.append(closing_char)
    if closing_chars:
        incomplete_lines.append(closing_chars)

# -- part_1
bounty_points = {']': 57, '}': 1197, ')': 3,'>': 25137}
total_points = 0
for char, points in bounty_points.items():
    occurrence = illegal_chars.count(char)
    total_points += occurrence * points

print(total_points)

# --part_2
contest_points = {']': 2, '}': 3, ')': 1, '>': 4}
all_scores = []
for line in incomplete_lines:
    line_points = 0
    for char in line:
        line_points = line_points * 5 + contest_points[char]
    all_scores.append(line_points)

all_scores.sort()
index = len(all_scores)//2
print(all_scores[index])
