def main():
    file = open("day6.txt", "r")
    text = file.read()

    groups = text.split("\n\n")

    print(f"day 5 part one: {partone(groups)}")
    print(f"day 5 part two: {parttwo(groups)}")


def partone(groups):
    total_count = 0

    for group in groups:
        group = group.replace("\n", "")
        total_count += len(set(group))

    return total_count


def parttwo(groups):
    total_count = 0

    for group in groups:
        group = group.split("\n")
        group = list(map(set, group))
        total_count += len(group[0].intersection(*group))
    return total_count


if __name__ == "__main__":
    main()
