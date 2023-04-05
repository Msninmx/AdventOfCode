f = open("inputs/1input.txt", "r")

totals = []
total = 0

for line in f:
    if line != "\n":
        total += int(line)
    else:
        totals.append(total)
        total = 0
f.close()

totals.sort(reverse=True)

# Part 1: Elf with highest calories
print(totals[0])

# Part 2: Top 3 elves with highest calories
print(sum(totals[0:3]))
