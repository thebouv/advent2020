from statistics import median
from math import ceil


def main():
    with open('day5.txt') as file:
        tickets = file.read().splitlines()
        print(f"highest seat id: {partone(tickets)}")


def partone(tickets):
    highest_seat = 0

    for ticket in tickets:
        boardingpass = get_boardingpass(ticket)
        if boardingpass["seat"] > highest_seat:
            highest_seat = boardingpass["seat"]

    return highest_seat


def daytwo():
    pass


def get_boardingpass(ticket):
    row = bsp_lookup(0, 127, 0, ticket[0:7])
    column = bsp_lookup(0, 7, 0, ticket[-3:])
    seat = row * 8 + column

    return {'row': row, 'column': column, 'seat': seat}


def bsp_lookup(low, high, pos, item):
    direction = item[pos]
    if (pos < len(item)-1):
        pos += 1
        if direction == 'F' or direction == 'L':
            high = ceil(median(range(low, high)))
            return bsp_lookup(low, high, pos, item)
        else:
            low = ceil(median(range(low, high))) + 1
            return bsp_lookup(low, high, pos, item)
    else:
        if direction == 'F' or direction == 'L':
            return low
        else:
            return high


if __name__ == "__main__":
    main()
