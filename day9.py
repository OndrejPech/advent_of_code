def get_neighbours(i, j):
    """get values of all neighbours, 99 if no neighbour in that direction"""
    # I use 99 instead of None, because I am sure that there no two digit number
    upper = matrix[i-1][j] if i != 0 else 99
    lower = matrix[i+1][j] if i != n_rows-1 else 99
    left = matrix[i][j-1] if j != 0 else 99
    right = matrix[i][j+1] if j != n_columns-1 else 99

    return left, right, upper, lower


def count_basins(point):
    """
    update count point in case that any neighbour is higher
    in that case, move recursively to that neighbour
    """
    global count
    i = point[0]
    j = point[1]
    point_value = matrix[i][j]

    # if left_point_value > point value, but not 9, move left
    next_point = (i, j-1)
    if j != 0 and 9 > matrix[i][j-1] > point_value and next_point not in visited_points:
        count += 1
        visited_points.append(next_point)
        count_basins(next_point)

    # if bellow_point_value > point value, but not 9, move down
    next_point = (i+1, j)
    if i != n_rows-1 and 9 > matrix[i+1][j] > point_value and next_point not in visited_points:
        count += 1
        visited_points.append(next_point)
        count_basins(next_point)

    # if right_point_value > point value, but not 9 ,move right
    next_point = (i, j+1)
    if j != n_columns-1 and 9 > matrix[i][j+1] > point_value and next_point not in visited_points:
        count += 1
        visited_points.append(next_point)
        count_basins(next_point)

    # if upper_point_value > point value, but not 9,move up
    next_point = (i-1, j)
    if i != 0 and 9 > matrix[i-1][j] > point_value and next_point not in visited_points:
        count += 1
        visited_points.append(next_point)
        count_basins(next_point)

    # base case, if no neighbour is higher
    return count


# fill up matrix
matrix = []
with open('day_9_file.txt') as file:
    for line in file:
        matrix.append([int(num) for num in line.strip()])

# size of created matrix
n_rows = len(matrix)
n_columns = len(matrix[0]) if matrix else 0

# --part1
locations_of_low_points = []
low_points =[]
for r, row in enumerate(matrix):
    for c, column in enumerate(row):
        num = matrix[r][c]
        neighbours = get_neighbours(r, c)
        if num < min(neighbours):
            low_points.append(num)
            locations_of_low_points.append((r,c))

print(sum(low_points)+len(low_points))


# --part2
all_basins_values = []
for low_point in locations_of_low_points:
    visited_points = []
    count = 1  # starting count
    count_basins(low_point)  # change the count variable
    all_basins_values.append(count)

top3 = sorted(all_basins_values, reverse=True)[:3]
print(top3[0] * top3[1] * top3[2])
