def main():
    file = open("day6.txt", "r")
    text = file.read()

    groups = text.split("\n\n")
    groups = [group.replace("\n", "") for group in groups]

    print(f"day 5 part one: {partone(groups)}")


def partone(groups):
    total_count = 0
    for group in groups:
        total_count += len(set(group))

    return total_count


if __name__ == "__main__":
    main()
