file = open("Day2Input.txt")

lines = file.read().splitlines()

count = 0

for line in lines:
    vals = line.split(" ") # all input values
    limits = vals[0].split("-") # upper and lower lim for char
    char = vals[1][0] # character to check
    if (vals[2].count(char) >= int(limits[0]) and vals[2].count(char) <= int(limits[1])):
        count += 1

print(count)