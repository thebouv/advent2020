with open('day2.txt') as file:
    passwords = file.read().splitlines()

invalid1 = 0
invalid2 = 0
valid1 = 0
valid2 = 0


def main():
    for line in passwords:
        elements = line.split()
        first, second = map(int, elements[0].split('-'))
        letter = elements[1].replace(':', '')
        password = elements[2]
        day1(first, second, letter, password)
        day2(first, second, letter, password)
        print(f"day 1 invalid passwords: {invalid1}")
        print(f"day 1 valid passwords: {valid1}")
        print(f"day 2 invalid passwords: {invalid2}")
        print(f"day 2 valid passwords: {valid2}")


def day1(first, second, letter, password):
    count = password.count(letter)

    if count < first or count > second:
        global invalid1
        invalid1 += 1
    else:
        global valid1
        valid1 += 1


def day2(first, second, letter, password):
    first -= 1
    second -= 1

    if (password[first] == letter or password[second] == letter) and not (password[first] == letter and password[second] == letter):
        global valid2
        valid2 += 1
    else:
        global invalid2
        invalid2 += 1


if __name__ == "__main__":
    main()
