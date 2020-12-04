with open('day3.txt') as file:
    lines = file.read().splitlines()


def main():
    slope1 = findtrees(1, 1)
    slope2 = findtrees(3, 1)
    slope3 = findtrees(5, 1)
    slope4 = findtrees(7, 1)
    slope5 = findtrees(1, 2)

    print(f"part 1: {slope2}")

    print(f"part 2: {slope1*slope2*slope3*slope4*slope5}")


def findtrees(rateX, rateY):
    xpos = 0
    ypos = 0
    trees = 0
    maxpos = len(lines[0]) - 1
    botpos = len(lines) - 1

    while ypos < botpos:
        xpos += rateX
        ypos += rateY

        if ypos > botpos:
            break

        if xpos > maxpos:
            xpos = xpos - maxpos - 1

        if lines[ypos][xpos] == '#':
            trees += 1

    return trees


if __name__ == "__main__":
    main()
