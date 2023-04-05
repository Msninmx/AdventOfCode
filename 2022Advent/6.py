f = open("inputs/6input.txt", "r").read()


def part_one(line):
    # Get position of first occurence of unique group of 4 letters
    p1 = 0
    p2 = 1
    p3 = 2
    p4 = 3

    while p1 <= len(line) - 3:
        sample = set([line[p1], line[p2], line[p3], line[p4]])

        if len(sample) < 4:
            p1 += 1
            p2 += 1
            p3 += 1
            p4 += 1
        else:
            return p4 + 1


def part_two(line):
    # Get position of first occurence of unique group of 14 letters
    p1 = 0
    p2 = 14
    while p1 <= len(line) - 14:
        sample = set(line[p1:p2])

        if len(sample) < 14:
            p1 += 1
            p2 += 1
        else:
            return p2

print(part_one(f))
print(part_two(f))
