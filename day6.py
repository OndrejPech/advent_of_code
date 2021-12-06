with open('day_6_file.txt') as file:
    content = file.read()
    original = [int(num) for num in content.split(',')]

# --part1
nums = original
days = 80
for i in range(days):
    updated_nums = []
    zeros = 0
    for num in nums:
        if num == 0:
            zeros += 1
            updated_nums.append(6)
        else:
            updated_nums.append(num-1)

    # for each zero create new 8 on the end
    updated_nums.extend(zeros*[8])

    nums = updated_nums

print(len(nums))

#--part2
# create dictionary with counts of fish
all_fish = {'stage0': 0,
            'stage1': 0,
            'stage2': 0,
            'stage3': 0,
            'stage4': 0,
            'stage5': 0,
            'stage6': 0,
            'stage7': 0,
            'stage8': 0}

# update counts from file input
for days_left in original:
    key = f'stage{days_left}'
    all_fish[key] = all_fish.get(key, 0) + 1

days = 256
for day in range(days):
    # each fish decreases its stage
    # so num_of_fish_in_stage[i] -> num_of_fish_in_stage[i+1]
    # each stage0 goes to stage6 and create one extra stage8
    updated_dict = {'stage0': all_fish.get('stage1'),
                    'stage1': all_fish.get('stage2'),
                    'stage2': all_fish.get('stage3'),
                    'stage3': all_fish.get('stage4'),
                    'stage4': all_fish.get('stage5'),
                    'stage5': all_fish.get('stage6'),
                    'stage6': all_fish.get('stage7') + all_fish.get('stage0'),
                    'stage7': all_fish.get('stage8'),
                    'stage8': all_fish.get('stage0')
                    }

    all_fish = updated_dict

print(sum(all_fish.values()))

