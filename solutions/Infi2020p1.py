def octagon(sides):
    sum = 0
    for i in range(sides):
        sum += (sides * 3)
    j = sides
    while j != (sides * 3):
        sum += 2 * j
        j = j + 2
    return sum

print(octagon(100))

result = 0
r = 0
while (result < 17483970):
    result = octagon(r)
    r += 1

print(r)

