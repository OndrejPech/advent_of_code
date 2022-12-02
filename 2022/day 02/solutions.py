# Rock is A(opponent) or X(me), Paper is B or Y, Scissors is C or Z
points = {'X': {'shape_points': 1,
                'A': 3,
                'B': 0,
                'C': 6},
          'Y': {'shape_points': 2,
                'A': 6,
                'B': 3,
                'C': 0},
          'Z': {'shape_points': 3,
                'A': 0,
                'B': 6,
                'C': 3},
          }

# for part 2 only, find my value(shape) based on opponents shape and result
# key X is need of my lose, key Y is draw, key Z is need of my win
my_shape_dict = {'A': {'X': 'Z',
                       'Y': 'X',
                       'Z': 'Y'},
                 'B': {'X': 'X',
                       'Y': 'Y',
                       'Z': 'Z'},
                 'C': {'X': 'Y',
                       'Y': 'Z',
                       'Z': 'X'}
                 }


def get_points_for_one_game(opponent_shape, my_shape):
    shape_point = points[my_shape]['shape_points']
    won_point = points[me][opponent_shape]
    return shape_point + won_point


with open('input.txt', 'r') as file:
    total_points_part1 = 0
    total_points_part2 = 0
    while True:
        line = file.readline()
        if not line:
            break

        # part 1
        opponent, me = line.split()
        total_points_part1 += get_points_for_one_game(opponent, me)

        # part 2
        opponent, result = line.split()
        me = my_shape_dict[opponent][result]
        total_points_part2 += get_points_for_one_game(opponent, me)


print(total_points_part1)
print(total_points_part2)
