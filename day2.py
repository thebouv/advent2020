with open('day2.txt') as file:
    passwords = file.read().splitlines()

valid = 0
invalid = 0

for line in passwords:
    elements = line.split()
    min, max = map(int, elements[0].split('-'))
    letter = elements[1].replace(':', '')
    password = elements[2]

    count = password.count(letter)

    if count < min or count > max:
        invalid += 1
    else:
        valid += 1

print(f"invalid passwords: {invalid}")
print(f"valid passwords: {valid}")
