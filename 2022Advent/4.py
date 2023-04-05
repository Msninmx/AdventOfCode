f = open("inputs/4input.txt", "r").read().splitlines()


def part_one(lines):
    # Get total of sets that are subsets
    total = 0
    for i in lines:
        hours = i.split(',')
        first = list(map(int, hours[0].split('-')))
        second = list(map(int, hours[1].split('-')))

        if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
            total += 1
    return total


def part_two(lines):
    # Get total of sets that have overlaps
    total = 0
    for i in lines:
        hours = i.split(',')
        first = list(map(int, hours[0].split('-')))
        second = list(map(int, hours[1].split('-')))
        first_hours = set(range(first[0], first[1] + 1))
        second_hours = set(range(second[0], second[1] + 1))

        if len(first_hours & second_hours) != 0:
            total += 1

    return total


print(part_one(f))
print(part_two(f))
