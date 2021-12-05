def create_all_points(x1, y1, x2, y2, constant_axis: str) -> list:
    """create list of tuples, with all point between start_point and end_point"""
    all_points = []
    if constant_axis == 'y':  # horizontal line
        start = x1
        end = x2
        if start > end:
            start, end = end, start
        for i in range(start, end+1):
            all_points.append((i, y1))
    elif constant_axis == 'x':  # vertical line
        start = y1
        end = y2
        if start > end:
            start, end = end, start
        for i in range(start, end+1):
            all_points.append((x1, i))

    return all_points


def create_all_points_in_diagonals(x1, y1, x2, y2, num: int) -> list:
    """create list of tuples, with all point between start_point and end_point"""
    if x1 > x2:  # switch start_point[x1,y1] and end_point[x2,y2]
        x1, y1, x2, y2 = x2, y2, x1, y1

    diff = x2 - x1
    all_points = []
    for i in range(diff+1):
        # increase x, and increase y only if num is positive,else decrease
        all_points.append((x1 + i, y1 + (num*i)))

    return all_points


# load all data
all_lines = []
with open('day_5_file.txt') as file:
    lines = file.readlines()
    for line in lines:
        both_points = line.split(' -> ')
        first_point_strings = both_points[0].split(',')
        second_point_strings = both_points[1].split(',')
        first_point = [int(item) for item in first_point_strings]
        second_point = [int(item) for item in second_point_strings]
        all_lines.append([first_point, second_point])


# --part1
# create all points as tuples in matrix
all_points_in_matrix = []
for line in all_lines:
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    if x1 == x2:  # vertical
        all_points_in_line = create_all_points(x1, y1, x2, y2, 'x')
    elif y1 == y2:  # horizontal
        all_points_in_line = create_all_points(x1, y1, x2, y2, 'y')
    else:  # points are not on the same x or y line
        all_points_in_line = []
    all_points_in_matrix.extend(all_points_in_line)

# count how many times each point is in matrix
counts = {}
for point in all_points_in_matrix:
    counts[point] = counts.get(point, 0) + 1

# keep only points, where count is at least 2
overlap_points = [point for point, count in counts.items() if count > 1]
print(len(overlap_points))


# --part2
# create all points as tuples in matrix
all_points_in_matrix = []
for line in all_lines:
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    if x1 == x2:  # vertical
        all_points_in_line = create_all_points(x1, y1, x2, y2, 'x')
    elif y1 == y2:  # horizontal
        all_points_in_line = create_all_points(x1, y1, x2, y2, 'y')
    elif x2 - x1 == y2 - y1:  # positive diagonal
        all_points_in_line = create_all_points_in_diagonals(x1, y1, x2, y2, 1)
    elif x1 - x2 == y2-y1:  # negative diagonal
        all_points_in_line = create_all_points_in_diagonals(x1, y1, x2, y2, -1)
    else:  # lines are not horizontal, vertical or diagonal
        all_points_in_line = []
    all_points_in_matrix.extend(all_points_in_line)

# count how many times each point is in matrix
counts = {}
for point in all_points_in_matrix:
    counts[point] = counts.get(point, 0) + 1

# keep only points, where count is at least 2
overlap_points = [point for point, count in counts.items() if count > 1]
print(len(overlap_points))
