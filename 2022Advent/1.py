f = open("inputs/1input.txt", "r").read().splitlines()


def part_one(lines):
    # Take the sum of each group of calories, return the highest one
    totals = []
    total = 0
    for i in lines:
        if i != "":
            total += int(i)
        else:
            totals.append(total)
            total = 0
    totals.sort(reverse=True)
    return totals[0]


def part_two(lines):
    # Take the sum of each group of calories, return sum of highest 3
    totals = []
    total = 0
    for i in lines:
        if i != "":
            total += int(i)
        else:
            totals.append(total)
            total = 0
    totals.sort(reverse=True)
    return sum(totals[0:3])


print(part_one(f))
print(part_two(f))
