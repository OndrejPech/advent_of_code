def is_visible_in_row(index: int, trees: list) -> bool:
    tree = trees[index]
    one_side = trees[:index]
    second_side = trees[index + 1:]
    if max(one_side) < tree or max(second_side) < tree:
        return True
    return False


def count_visible_distance(size, trees) -> int:
    distance = 0
    if len(trees) == 0:
        return 0
    for tree in trees:
        distance += 1
        if tree >= size:
            return distance
    return distance


grid = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

    # fill grid
    for line in lines:
        grid.append([int(num) for num in line.strip()])

n_rows = len(grid)
n_columns = len(grid[0])

# swap rows and columns
transposed_grid = [[grid[j][i] for j in range(len(grid))] for i in
                   range(len(grid[0]))]

# PART 1
total_visible = 0
for i in range(n_rows):
    for j in range(n_columns):
        if i == 0 or j == 0 or i == n_rows - 1 or j == n_columns - 1:  # edges
            total_visible += 1
        elif is_visible_in_row(j, grid[i]):  # check row
            total_visible += 1
        elif is_visible_in_row(i, transposed_grid[j]):  # check columns( rows in transposed)
            total_visible += 1

print(total_visible)

# PART 2
highest_index = 0
for i in range(n_rows):
    for j in range(n_columns):
        tree_row = grid[i]
        tree_column = transposed_grid[j]
        current_tree = tree_row[j]
        left_trees = tree_row[:j]
        right_trees = tree_row[j + 1:]
        upper_trees = tree_column[:i]
        down_trees = tree_column[i + 1:]
        # need to swap ordering to count from the closest tree
        upper_distance = count_visible_distance(current_tree, upper_trees[::-1])
        # need to swap ordering to count from the closest tree
        left_distance = count_visible_distance(current_tree, left_trees[::-1])
        down_distance = count_visible_distance(current_tree, down_trees)
        right_distance = count_visible_distance(current_tree, right_trees)
        visibility_index = upper_distance * left_distance * down_distance * right_distance
        if visibility_index > highest_index:
            highest_index = visibility_index

print(highest_index)
