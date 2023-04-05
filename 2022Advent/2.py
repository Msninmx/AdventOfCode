f = open("inputs/2input.txt", "r").read().splitlines()

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


def part_one(lines):
    # Return points based on win and choice
    points = 0
    for i in lines:
        choices = i.split()
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

    return points


def part_two(lines):
    # Return points based on win and choice
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

    for i in f:
        choices = i.split()
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

    return points


print(part_one(f))
print(part_two(f))
