bingo_nums = []
all_matrices = []

with open('day_4_file.txt') as file:
    lines = file.readlines()
    cur_matrix = []
    for line in lines:
        if not bingo_nums:  # first need to fill up bingo nums
            bingo_nums = [int(num) for num in line.strip().split(',')]
        else:
            if line == "\n":  # current matrix is done
                all_matrices.append(cur_matrix)
                cur_matrix = []
            else:
                cur_matrix.append([[int(num), 0] for num in line.strip().split()])

    all_matrices.append(cur_matrix)
    del all_matrices[0]  # delete first matrix, because its empty


def find_and_mark(matrix, num):
    """if first item in any number_tuple == bingo_num, change second item to 1"""
    for row in matrix:
        for number_tuple in row:
            if number_tuple[0] == num:
                number_tuple[1] = 1


def check_rows(matrix) -> bool:
    """return True if any of the rows has all 1s as second item in tuple"""
    for row in matrix:
        if all([item[1] for item in row]):
            return True
    return False


def unmarked_nums_sum(matrix) -> int:
    """sum all the first items of number_tuple, if second item in number_tuple is 0"""
    total_sum = 0
    for row in matrix:
        for number_tuple in row:
            if number_tuple[1] == 0:
                total_sum += number_tuple[0]

    return total_sum


--part1
for bingo_num in bingo_nums:
    for bingo_board in all_matrices:
        find_and_mark(bingo_board, bingo_num)
        # transpose matrix. Rows became columns and vice versa
        transposed_bingo_board = [[bingo_board[i][j] for i in range(len(bingo_board))] for j in range(len(bingo_board[0]))]

        if check_rows(bingo_board) or check_rows(transposed_bingo_board):
            total = unmarked_nums_sum(bingo_board)
            print('Winner found')
            print(total*bingo_num)
            break
    else:
        print('Did not find any winning bingo board')
        continue
    break  # executed only if Winner found

# --part2
for bingo_num in bingo_nums:
    for bingo_board in reversed(all_matrices):  # go backwards so its safe to delete in loop
        find_and_mark(bingo_board, bingo_num)
        # transpose matrix. Rows became columns and vice versa
        transposed_bingo_board = [[bingo_board[i][j] for i in range(len(bingo_board))] for j in range(len(bingo_board[0]))]

        if check_rows(bingo_board) or check_rows(transposed_bingo_board):
            print('Winner found, remove bingo_card')
            if len(all_matrices) > 1:
                all_matrices.remove(bingo_board)
            else:
                print('Last Winner found:')
                total = unmarked_nums_sum(bingo_board)
                print(total*bingo_num)
                break
    else:
        continue
    break
