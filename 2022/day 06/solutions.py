with open('input.txt', 'r') as file:
    code = file.read()


def find_marker_end_position(marker_length):
    for i in range(len(code)):
        end_position = marker_length + i
        text = code[i:end_position]
        if len(set(text)) >= marker_length:
            return end_position


# part 1:
print(find_marker_end_position(marker_length=4))
# part 2
print(find_marker_end_position(marker_length=14))
