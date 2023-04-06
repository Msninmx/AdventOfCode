f = open("inputs/7input.txt", "r").read().splitlines()


def part_one(lines):
    sizes = {}
    current_dir = ""
    parent_dirs = []

    for line in lines:
        if line.startswith("$ ls") or line.startswith("dir"):
            continue
        if line.startswith("$ cd"):
            new_dir = line[5:]
            if new_dir == "..":
                parent_dirs.pop()
                current_dir = parent_dirs[-1]
            else:
                current_dir = f"{parent_dirs[-1]}_{new_dir}" if parent_dirs else new_dir
                if current_dir not in sizes:
                    sizes[current_dir] = 0
                # current_dir = parent_dirs[-1] + "_" + new_dir
                parent_dirs.append(current_dir)
        else:
            size, _ = line.split()
            size = int(size)

            for dir in parent_dirs:
                sizes[dir] += size

    total_size = sum(value for value in sizes.values() if value < 100000)
    return total_size


def part_two(lines):
    sizes = {}
    current_dir = ""
    parent_dirs = []

    for line in lines:
        if line.startswith("$ ls") or line.startswith("dir"):
            continue
        if line.startswith("$ cd"):
            new_dir = line[5:]
            if new_dir == "..":
                parent_dirs.pop()
                current_dir = parent_dirs[-1]
            else:
                current_dir = f"{parent_dirs[-1]}_{new_dir}" if parent_dirs else new_dir
                if current_dir not in sizes:
                    sizes[current_dir] = 0
                # current_dir = parent_dirs[-1] + "_" + new_dir
                parent_dirs.append(current_dir)
        else:
            size, _ = line.split()
            size = int(size)

            for dir in parent_dirs:
                sizes[dir] += size

    min = sizes["/"] - (70000000 - 30000000)
    smallest = 0

    for value in sizes.values():
        if value < min:
            continue
        else:
            if -value < smallest:
                smallest = value

    return smallest


print(part_one(f))
print(part_two(f))
