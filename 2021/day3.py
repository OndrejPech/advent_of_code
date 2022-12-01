import numpy

matrix_list = []

# save each line as new list into matrix_list
with open('day_3_file.txt') as file:
    lines = file.readlines()
    for line in lines:
        digits = [int(digit) for digit in line.strip()]
        matrix_list.append(digits)

# # --part1
arr = numpy.array(matrix_list)
length = len(arr)
column_sums = arr.sum(axis=0)  # sum of each column

# if sum of column / len(array) > 0.5, than result is 1 else 0
b_result = [round(c_sum / length) for c_sum in column_sums]
# switch 0 and 1
opposite_b_result = [(1-num) for num in b_result]

# convert list of integers into string
binary_gamma_rate = ''.join(map(str, b_result))
binary_epsilon_rate = ''.join(map(str, opposite_b_result))

# convert binary to int
gama_rate = int(binary_gamma_rate,2)
epsilion_rate = int(binary_epsilon_rate,2)

print(gama_rate * epsilion_rate)


# # --part2
def find_the_row(matrix, c_num:int, reverse=False) -> list:
    # base case
    if len(matrix) == 1:
        return matrix[0]

    # recursion case
    column_sum = matrix[:, c_num].sum()
    ratio = column_sum / len(matrix)

    if ratio == 0.5:  # 0.5 is rounded to 0 by default
        most_binary = 1
    else:
        most_binary = round(ratio)

    if reverse:  # looking for less_common number
        most_binary = 1 - most_binary # switch all binary numbers

    # only rows where index [c_num] == most_binary
    new_arr = matrix[matrix[:, c_num] == most_binary]
    return find_the_row(new_arr, c_num+1, reverse=reverse)


arr = numpy.array(matrix_list)

b_result_OGR = find_the_row(arr, 0)
b_result_CO2= find_the_row(arr,0,reverse =True)

# convert list of integers into string
binary_OGR = ''.join(map(str, b_result_OGR))
binary_CO2 = ''.join(map(str, b_result_CO2))

# convert binary to int
oxygen_generator_rating = int(binary_OGR, 2)
co2_scrubber_rating = int(binary_CO2, 2)

print(oxygen_generator_rating * co2_scrubber_rating)
