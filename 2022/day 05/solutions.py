import copy


def get_final_message(final_stacks: list) -> str:
    final_message = []
    for stack in final_stacks:
        final_message.append(stack[-1])

    return ''.join(final_message)


with open('input.txt', 'r') as file:
    stacks = []
    stacks_filled = False
    while True:
        line = file.readline()
        if not line:
            break

        line = line.rstrip()
        if line == '':
            stacks_filled = True
            stacks_2 = copy.deepcopy(stacks)  # make copy for second task
            continue

        if not stacks_filled:
            # i is number of stack, j is position of character on the line(on 1,5,9,13... are data)
            for i, j in enumerate(range(1, len(line), 4)):
                try:
                    stacks[i]
                except IndexError:
                    stacks.append([])
                char = line[j]
                if char != ' ' and not char.isdigit():
                    stacks[i].insert(0, char)
        else:  # START TO MOVE BOXES
            nums = [int(char) for char in line.split() if char.isdigit()]
            n_boxes, move_from, move_to = nums

            # for part 1
            for i in range(n_boxes):
                box = stacks[move_from - 1].pop()
                stacks[move_to - 1].append(box)

            # for part 2
            boxes_to_move = stacks_2[move_from - 1][-n_boxes:]
            stacks_2[move_from - 1] = stacks_2[move_from - 1][:-n_boxes]
            stacks_2[move_to - 1] = stacks_2[move_to - 1] + boxes_to_move

print(get_final_message(stacks))
print(get_final_message(stacks_2))
