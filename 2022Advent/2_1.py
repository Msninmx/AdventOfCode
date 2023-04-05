f = open("2input.txt", "r")
wins = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
loses = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}
ties = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
scores = {
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

    if me == "X":
        points += 0
        points += scores[loses[op]]
    elif me == "Y":
        points += 3
        points += scores[ties[op]]
    elif me == "Z":
        points += 6
        points += scores[wins[op]]

print(points)
f.close()
