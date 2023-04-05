f = open("1input.txt", "r")
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
print(totals[0:3])
print(sum(totals[0:3]))
