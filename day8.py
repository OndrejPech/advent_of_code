
with open('day_8_file.txt') as file:
    lines = file.readlines()


# --part1
# outputs_only = [line.split('|')[1].strip() for line in lines]
#
# famous_instances = 0
# for output in outputs_only:
#     for signal in output.split():
#         if len(signal) in [2, 3, 4, 7]:
#             famous_instances += 1
#
# print(famous_instances)

# --part2
correct_patterns= {
                    0: {'a', 'b', 'c', 'e', 'f', 'g'},
                    1: {'c', 'f'},
                    2: {'a', 'c', 'd', 'e', 'g'},
                    3: {'a', 'c', 'd', 'f',  'g'},
                    4: {'b', 'c', 'd', 'f'},
                    5: {'a', 'b', 'd', 'f', 'g'},
                    6: {'a', 'b', 'd', 'e', 'f', 'g'},
                    7: {'a', 'c', 'f'},
                    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                    9: {'a', 'b', 'c', 'd', 'f', 'g'},
                   }

total = 0
for line in lines:
    signals_patterns = line.split('|')[0].strip()
    output_values = line.split('|')[1]

    a = b = c = d = e = f = g = None
    # sort signals to famous groups
    nums235 = []
    nums069 = []
    num1 = num7 = num4 = num8 = None
    for signal_pat in signals_patterns.split():
        if len(signal_pat) == 2:
            num1 = set(signal_pat)
        elif len(signal_pat) == 3:
            num7 = set(signal_pat)
        elif len(signal_pat) == 4:
            num4 = set(signal_pat)
        elif len(signal_pat) == 7:
            num8 = set(signal_pat)
        elif len(signal_pat) == 5:
            nums235.append(set(signal_pat))
        elif len(signal_pat) == 6:
            nums069.append(set(signal_pat))

    # we are sure what is a
    a = (num7 - num1).pop()
    # c and f are elements in num1, I put it randomly for now
    c_or_f = list(num1)
    c = c_or_f[0]
    f = c_or_f[1]
    # f is in all_nums except num2,
    # c is in all_nums except num5, num6

    # if c is is missing in others just once, than is not c, it is f
    if sum([(c not in s) for s in nums235+nums069]) == 1:
        c, f = f, c

    # b or d are the extra two in num4, I put the randomly for now
    b_or_d = list(num4-num1)
    b = b_or_d[0]
    d = b_or_d[1]

    # d is not in num0, so if b is missing once, than is not b, but d
    if sum([(b not in s) for s in nums069]) == 1:
        b, d = d, b

    # e and g are in num8 but not in num1,num4,num7, I match them randomly
    e_or_g = list(num8 - set(num1 | num4 | num7))
    e = e_or_g[0]
    g = e_or_g[1]

    # e is in num235 just once, if its more than is g
    if sum([(e in s) for s in nums235]) > 1:
        e, g = g, e

    vocabulary = {a: 'a', b: 'b', c: 'c', d: 'd', e: 'e', f: 'f', g: 'g'}

    line_num = ''
    for output_digit in output_values.split():
        # translate each output signal
        encrypted = ''
        for letter in output_digit:
            encrypted += vocabulary[letter]

        # find out the value of encrypted text and add next digit to cur_num
        for number, signal in correct_patterns.items():
            if set(encrypted) == signal:
                line_num += str(number)
                break

    total += int(line_num)

print(total)
