with open('input.txt', 'r') as file:
    contains = 0
    overlaps = 0
    while True:
        line = file.readline()
        if not line:
            break

        # split line into two elfs
        first, second = line.rstrip().split(',')

        # create sections for both elfs
        begin, end = first.split('-')
        first_elf_sections = set(range(int(begin), int(end) + 1))
        begin, end = second.split('-')
        second_elf_sections = set(range(int(begin), int(end) + 1))

        # FIRST PART
        if first_elf_sections - second_elf_sections == set() or \
                second_elf_sections - first_elf_sections == set():
            contains += 1

        # SECOND PART
        if len(first_elf_sections & second_elf_sections) > 0:
            overlaps += 1

print(contains)
print(overlaps)
