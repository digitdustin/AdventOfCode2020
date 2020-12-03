file = open("sums.txt")

lines = file.readlines()

numset = {"0"}

#Part 1: find 2 nubers that sum to 2020
for line in lines:
    numset.add(int(line))
    if ((2020 - int(line)) in numset):
        print(line, 2020 - int(line))
        product = int(line) * (2020 - int(line))
        print("product: " + str(product))

#Part 2: find 3 numbers that sum to 2020
for line in lines:
    numset.ad