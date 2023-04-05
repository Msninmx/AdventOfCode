f = open("3input.txt", "r")

values = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

total = 0

for line in f:
    line = str(line).strip()
    first = set(list(line[:len(line) // 2]))
    second = set(list(line[len(line) // 2:]))

    unique = min(first & second)
    total += values[unique[0]]

print(total)
f.close()

f = open("3input.txt", "r")
total_1 = 0
while True:
    first = set(list(str(f.readline()).strip()))
    if not first:
        break
    second = set(list(str(f.readline()).strip()))
    third = set(list(str(f.readline()).strip()))
    # print(first, second, third)

    unique = min(first & second & third)
    print(unique)
    total_1 += values[unique]

print(total_1)
f.close()
