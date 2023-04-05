f = open("4input.txt", "r")

total = 0
total_1 = 0

for line in f:
    hours = str(line).strip()
    hours = hours.split(',')
    first = hours[0].split('-')
    second = hours[1].split('-')
    first = list(map(int, first))
    second = list(map(int, second))

    print(first, second)

    if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
        print(True)
        total += 1

    first_hours = set(range(first[0], first[1] + 1))
    second_hours = set(range(second[0], second[1] + 1))

    if len(first_hours & second_hours) != 0:
        total_1 += 1


print(total)
print(total_1)
f.close()
