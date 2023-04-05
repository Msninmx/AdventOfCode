f = open("inputs/5input.txt", "r").read().splitlines()

stacks = {
    "1": ["B", "V", "S", "N", "T", "C", "H", "Q"],
    "2": ["W", "D", "B", "G"],
    "3": ["F", "W", "R", "T", "S", "Q", "B"],
    "4": ["L", "G", "W", "S", "Z", "J", "D", "N"],
    "5": ["M", "P", "D", "V", "F"],
    "6": ["F", "W", "J"],
    "7": ["L", "N", "Q", "B", "J", "V"],
    "8": ["G", "T", "R", "C", "J", "Q", "S", "N"],
    "9": ["J", "S", "Q", "C", "W", "D", "M"],
}


def part_one(lines, stacks):
    # Restack crates and get top crates
    stacks_one = {key: value[:] for key, value in stacks.items()}
    for i in lines:
        steps = [i.split()[num] for num in [1, 3, 5]]
        to = steps[2]
        fr = steps[1]
        am = int(steps[0])

        for _ in range(am):
            stacks_one[to].append(stacks_one[fr].pop())

    tops = ""
    for column in stacks_one.values():
        tops += column[-1]

    return tops


def part_two(lines, stacks):
    # Restack crates and get top crates, moving multiple crates
    stacks_two = {key: value[:] for key, value in stacks.items()}
    for i in lines:
        steps = [i.split()[num] for num in [1, 3, 5]]
        to = steps[2]
        fr = steps[1]
        am = int(steps[0])

        carry = stacks_two[fr][-am:]
        del stacks_two[fr][-am:]
        stacks_two[to] += carry

    tops = ""
    for column in stacks_two.values():
        tops += column[-1]

    return tops


print(part_one(f, stacks))
print(part_two(f, stacks))
