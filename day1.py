import itertools

with open('day1.txt') as file:
    numbers1 = list(map(int, file.read().splitlines()))
    numbers2 = numbers1

for x, y in itertools.combinations(numbers1, 2):
    if (x + y) == 2020:
        print(f'{x},{y},{x+y},{x*y}')

for w, x, y in itertools.combinations(numbers2, 3):
    if (w + x + y) == 2020:
        print(f'{w},{x},{y},{w+x+y},{w*x*y}')
