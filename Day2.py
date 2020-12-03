file = open("Day2Input.txt")

lines = file.read().splitlines()

count = 0

# part 1: toboggan password rule 1
for line in lines:
    vals = line.split(" ") # all input values
    limits = vals[0].split("-") # upper and lower lim for char
    char = vals[1][0] # character to check
    if (vals[2].count(char) >= int(limits[0]) and vals[2].count(char) <= int(limits[1])):
        count += 1
print("old system: " + str(count))

count = 0
# part 2: toboggan password rule 2
for line in lines:
    vals = line.split(" ") # all input values
    limits = vals[0].split("-") # upper and lower lim for char
    char = vals[1][0] # character to check
    if ((vals[2][int(limits[0]) - 1] == char and vals[2][int(limits[1]) - 1] != char) or (vals[2][int(limits[0]) - 1] != char and vals[2][int(limits[1]) - 1] == char)):
        count += 1

print("new system: " + str(count))