f = open("2input.txt", "r")
scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
points = 0
for line in f:
    choices = line.split()
    choices[1].strip()
    op = choices[0]
    me = choices[1]
    points += scores[me]

    if op == "A" and me == "X":
        points += 3
    elif op == "A" and me == "Y":
        points += 6
    elif op == "B" and me == "Y":
        points += 3
    elif op == "B" and me == "Z":
        points += 6
    elif op == "C" and me == "Z":
        points += 3
    elif op == "C" and me == "X":
        points += 6

f.close()
print(points)
